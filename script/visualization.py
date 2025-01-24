import matplotlib.pyplot as plt
import seaborn as sns

def plot_numerical_distributions(df):
    """Plot distributions of numerical features."""
    plt.figure(figsize=(12, 8))
    for i, column in enumerate(df.select_dtypes(include=['float64', 'int64']).columns, 1):
        plt.subplot(3, 1, i)
        sns.histplot(df[column], bins=10, kde=True)
        plt.title(f'Distribution of {column}')
    plt.tight_layout()
    plt.show()

def plot_categorical_distribution(df, column):
    """Plot distribution of categorical features."""
    plt.figure(figsize=(8, 5))
    sns.countplot(x=column, data=df)
    plt.title(f'Distribution of {column}')
    plt.show()

def plot_correlation_matrix(df):
    """Plot correlation matrix."""
    correlation_matrix = df.corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Matrix')
    plt.show()

def plot_boxplots(df):
    """Plot boxplots for numeric features to detect outliers."""
    plt.figure(figsize=(12, 8))
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    num_rows = (len(numeric_columns) // 2) + (len(numeric_columns) % 2)
    for i, column in enumerate(numeric_columns, 1):
        plt.subplot(num_rows, 2, i)
        sns.boxplot(y=df[column])
        plt.title(f'Box Plot of {column}')
    plt.tight_layout()
    plt.show()