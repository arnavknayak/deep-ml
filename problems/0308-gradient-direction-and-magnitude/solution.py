import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	
	gradient = np.array(gradient, dtype=float)
	magnitude = np.sqrt(np.sum(gradient ** 2))

	if magnitude == 0:
		return {'magnitude': 0.0, 'direction': [0.0] * len(gradient), 'descent_direction': [0.0] * len(gradient)}
	
	return {'magnitude': magnitude, 'direction': gradient / magnitude, 'descent_direction': -1 * (gradient / magnitude)}