import numpy as np
import math

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	
	dot_prod = np.dot(v1, v2)
	v1_norm = np.sqrt(np.sum(v1 ** 2))
	v2_norm = np.sqrt(np.sum(v2 ** 2))

	return dot_prod / (v1_norm * v2_norm)
