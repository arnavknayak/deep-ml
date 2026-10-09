import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	scores = np.array(scores)
	max_score = np.max(scores)
	shifted = scores - max_score
	normalization = np.log(np.sum(np.exp(shifted)))

	return scores - max_score - normalization