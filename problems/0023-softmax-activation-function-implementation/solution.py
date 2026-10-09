import math

def softmax(scores: list[float]) -> list[float]:
    max_score = max(scores)
    shifted = [x-max_score for x in scores]
    exponentiated = [math.exp(x) for x in shifted]
    normalization = sum(exponentiated)

    return [x / normalization for x in exponentiated]