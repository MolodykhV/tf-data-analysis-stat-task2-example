import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 238786813 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = p
    loc = x.mean()
    return (loc - 0.008)/(1-alpha/2)+0.008, \
           (loc - 0.008)/(alpha/2)+0.008
