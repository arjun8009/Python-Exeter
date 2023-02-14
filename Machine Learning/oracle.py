import numpy as np

def oracle_sigma():
    sigma = 9.1
    return sigma

def oracle_mean():
    mu = 171
    return mu

def oracle_sample():
    mu = oracle_mean()
    sigma = oracle_sigma()
    samples = sigma*np.random.randn(1) + mu
    sample = samples[0]
    return sample