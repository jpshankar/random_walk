import random

from typing import Any, Callable, Dict, List

from dataclasses import dataclass

from randomWalk.steps_generating_exception import StepsGeneratingException

@dataclass(repr=False, eq=False, order=False, unsafe_hash=True)
class RandomWalk:
	pos: Any
	step: Callable = None
	
	'''
	given a dictionary of step_choice: probability format, returns a function for returning a randomly chosen step
	'''
	@classmethod
	def simple_step_function(cls, step_probs: Dict):
		return lambda: random.choices(list(step_probs.keys()), weights=list(step_probs.values()))[0]
	
	'''
	takes step_count steps, returns a list of those steps
	'''
	def steps_list(self, step_count: int):
		try:
			hi_start = len(self.walk_history) if hasattr(self, 'walk_history') else 0
			for _ in range(step_count):
				self.single_step()
			return self.walk_history[hi_start+1:]
		except:
			raise
	'''
	returns a generator for taking step_count steps
	'''
	def steps_generator(self, step_count: int):
		if not hasattr(self, 'generating') or not self.generating:
			self.generating = True
			
			def generator():
				for i in range(step_count):
					self.single_step()
					if i == step_count - 1:
						self.generating = False
					yield self.pos
					
			return generator()
		elif self.generating:
			raise StepsGeneratingException('Step generator already created')
	
	'''
	takes a single step
	'''
	def single_step(self):
		'''
		creates walk_history (a record of the position at step i) if it doesn't exist
			walk_history[0] is the starting position
		'''
		if not hasattr(self, 'walk_history'):
			self.walk_history = [self.pos]
			
		pos_step = self.step()
		try:
			self.pos+=pos_step
			self.walk_history.append(self.pos)
		except:
			raise