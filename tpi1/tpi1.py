# Nmec: 88931
# Author: Vasco António Lopes Ramos

from tree_search import *
import math


class MyNode(SearchNode):
    def __init__(self, state, parent, depth, cost, evalfunc=0):
        super().__init__(state, parent)

        self.depth = depth
        self.evalfunc = evalfunc
        self.children = None
        self.cost = cost

    def in_parent(self, state):
        if self.parent is None:
            return False
        return self.parent.state == state or self.parent.in_parent(state)

    def __str__(self):
        return str(self.state)

    def __repr__(self):
        return str(self)


class MyTree(SearchTree):

    def __init__(self, problem, strategy='breadth', max_nodes=None):
        super().__init__(problem, strategy)

        self.root = MyNode(problem.initial, None, 0, 0, self.problem.domain.heuristic(
            self.problem.initial, self.problem.goal))
        self.open_nodes = [self.root]
        self.strategy = strategy
        self.solution_cost = 0
        self.solution_length = 0
        self.total_nodes = 1
        self.terminal_nodes = 0
        self.non_terminal_nodes = 0
        self.max_nodes = max_nodes
        self.closed_nodes = []

    def astar_add_to_open(self, lnewnodes):
        # Sort all open nodes taking into consideration the evalfunc (heuristic + cost) of each node
        self.open_nodes = sorted(
            self.open_nodes + lnewnodes, key=lambda x: x.evalfunc)

    def effective_branching_factor(self):
        # Algorithm adapted from: http://ozark.hendrix.edu/~ferrer/courses/335/f11/lectures/effective-branching.html
        # 1) Select an error tolerance
        # 2) Average the estimates to provide a guess for b* using a d + threshold (initially 0)
        # 3) Calculate N' using the guess for b* and d_
        # 4) If abs(N' - N) > error, modify the b_ estimate accordingly
        # 5) Otherwise, it is within the error, so return the guess for b*
        n = self.total_nodes
        d = self.solution_length
        d_ = d
        error_tolerance = 0.001

        guess = math.pow(n, 1/d_)

        n_computed = sum([math.pow(guess, i) for i in range(d+1)])

        while abs(n - n_computed) > error_tolerance:
            guess = math.pow(n, 1/d_)
            n_computed = sum([math.pow(guess, i) for i in range(d+1)])
            d_ += 0.000001

        return guess

    def update_ancestors(self, node):
        # 1) Check if the node has children
        # 2) If it has, calculate de child with min value of evalfun and change the parent evalfunc to the child one.
        #    If does not have children, do nothing
        # 3) If the node has parent (i.e. it's not the root node), we will propagate the algorithm to the parent nodes recursively
        if node.children is not None:
            node.evalfunc = sorted([node.evalfunc for node in node.children], key= lambda node: node)[0]
        
            if node.parent is not None:
                self.update_ancestors(node.parent)

    def discard_worse(self):
        # 1) Get the parent nodes that have leaf nodes as children
        #    (may there be parent nodes that have some children that are not leafs)
        # 2) Filter the previous list to ensure that the (parent) nodes we have only have leaf nodes as children
        # 3) Get the parent node with the highest value of evalfunc
        # 4) Remove from the open nodes the children of the node that resulted from 3) step
        #    (remove also the children from the node itself [node.children property])
        # 5) Add to the open nodes the node that resulted from 3) step
        parent_nodes = set(map(lambda node: node.parent, filter(lambda node: node.children is None, self.open_nodes)))

        parent_nodes_with_leaf_children = []

        for parent_node in parent_nodes:
            if  all([node.children is None for node in parent_node.children]):
                parent_nodes_with_leaf_children.append(parent_node)

        parent_nodes_with_leaf_children = sorted(parent_nodes_with_leaf_children, key = lambda node: node.evalfunc, reverse = True)

        if parent_nodes_with_leaf_children != []:
            node_with_higher_evalfunc = parent_nodes_with_leaf_children[0]

            for children_node in node_with_higher_evalfunc.children:
                if children_node in self.open_nodes:
                    self.open_nodes.remove(children_node)

            self.add_to_open([node_with_higher_evalfunc])
            self.closed_nodes.remove(node_with_higher_evalfunc)

            node_with_higher_evalfunc.children = None          

    def search2(self):
        while self.open_nodes != []:
            self.terminal_nodes = len(self.open_nodes)
            node = self.open_nodes.pop(0)
            
            self.non_terminal_nodes = len(self.closed_nodes)
            self.closed_nodes.append(node)

            if self.max_nodes is not None:
                while self.terminal_nodes + self.non_terminal_nodes > self.max_nodes:
                    self.discard_worse()
                    self.terminal_nodes = len(self.open_nodes) + 1
                    self.non_terminal_nodes = len(self.closed_nodes) - 1
    
                    
            if self.problem.goal_test(node.state):
                self.solution_cost = node.cost
                self.solution_length = node.depth
                return self.get_path(node)

            lnewnodes = []
            for a in self.problem.domain.actions(node.state):
                newstate = self.problem.domain.result(node.state, a)
                if not node.in_parent(newstate):
                    newnode = MyNode(newstate, node, node.depth + 1, node.cost + self.problem.domain.cost(
                        node.state, a), self.problem.domain.heuristic(newstate, self.problem.goal))
                    newnode.evalfunc += newnode.cost 

                    lnewnodes.append(newnode)
                    self.total_nodes += 1

            if lnewnodes != []:
                node.children = lnewnodes
            self.update_ancestors(node)
            self.add_to_open(lnewnodes)
        return None

    # shows the search tree in the form of a listing
    def show(self, heuristic=False, node=None, indent=''):
        if node == None:
            self.show(heuristic, self.root)
            print('\n')
        else:
            line = indent+node.state
            if heuristic:
                line += (' [' + str(node.evalfunc) + ']')
            print(line)
            if node.children == None:
                return
            for n in node.children:
                self.show(heuristic, n, indent+'  ')
