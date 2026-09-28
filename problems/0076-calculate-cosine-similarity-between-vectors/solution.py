import torch
import torch.nn.functional as F

def cosine_similarity(v1: torch.Tensor, v2: torch.Tensor) -> float:
    """
    Calculate the cosine similarity of two vectors using PyTorch.
    Args:
        v1 (torch.Tensor): 1D tensor representing the first vector.
        v2 (torch.Tensor): 1D tensor representing the second vector.
    Returns:
        float: The cosine similarity of the two vectors.
    """
    
    v1 = v1.float()
    v2 = v2.float()

    if v1.shape != v2.shape:
        raise ValueError(f"Input vectors must have same shape. Got {v1.shape} and {v2.shape}")
    
    if v1.numel() == 0:
        raise ValueError(f"Input vectors cannot be empty.")
    
    norm1 = torch.sqrt(torch.sum(v1 ** 2))
    norm2 = torch.sqrt(torch.sum(v2 ** 2))

    if norm1 == 0 or norm2 == 0:
        raise ValueError("Input vectors cannot have zero magnitude.")
    
    dot_product = torch.dot(v1, v2)

    return (dot_product / (norm1 * norm2)).item()