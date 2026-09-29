import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """  
    data = np.array(data)

    mean = float(np.mean(data))
    median = float(np.median(data))

    unique, counts = np.unique(data, return_counts=True)
    max_count = np.max(counts)
    modes = unique[counts == max_count]
    mode = int(modes[0])

    variance = float(np.var(data))
    std_dev = float(np.std(data))

    p25, p50, p75 = [float(p) for p in np.percentile(data, [25, 50, 75])]

    iqr = p75 - p25

    return {
        "mean": mean,
        "median": median,
        "mode": mode,
        "variance": variance,
        "standard_deviation": std_dev,
        "25th_percentile": p25,
        "50th_percentile": p50,
        "75th_percentile": p75,
        "interquartile_range": iqr
    }