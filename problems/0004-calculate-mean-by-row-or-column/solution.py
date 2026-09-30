def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	if mode == 'row':
		return [sum(matrix[i])/len(matrix[0]) for i in range(len(matrix))]
	elif mode == 'column':
		return [sum(matrix[i][j] for i in range(len(matrix)))/len(matrix) for j in range(len(matrix[0]))]
	else:
		raise ValueError(f"Mode must be either 'row' or 'column'. Got {mode} instead.")