import torch

def empirical_pmf(samples: torch.Tensor) -> list:
    """
    Given a 1D tensor of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    values, counts = torch.unique(samples, return_counts=True)
    probabilities = counts.float() / len(samples)

    return list(zip(values.tolist(), probabilities.tolist()))