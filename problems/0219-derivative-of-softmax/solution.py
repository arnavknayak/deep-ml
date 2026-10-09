import numpy as np

def softmax_derivative(x: list[float]) -> list[list[float]]:
	"""
	Compute the Jacobian matrix of the softmax function.
	
	Args:
		x: Input vector of real numbers
		
	Returns:
		Jacobian matrix J where J[i][j] = d(softmax_i)/d(x_j)
	"""
	x = np.array(x)
	s = np.exp(x - np.max(x))
	s = s / np.sum(s)

	return np.diag(s) - s[:, None] @ s.T[None, :]