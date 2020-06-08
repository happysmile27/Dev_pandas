GermanCars = {
    'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'],
    'Price': [23845, 171995, 135925 , 71400]}
JapaneseCars = {
    'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '],
    'Price': [29995, 23600, 61500 , 58900]}

import pandas as pd

German = pd.DataFrame(GermanCars)
Japanese = pd.DataFrame(JapaneseCars)
frames = [German, Japanese]
c = pd.concat(frames, keys=["German", "Japanese"])

print(c)