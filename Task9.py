import pandas as pd

df = pd.read_csv("/Users/olhafedyshyn/DevRepublic/NobelPrizeWinners.csv")

temp_df = df[~df["Death Date"].isnull()] #is Nan
temp_df.reset_index(drop=True)
temp_df["Death Date"] = temp_df["Death Date"].dt.year

print(temp_df)

df["Year_DT"] = pd.to_datetime(df["Year"], format="%Y")
c = df["Year_DT"].dt.year
print(c)
