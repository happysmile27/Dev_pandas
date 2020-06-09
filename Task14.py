import pandas as pd

df = pd.read_csv("/Users/olhafedyshyn/DevRepublic/NobelPrizeWinners.csv")

temp1 = df.groupby(["Category", "Sex"])[["Sex"]].count()
temp1.rename(columns={"Sex": "Count"}, inplace=True)
temp1.reset_index(inplace=True)
temp2 = df.groupby("Category", as_index=False)[["Sex"]].count()
temp2.rename(columns={"Sex": "Total_Count"}, inplace=True)

temp_df = pd.merge(temp1, temp2, how="left", on="Category")
temp_df["Ratio"] = temp_df["Count"] / temp_df["Total_Count"]
print(temp_df)