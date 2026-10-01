import torch

def dice_statistics(n: int) -> tuple[float, float]:
    """
    Compute the expected value and variance of a fair n-sided die roll using PyTorch.

    Args:
        n (int): Number of sides of the die

    Returns:
        tuple: (expected_value, variance)
    """
    outcomes = torch.arange(1, n+1, dtype=torch.float32)
    mean = torch.mean(outcomes)
    variance = torch.mean((outcomes - mean) ** 2) # Var(X) = E((X-mean)^2)

    return (mean.item(), variance.item())