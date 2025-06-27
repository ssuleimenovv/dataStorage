import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./appearances.csv')

# data review
print("Dataset Overview:")
print(df.info())
print("\nMissing Values:")
print(df.isnull().sum())
print("\nBasic Statistics:")
print(df.describe())

# missed value checking
df = df.fillna(df.median(numeric_only=True))

# data loc
plt.figure(figsize=(12, 6))
sns.boxplot(data=df.select_dtypes(include=['number']))
plt.title("Boxplot for Numerical Columns")
plt.xticks(rotation=45)
plt.show()

# histogram
plt.figure(figsize=(12, 6))
df.hist(figsize=(12, 8), bins=20)
plt.suptitle("Histograms of Numeric Features")
plt.show()

# analysis
correlation_matrix = df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Matrix")
plt.show()

# business-suggestion
if 'minutes_played' in df.columns:
    avg_minutes = df.groupby('player_id')['minutes_played'].mean()
    print("\nTop 10 Players by Average Minutes Played:")
    print(avg_minutes.nlargest(10))

print("\nData Analysis Completed.")
