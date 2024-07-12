import pandas as pd

data = {"Fruits": ['Apple', 'Mango', 'Orange'],
        "Quantity": [4, 8, 7]}

data2 = {"Veggies": ['Cauliflower', 'Bottlegaurd', 'Brocolli'],
        "Quantity": [2, 1, 4]}
df = pd.DataFrame(data)

print(df)

df2 = pd.DataFrame(data2)
df3 = pd.concat([df, df2])
print(df3)
