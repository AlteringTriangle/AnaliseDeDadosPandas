import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pokemon = pd.read_csv('pokemon.csv')

print(pokemon.to_dict())