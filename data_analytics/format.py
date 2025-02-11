import pandas as pd

data = {'date': ['2022-01-01', '2022-02-01', '2022-03-01'],
        'time': ['12:00:00', '13:30', '15:45']}

df = pd.DataFrame(data)
print(df)

# Formatting date and time data in a specific format
df['date'] = pd.to_datetime(df['date']).dt.strftime('%d-%m-%Y')
df['time'] = pd.to_datetime(df['time']).dt.strftime('%H:%M:%S')

print("\n --------Formatted data---------\n")
print(df)
