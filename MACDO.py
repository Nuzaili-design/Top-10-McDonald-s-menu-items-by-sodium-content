import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV
df = pd.read_csv(r"C:\Data Analyst\Python\menu.csv")

# here we are showing the first few rows
print(df.head())


# max sodium item
max_sodium_item = df.loc[df['Sodium (mg)'].idxmax()]
print("\nFood with maximum sodium:")
print(max_sodium_item[['Item', 'Sodium (mg)']])

sns.set_theme(style="whitegrid")

#  Bar plot: Top 10 sodium items
top10_sodium = df.nlargest(10, 'Sodium (mg)').sort_values('Sodium (mg)', ascending=False)

plt.figure(figsize=(12, 7))
sns.barplot(
    data=top10_sodium,
    x='Sodium (mg)',
    y='Item',
    palette='Reds_r',
    edgecolor="black"
)

plt.title("Top 10 McDonald's Items by Sodium Content", fontsize=18, fontweight='bold', loc='center', pad=15)
plt.xlabel("Sodium (mg)", fontsize=12)
plt.ylabel("Menu Item", fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.show()
