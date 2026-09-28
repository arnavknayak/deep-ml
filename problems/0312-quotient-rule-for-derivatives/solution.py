import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """

    def evaluate(coeffs: list, x: float) -> float:
        return sum(coeffs[i] * (x ** (len(coeffs)-1-i)) for i in range(len(coeffs)))
        
    def derive(coeffs: list) -> list:
        return [coeffs[i] * (len(coeffs)-1-i) for i in range(len(coeffs)-1)]
    
    hx = evaluate(h_coeffs, x)
    gx = evaluate(g_coeffs, x)
    dhx = evaluate(derive(h_coeffs), x)
    dgx = evaluate(derive(g_coeffs), x)
    
    return (hx * dgx - gx * dhx) / (hx ** 2)