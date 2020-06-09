import pandas as pd

df = pd.read_csv("/Users/olhafedyshyn/DevRepublic/NobelPrizeWinners.csv")

# def cent(n):
#     if n >= 2000:
#         return "XX"
#     else:
#         return "XIX"
# new_col = df["century"] = df.apply(cent(df.Year))
# print(new_col)

df["Century"] = df["Year"].apply(lambda x: "XIX" if x < 2000 else "XX")
print(df["Year"],  df["Century"])
