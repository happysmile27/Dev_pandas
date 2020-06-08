import pandas as pd
import numpy as np

c = np.random.randint(0, 100, size=10)
a = pd.Series(c)
print(a.nunique())

# print(pd.unique(a))
