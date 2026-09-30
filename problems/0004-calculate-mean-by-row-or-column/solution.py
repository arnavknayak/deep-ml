def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = []
	if mode == 'row':
		for i in range(len(matrix)):
			row_sum = 0
			for j in range(len(matrix[0])):
				row_sum += matrix[i][j]
			means.append(row_sum/len(matrix[0]))
		return means
	elif mode == 'column':
		for j in range(len(matrix[0])):
			col_sum = 0
			for i in range(len(matrix)):
				col_sum += matrix[i][j]
			means.append(col_sum/len(matrix))
		return means
	else:
		raise ValueError(f"Mode must be either 'row' or 'column'. Got {mode} instead.")