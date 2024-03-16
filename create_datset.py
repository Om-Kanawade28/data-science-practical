import pandas as pd
df = pd.DataFrame(columns=['company','model','year'])
df.loc[0] = ['tata','nexon',2027]
df.loc[1] = ['mg','astor',2021]
df.loc[2] = ['kia','seltos',2019]
print(df)
