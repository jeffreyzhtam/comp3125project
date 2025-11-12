import pandas as pd

df = pd.read_csv("data.csv")
print(df.shape)
df.drop_duplicates(inplace = True)

df.dropna(subset=['Year'],inplace=True)
df.dropna(subset=['Publisher'],inplace=True)

print(df.shape)
platform_groups = {platform: data for platform, data in df.groupby('Platform')}
#print(platform_groups.keys())

genre_groups = {genre: data for genre, data in df.groupby('Genre')}
#print(genre_groups.keys())

publisher_groups = {publisher: data for publisher, data in df.groupby('Publisher')}
#print(publisher_groups.keys())