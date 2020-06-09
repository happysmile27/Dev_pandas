import pandas as pd

df = pd.read_csv("/Users/olhafedyshyn/DevRepublic/NobelPrizeWinners.csv")

a = df["Sex"].value_counts() * 100 / df.shape[0]
print(a)

c = df["Sex"].value_counts(normalize=True)
print(c)