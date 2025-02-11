import pandas as pd

data = {'A':[1000,2000,3000],
        'B':[0.2232,0.625, 0.235]}

df = pd.DataFrame(data)
print(df)

print("\n -----Formatted data-----")
df.style.format({'B':'{:.2f}'})
