import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 238786813 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    s = np.sqrt(np.var(x))
    return x.max() + norm.ppf(alpha / 2)* s / np.sqrt(len(x)), \
           x.max() + norm.ppf(1-alpha / 2) * s / np.sqrt(len(x))
