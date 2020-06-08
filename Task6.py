import pandas as pd

df = pd.read_csv("/Users/olhafedyshyn/DevRepublic/NobelPrizeWinners.csv")

print(df["Category"].value_counts())
print(df["Category"].value_counts()[:5])