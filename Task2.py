import pandas as pd

ser_A = pd.Series([1, 2, 3, 4, 5])
ser_B = pd.Series([4, 5, 6, 7, 8])

print(ser_A[~ser_A.isin(ser_B)])


