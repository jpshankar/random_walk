import pytest, sys

from randomWalk.random_walk import RandomWalk

from typing import Generator

from randomWalk.steps_generating_exception import StepsGeneratingException

from dataclasses import dataclass

class TestRandomWalk:
	def setup_class(cls):
		cls.step_count = 5
		
	def setup_method(self, method):
		name = method.__name__
		
		if name.endswith('pos_without_add'):
			@dataclass(repr=False, eq=False, order=False, unsafe_hash=True)
			class PosWithoutAdd:
				pos: int
					
			step_function = lambda: PosWithoutAdd(1)
			
			ini_pos = PosWithoutAdd(0)
			
			self.random_walk = RandomWalk(pos=ini_pos, step=step_function)
		else:
			step_probs = {
				-1: 1,
				1: 1
			}
			
			step = RandomWalk.simple_step_function(step_probs)
			self.random_walk = RandomWalk(pos=0, step=step)
		
	def test_steps_as_list(self):
		rw_list = self.random_walk.steps_list(5)
		assert isinstance(rw_list, list)
		assert len(rw_list) == 5
		
	def test_steps_as_generator(self):
		rw_gen = self.random_walk.steps_generator(5)
		assert isinstance(rw_gen, Generator)
		
	def test_single_step(self):
		prev_pos = self.random_walk.pos
		
		self.random_walk.single_step()
		
		assert self.random_walk.pos != prev_pos
		assert len(self.random_walk.walk_history) == 2
		
	def test_only_one_generator(self):
		self.random_walk.steps_generator(5)
		with pytest.raises(StepsGeneratingException):
			self.random_walk.steps_generator(5)
			
	def test_new_generator_after_old_one(self):
		rw_gen = self.random_walk.steps_generator(self.step_count)
		for _ in range(self.step_count):
			next(rw_gen)
		
		rw_gen = self.random_walk.steps_generator(self.step_count)
		next(rw_gen)
		
	def test_list_during_generator(self):
		rw_gen = self.random_walk.steps_generator(self.step_count)
		next(rw_gen)
		
		rw_list = self.random_walk.steps_list(5)
		assert len(self.random_walk.walk_history) == 7
		
	def test_generator_after_list(self):
		rw_gen = self.random_walk.steps_generator(self.step_count)
		next(rw_gen)
		
		rw_list = self.random_walk.steps_list(5)
		
		next(rw_gen)
		assert len(self.random_walk.walk_history) == 8
		
	def test_step_with_pos_without_add(self):
		with pytest.raises(TypeError):
			self.random_walk.single_step()
			
	def test_list_with_pos_without_add(self):
		with pytest.raises(TypeError):
			self.random_walk.steps_list(self.step_count)
			
	def test_generator_with_pos_without_add(self):
		with pytest.raises(TypeError):
			rw_gen = self.random_walk.steps_generator(self.step_count)
			next(rw_gen)