import pandas as pd

table_1 = pd.DataFrame({
    'user_id': [1, 2, 3, 4, 5, 6, 7],
    'user_name': ['Sophia', 'Mary', 'Luca', 'Natalie', 'John', 'Bob', 'Eliza'],
    'user_source': ['google_ppc', 'facebook_ads', 'google_ppc', 'direct',
                    'direct', 'bing_ads', 'organic_seach']
})

table_2 = pd.DataFrame({
    'user_id': [2, 2, 3, 4, 5, 5, 5, 6, 8],
    'user_preferences': ['clothes', 'baby clothes', 'accessories',
                         'clothes', 'gadgets', 'accessories',
                         'healthcare', 'baby clothes', 'gadgets']
})

table_2["name"] = ["Brown", "Brown", "Black", "White", "Smith", "Smith", "Smith", "Griffin", "Simpson"]
print(table_2)