# -*- coding: utf-8 -*-
"""
Reusable visualization modules for CUMCM.
This script contains templates for common plotting functions.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# AI-PROMPT: It's a good practice to standardize plot aesthetics.
# You can define a setup function to apply consistent styling.
def setup_plot_style():
    """Sets a consistent and professional style for all plots."""
    sns.set_theme(style="whitegrid")
    plt.rcParams['font.family'] = 'sans-serif' # Use a common font
    plt.rcParams['font.sans-serif'] = ['SimHei'] # Specify Chinese font if needed
    plt.rcParams['axes.unicode_minus'] = False # Fix for displaying minus sign
    plt.rcParams['figure.figsize'] = (10, 6)
    plt.rcParams['axes.labelsize'] = 12
    plt.rcParams['xtick.labelsize'] = 10
    plt.rcParams['ytick.labelsize'] = 10
    plt.rcParams['legend.fontsize'] = 10

def save_figure(fig, name: str, save_dir: str = "results/figures"):
    """
    Saves a matplotlib figure to the specified directory.

    Args:
        fig: The matplotlib figure object.
        name (str): The name of the file (without extension).
        save_dir (str): The directory to save the figure in.
    """
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    path = os.path.join(save_dir, f"{name}.png")
    fig.savefig(path, dpi=300, bbox_inches='tight')
    print(f"Figure saved to {path}")
    plt.close(fig)


# AI-PROMPT: This is a template for plotting a time series.
# Please adapt it by specifying the correct column names for x and y axes.
# You can also customize labels, title, and colors.

def plot_time_series_template(df: pd.DataFrame, x_col: str, y_col: str, title: str, filename: str):
    """
    Generates and saves a time series plot from a DataFrame.

    Args:
        df (pd.DataFrame): DataFrame containing the time series data.
        x_col (str): The name of the column for the x-axis (e.g., 'date').
        y_col (str): The name of the column for the y-axis (e.g., 'value').
        title (str): The title of the plot.
        filename (str): The filename for the saved plot.
    """
    setup_plot_style()
    fig, ax = plt.subplots()
    ax.plot(df[x_col], df[y_col], marker='o', linestyle='-')
    ax.set_title(title)
    ax.set_xlabel(x_col.replace('_', ' ').title())
    ax.set_ylabel(y_col.replace('_', ' ').title())
    plt.xticks(rotation=45)
    save_figure(fig, filename)


# AI-PROMPT: This is a template for a correlation matrix heatmap.
# It's useful for exploring relationships between variables.
# You can select a subset of columns to visualize if the DataFrame is too large.

def plot_correlation_matrix_template(df: pd.DataFrame, columns: list, title: str, filename: str):
    """
    Generates and saves a correlation matrix heatmap.

    Args:
        df (pd.DataFrame): DataFrame containing the data.
        columns (list): A list of column names to include in the correlation matrix.
        title (str): The title of the plot.
        filename (str): The filename for the saved plot.
    """
    setup_plot_style()
    correlation_matrix = df[columns].corr()
    
    fig, ax = plt.subplots(figsize=(12, 10))
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
    ax.set_title(title)
    save_figure(fig, filename)