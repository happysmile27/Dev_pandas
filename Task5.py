import pandas as pd

df = pd.read_csv("/Users/olhafedyshyn/DevRepublic/NobelPrizeWinners.csv")
for col in df:
    print(col)
    print(type(col))

sort_df = pd.DataFrame(df, columns=["Full Name"])
print(sort_df)


#969 rows x 18 columns