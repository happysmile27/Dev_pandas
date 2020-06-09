import pandas as pd

df = pd.read_csv("/Users/olhafedyshyn/DevRepublic/NobelPrizeWinners.csv")

a = df.groupby("Full Name")[["Full Name"]].count()
a.rename(columns={"Full Name": "Count"}, inplace=True)
a.reset_index(inplace=True)
a.sort_values("Full Name", ascending=True, inplace=True)
c = a["Full Name"][a["Count"] > 1].reset_index(drop=True)

print(c)

b = pd.merge(left=a, right=df[["Full Name", "Organization Name"]], on="Full Name", how="left")
print(b)