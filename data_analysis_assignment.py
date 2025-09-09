# Data Analysis Assignment: Pandas and Matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Load and Explore the Dataset
try:
    # Load Iris dataset from seaborn
    df = sns.load_dataset('iris')
    print("Dataset loaded successfully.")
except Exception as e:
    print("Error loading dataset:", e)
    exit()

print("\nFirst five rows:")
print(df.head())

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

# Clean dataset (drop missing values)
df_clean = df.dropna()
print("\nDataset cleaned. Shape:", df_clean.shape)

# Task 2: Basic Data Analysis
print("\nBasic statistics:")
print(df_clean.describe())

# Group by species and compute mean petal_length
grouped = df_clean.groupby('species')['petal_length'].mean()
print("\nMean petal length per species:")
print(grouped)

# Task 3: Data Visualization

# 1. Line chart: mean petal length per species
plt.figure(figsize=(6,4))
grouped.plot(kind='line', marker='o')
plt.title('Mean Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Mean Petal Length')
plt.grid(True)
plt.show()

# 2. Bar chart: average sepal width per species
plt.figure(figsize=(6,4))
df_clean.groupby('species')['sepal_width'].mean().plot(kind='bar', color=['skyblue','salmon','lime'])
plt.title('Average Sepal Width per Species')
plt.xlabel('Species')
plt.ylabel('Average Sepal Width')
plt.show()

# 3. Histogram: distribution of petal length
plt.figure(figsize=(6,4))
plt.hist(df_clean['petal_length'], bins=20, color='purple', alpha=0.7)
plt.title('Distribution of Petal Length')
plt.xlabel('Petal Length')
plt.ylabel('Frequency')
plt.show()

# 4. Scatter plot: sepal length vs petal length
plt.figure(figsize=(6,4))
sns.scatterplot(data=df_clean, x='sepal_length', y='petal_length', hue='species')
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.legend(title='Species')
plt.show()

# Findings/Observations
print("\nObservations:")
print("- Setosa species has the shortest petal length on average.")
print("- Petal length distribution is skewed towards lower values.")
print("- Sepal length and petal length are positively correlated, especially for versicolor and virginica.")
