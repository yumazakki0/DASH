import pandas as pd

df = pd.read_csv('data/usuarios.csv', dtype=str)
df['usuario'] = df['usuario'].str.strip()
df['senha'] = df['senha'].str.strip()

print(df)
print(df[(df['usuario'] == 'yumazakki') & (df['senha'] == '253042')])
