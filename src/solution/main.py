# -*- coding: utf-8 -*-
"""
CUMCM 2025 Template: Main Execution Script for the Solution

This script serves as the main entry point for running the entire analysis pipeline
for the competition problem. It orchestrates the data processing, modeling, and
visualization steps.

Usage:
    python src/solution/main.py
"""

import logging

# It's better to import your own modules with absolute paths
# assuming 'src' is the root for execution.
# For example: from solution import data_processing, modeling, visualization
# This might require setting PYTHONPATH=. or running as `python -m solution.main`
# For simplicity in a competition setting, we can use relative imports if
# this script is run from the `src/solution` directory, but it's less robust.
# Let's stick to a more robust approach. We'll assume you run from the root.
# To make this work, we add the project root to the path.
import sys
import os

# Add project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)

from src.solution import problem1
from src.solution import problem2
# Import other problem modules as you create them

def setup_logging():
    """Configures the logging for the application."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("results/logs/solution.log"),
            logging.StreamHandler()
        ]
    )

def main():
    """
    Main function to execute the solution pipeline.
    """
    setup_logging()
    logging.info("Starting CUMCM 2025 solution pipeline...")

    # --- Problem 1 ---
    logging.info("="*30)
    logging.info("Executing solution for Problem 1...")
    # Example of how you might structure the call
    # cleaned_data = problem1.clean_and_prepare_data('data/raw/problem1_data.csv')
    # model_results = problem1.run_model(cleaned_data)
    # problem1.generate_visualizations(model_results)
    logging.info("Problem 1 execution finished.")
    logging.info("="*30)


    # --- Problem 2 ---
    logging.info("="*30)
    logging.info("Executing solution for Problem 2...")
    # Add calls for problem 2 here
    logging.info("Problem 2 execution finished.")
    logging.info("="*30)


    # --- Add other problems as needed ---


    logging.info("Solution pipeline finished successfully.")


if __name__ == '__main__':
    # Create logs directory if it doesn't exist
    if not os.path.exists('results/logs'):
        os.makedirs('results/logs')
    main()