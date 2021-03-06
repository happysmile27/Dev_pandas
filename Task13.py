import pandas as pd

df = pd.read_csv("/Users/olhafedyshyn/DevRepublic/NobelPrizeWinners.csv")

df["Birth Date"] = pd.to_datetime(df["Birth Date"], format="%Y-%m-%d", errors="coerce")
df["Age"] = df["Year"].dt.year - df["Birth Date"].dt.year
a = df.groupby(["Category", "Sex"], as_index=False)[["Age"]].mean()
print(a)