import math

def activation_derivatives(x: float) -> dict[str, float]:
	"""
	Compute the derivatives of Sigmoid, Tanh, and ReLU at a given point x.
	
	Args:
		x: Input value
		
	Returns:
		Dictionary with keys 'sigmoid', 'tanh', 'relu' and their derivative values
	"""
	sigmoid = 1 / (1+math.exp(-x))
	grad_sigmoid = sigmoid * (1-sigmoid)

	grad_tanh = 1 - (math.tanh(x) ** 2)

	grad_relu = 1 if x > 0 else 0

	return {
		'sigmoid': grad_sigmoid,
		'tanh': grad_tanh,
		'relu': grad_relu
	}