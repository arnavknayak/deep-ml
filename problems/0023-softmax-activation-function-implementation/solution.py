import math

def softmax(scores: list[float]) -> list[float]:
    shift = max(scores)
    scores_shifted = [x-shift for x in scores]
    normalization = sum(math.exp(x) for x in scores_shifted)
    return [math.exp(x) / normalization for x in scores_shifted]