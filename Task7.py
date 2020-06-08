import pandas as pd

df = pd.read_csv("/Users/olhafedyshyn/DevRepublic/NobelPrizeWinners.csv")

# a = df[df.Year == 1997]
# print(a)

b = df[df["Full Name"] == "Stanley B. Prusiner"]
print(b["Category"])



