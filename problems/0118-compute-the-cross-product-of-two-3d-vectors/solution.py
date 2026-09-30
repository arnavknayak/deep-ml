import torch

def cross_product(a, b) -> torch.Tensor:
    """
    Compute the cross product of two 3D vectors a and b.
    Parameters:
        a (array-like or torch.Tensor): A 3-element vector.
        b (array-like or torch.Tensor): A 3-element vector.
    Returns:
        torch.Tensor: The cross product tensor.
    """
    a_t = torch.tensor(a, dtype=torch.float32)
    b_t = torch.tensor(b, dtype=torch.float32)

    return torch.cross(a_t, b_t, dim=0)