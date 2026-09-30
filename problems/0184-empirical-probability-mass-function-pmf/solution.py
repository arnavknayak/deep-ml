def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    n = len(samples)
    pmf = {}
    for i in samples:
        if i not in pmf:
            pmf[i] = 0
        pmf[i] += 1
    
    res = []
    for k, v in pmf.items():
        res.append((k, v/n))

    return res