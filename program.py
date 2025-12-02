import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data.csv")
df['Year'] = df['Year'].astype('Int64')

#drop the null values and duplicates 
df.drop_duplicates(inplace = True)
df.dropna(subset=['Year'],inplace=True)
df.dropna(subset=['Publisher'],inplace=True)

# ---------------------------------------------------------
#                     JEFFREY'S GRAPHS
# ---------------------------------------------------------
#Graph settings

sns.set_theme(style="whitegrid", palette="deep")

# --- GRAPH 1: Total Global Video Game Sales Over Time ---
sales_per_year = df.groupby('Year')['Global_Sales'].sum().reset_index()

sns.lineplot(data=sales_per_year, x = "Year", y = "Global_Sales", marker = 'o', palette="flare")
plt.title("Total Global Video Game Sales Over Time")
plt.xlabel("Year")
plt.ylabel("Global Sales (Millions)")
plt.tight_layout()
plt.savefig("sales_over_time.png")
plt.show()

# --- GRAPH 2: Number of Games Released Per Year ---
plt.figure(figsize=(12,6))
games_per_year = df.groupby('Year')['Name'].count().reset_index()

sns.barplot(data=games_per_year, x='Year', y='Name', palette='crest')
plt.title("Number of Games Released Per Year")
plt.xlabel("Year")
plt.ylabel("Number of Games")
plt.tight_layout()
plt.xticks(rotation=45)
plt.savefig("games_per_year.png")
plt.show()

# --- GRAPH 3: Market Share of Top 10 Platforms ---
platform_sales = df.groupby('Platform')['Global_Sales'].sum().sort_values(ascending=False).head(10)
colors = sns.color_palette("Paired", 10)

plt.figure(figsize=(10,10))
plt.axis('equal')
plt.pie(platform_sales.values, labels=platform_sales.index, autopct='%1.1f%%', startangle=90, colors=colors)
plt.title("Market Share of Top 10 Platforms")
plt.tight_layout()
plt.savefig("platform_market_share.png")
plt.show()
exit()
# --- GRAPH 4: Genre Sales by Region (NA, EU, JP) ---
region_genre = df.groupby('Genre')[['NA_Sales', 'EU_Sales', 'JP_Sales']].sum().reset_index()

region_genre_long = region_genre.melt( id_vars='Genre', value_vars=['NA_Sales', 'EU_Sales', 'JP_Sales'], var_name='Region', value_name='Sales')


