# Nmec: 88931
# Author: Vasco António Lopes Ramos
# Course: LEI


from semantic_network import *
from bayes_net import *
from statistics import mean


class MySN(SemanticNetwork):
	def query_dependents(self, entity):
		"""
		Function that returns a list with all entities which operation depends on the correct operation of a given Entity.
		:param entity: The entity for which we want to search it's dependents.
		:return: A list with all the dependents of the given entity. If there is none, then an empty list.
		"""
		result, query = [], filter(lambda d: d.relation.entity2 == entity and (isinstance(d.relation, Depends) or isinstance(d.relation, Subtype)), self.declarations)
		for ent in query:
			subs = [e.relation.entity1 for e in self.query_local(e2 = ent.relation.entity1, rel = "subtype")]
			result += (subs if (subs and isinstance(ent.relation, Depends)) else [ent.relation.entity1] if isinstance(ent.relation, Depends) else []) + self.query_dependents(ent.relation.entity1)
		return list(set(result))

	def query_causes(self, entity):
		"""
		Function that returns the list of all entities whose failure or malfunction can cause failure or malfunction in a given Entity.
		:param entity: The entity for which we want to search for possible causes of failure or malfunction.
		:return: A list with all the possible causes of failure or malfunction in the given entity. If there is none, then an empty list.
		"""
		result, query = [], filter(lambda d: d.relation.entity1 == entity and (isinstance(d.relation, Depends) or isinstance(d.relation, Subtype)), self.declarations)
		for ent in query:
			deps = [e.relation.entity2 for e in self.query_local(e1 = ent.relation.entity1, rel = "depends")]
			result += (deps if deps else [ent.relation.entity2] if isinstance(ent.relation, Depends) else []) + self.query_causes(ent.relation.entity2)
		return list(set(result))

	def query_causes_sorted(self, entity):
		"""
		Function that returns the list of all entities whose failure or malfunction can cause failure or malfunction in a given Entity sorted.
		:param entity: The entity for which we want to search for possible causes of failure or malfunction.
		:return: A list with all the possible causes of failure or malfunction in the given entity. If there is none, then an empty list.
				 The list is sorted first by the time to fix and then, in case of a tie, by the alphabetical value of the components.
		"""
		return sorted([(c, mean(list(map(lambda e: e.relation.entity2, self.query_local(e1=c, rel="debug_time"))))) for c in self.query_causes(entity)], key = lambda x: (x[1], x[0]))


class MyBN(BayesNet):
	def parents(self, var, exclude = None):
		"""
		Function that returns the list with the parents of a given 'var' node.
		:param var: The 'var' node for which we want to know the parent nodes.
		:param (optional) exclude: The entity to exclude from parents list.
		:return: A list with all the parents of a given 'var' node. If there is none, then an empty list.
		"""
		return list(set([k for i in self.dependencies[var].keys() for k in dict(i).keys() if k != exclude]))

	def markov_blanket(self, var):
		"""
		Return the markov blanket for a given 'var' node.
		:param var: The 'var' node for which we want to compute the markov blanket.
		:return: A list with all the nodes that belong to the markov blanket of a given 'var' node. 
		"""
		children = list(set([k for k, v in self.dependencies.items() if var in [k for i in v.keys() for k in dict(i).keys()]]))
		return list(set(self.parents(var) + children + [y for x in [self.parents(c, var) for c in children] for y in x]))


