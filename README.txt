Random_Walk, v1.1.1, for modeling random walks: https://en.wikipedia.org/wiki/Random_walk

constructor:
	Random_Walk(pos, step)
		pos = starting position
			pos should support + operation
		step = function for taking a step
		
to access the complete history of positions, use RandomWalk.walk_history after taking a step
	RandomWalk.walk_history is not accessible when no steps have been taken - then, RandomWalk.pos should be enough
	
Install module with python setup.py install
Run tests with python setup.py test