sns.barplot(data=region_genre_long, x='Genre', y='Sales', hue='Region', palette='bright')
plt.title("Genre Sales by Region")
plt.xlabel("Genre")
plt.ylabel("Sales (Millions)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("genre_by_region.png")
plt.show()

# ---------------------------------------------------------
#                        ADAM'S GRAPHS
# ---------------------------------------------------------
#Question: How many games were made for each console?
# --- GRAPH 5: Number of Games per Console ---
counts = df['Platform'].value_counts()

#plotting the data frame
plt.figure(figsize=(12,6))
counts.plot(kind='bar')

#labeling the axises and titling the graph
plt.xlabel("Console")
plt.ylabel("Number of Games")
plt.title("Number of Games per Console")
plt.tight_layout()
plt.savefig('games_per_console.png')
plt.show()


# --- GRAPH 6: Publishers with Most PS2 Games ---

#Question: How many games did each developer make for the Play Station 2?

#Filtering so it is only Play Station 2 games
df_ps2 = df[df['Platform'] == 'PS2']

#Tallying up the number of games on the Play Station 2
counts_ps2 = df_ps2['Publisher'].value_counts()

#Filter out the data so it only displays the top 50% of companies in terms of games made for the system
top_50_index = int(len(counts_ps2) * 0.5)
counts_top50 = counts_ps2.iloc[:top_50_index]

#Plotting the verticle bar graph
counts_top50.plot(kind='bar', figsize=(12, 6))

plt.xlabel("Development Company")
plt.ylabel("Number of Games")
plt.title("Top 50% Companies by Number of Games on the PS2")
#rotating the x axis titles to make it more readable
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('games_on_ps2.png')
plt.show()


# --- GRAPH 7: Publishers with Most DS Games ---
#Question: How many games did each developer make for the Nintendo DS?

#Filtering so it is only DS games
df_ds = df[df['Platform'] == 'DS']

#Tallying up the number of games on the DS
counts_ds = df_ds['Publisher'].value_counts()

#Filter out the data so it only displays the top 50% of companies in terms of games made for the system
top_50_percent_index = int(len(counts_ds) * 0.5)
counts_top50 = counts_ds.iloc[:top_50_percent_index]

#Plotting the verticle bar graph
plt.figure(figsize=(12,6))
counts_top50.plot(kind='bar')

plt.xlabel("Development Company")
plt.ylabel("Number of Games")
plt.title("Top 50% Companies by Number of Games on the DS")
plt.tight_layout()
plt.savefig('games_on_ds.png')
plt.show()

# ---------------------------------------------------------
#                         LIBAN'S GRAPHS
# ---------------------------------------------------------

# Set the visual style
sns.set(style="whitegrid")

# --- GRAPH 8: Total Global Sales by Genre ---

plt.figure(figsize=(12, 6))
genre_sales = df.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False)
sns.barplot(x=genre_sales.index, y=genre_sales.values, palette="viridis")
plt.title('Total Global Sales by Video Game Genre', fontsize=16)
plt.xlabel('Genre', fontsize=12)
plt.ylabel('Global Sales (Millions)', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('sales_by_genre.png')
plt.show()

# --- Graph 9: Top 10 Platforms by Global Sales ---
plt.figure(figsize=(12, 6))
platform_sales = df.groupby('Platform')['Global_Sales'].sum().sort_values(ascending=False).head(10)
sns.barplot(x=platform_sales.index, y=platform_sales.values, palette="magma")
plt.title('Top 10 Gaming Platforms by Global Sales', fontsize=16)
plt.xlabel('Platform', fontsize=12)
plt.ylabel('Global Sales (Millions)', fontsize=12)
plt.tight_layout()
plt.savefig('top_platforms.png')
plt.show()

# --- Graph 10: HeatMap of Genre vs. Platform Sales ---
top_platforms = df.groupby('Platform')['Global_Sales'].sum().sort_values(ascending=False).head(10).index
heatmap_data = df[df['Platform'].isin(top_platforms)]
pivot_table = heatmap_data.pivot_table(index='Genre', columns='Platform', values='Global_Sales', aggfunc='sum')

# Create Heatmap
plt.figure(figsize=(14, 10))
sns.heatmap(
    pivot_table,
    annot=True,     # Show the actual numbers
    fmt=".0f",      # Format as whole numbers
    cmap="YlGnBu",  # Color map (Yellow to Green to Blue)
    linewidths=.5,  # Add lines between cells
    cbar_kws={'label': 'Global Sales (Millions)'}
)
plt.title('Heatmap: Global Sales Concentration by Genre and Platform', fontsize=18)
plt.xlabel('Platform', fontsize=14)
plt.ylabel('Genre', fontsize=14)
plt.tight_layout()
plt.savefig('genre_platform_heatmap.png')
plt.show()

# --- Graph 11: Evolution of Top Genres Over Time ---
evolution_data = df[(df['Year'] >= 1995) & (df['Year'] <= 2016)]
genre_sales_year = evolution_data.groupby(['Year', 'Genre'])['Global_Sales'].sum().unstack()

# Select top 5 genres for clarity, group the rest as "Others"
top_genres = df.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False).head(5).index
genre_sales_year = genre_sales_year[top_genres]

# Plot
genre_sales_year.plot(kind='area', stacked=True, alpha=0.8, colormap='tab10', figsize=(14, 8))
plt.title('Evolution of Gaming Market Share by Top Genres (1995-2016)', fontsize=18)
plt.ylabel('Global Sales (Millions)', fontsize=14)
plt.xlabel('Year', fontsize=14)
plt.legend(title='Genre', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('genre_evolution_area.png')
plt.show()