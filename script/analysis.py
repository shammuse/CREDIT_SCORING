from loaddata import load_data
from cleandata import clean_data
from visualization import plot_numerical_distributions, plot_categorical_distribution, plot_correlation_matrix, plot_boxplots

def analyze_data(file_path):
    """Load, clean, and analyze data."""
    # Load data
    df = load_data(file_path)

    # Clean data
    df_cleaned = clean_data(df)

    # Visualization
    plot_numerical_distributions(df_cleaned)
    plot_categorical_distribution(df_cleaned, 'FraudResult')  # Adjust column name as necessary
    plot_correlation_matrix(df_cleaned)
    plot_boxplots(df_cleaned)

    # Return cleaned DataFrame
    return df_cleaned