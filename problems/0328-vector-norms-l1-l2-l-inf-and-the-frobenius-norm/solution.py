import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    
    arr = arr.float()

    if norm_type == "l1":
        return torch.sum(torch.abs(arr)).item()

    elif norm_type == "l2":
        return torch.sqrt(torch.sum(arr ** 2)).item()
        
    elif norm_type == "linf":
        return torch.max(torch.abs(arr)).item()

    elif norm_type == "frobenius":
        if arr.ndim != 2:
            raise ValueError("Frobenius norm requires a 2D tensor")
        return torch.sqrt(torch.sum(arr ** 2)).item()

    else:
        raise ValueError(f"Unknown norm type: {norm_type}")
        
