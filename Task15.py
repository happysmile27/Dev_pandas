import pandas as pd

table_1 = pd.DataFrame({
    'user_id': [1, 2, 3, 4, 5, 6, 7],
    'user_name': ['Sophia', 'Mary', 'Luca', 'Natalie', 'John', 'Bob', 'Eliza'],
    'user_source': ['google_ppc', 'facebook_ads', 'google_ppc', 'direct',
                    'direct', 'bing_ads', 'organic_seach']
})

# table_2 = pd.DataFrame({
#     'user_id': [2, 2, 3, 4, 5, 5, 5, 6, 8],
#     'user_preferences': ['clothes', 'baby clothes', 'accessories',
#                          'clothes', 'gadgets', 'accessories',
#                          'healthcare', 'baby clothes', 'gadgets']

table1_new = table_1.append({"user_id" : 13, "user_name": "Jill", "user_source": "bing_ads"}, ignore_index=True)
print(table1_new)