import pandas as pd

data = {'A': [1, 22, 333],
        'B': [4444, 55555, 666666]}

df = pd.DataFrame(data)
print(df)

# # Aligning data within columns (left alignment)
df.style.set_properties(**{'text-align': 'left'})
