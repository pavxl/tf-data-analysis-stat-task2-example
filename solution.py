import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 362844815

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    t = x.max() - 0.05
    n = len(x)
    return 0.05 + t / ((1 - alpha / 2)**(1 / n)), \
           0.05 + t / ((alpha / 2)**(1 / n))
