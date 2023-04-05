import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 238786813 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    x = 2 * x - 0.008
    alpha = (1-p)/2
    s = np.sqrt(np.var(x))
    return x.mean() + norm.ppf(alpha)* s / np.sqrt(len(x)), \
           x.mean() + norm.ppf(1-alpha) * s / np.sqrt(len(x))
