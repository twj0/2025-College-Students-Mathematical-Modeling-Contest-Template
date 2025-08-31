# AI Collaboration Prompts for CUMCM 2025

This document is the central hub for managing and iterating on prompts for AI assistants. All prompts used for code generation, data analysis, and paper writing should be recorded here.

---

## Part 1: Code Generation

### Prompt 1.1: Data Cleaning
*(Please fill in the details below before sending to the AI)*

**Context:**
- **Goal:** Clean the raw data for initial analysis.
- **Raw Data File:** `data/raw/your_data_file.csv`
- **Output File:** `data/processed/cleaned_data.csv`
- **Key Cleaning Steps:** [e.g., Handle missing values, correct data types, remove duplicates, etc.]

**Request:**
"Please write a Python function in `src/solution/data_processing.py`. The function, named `clean_and_prepare_data`, should:
1. Load the data from `data/raw/your_data_file.csv`.
2. Perform the following cleaning steps: [Specify the steps clearly].
3. Save the cleaned DataFrame to `data/processed/cleaned_data.csv`.
4. Return the cleaned DataFrame.
Please include detailed docstrings and comments."

---

### Prompt 1.2: Model Implementation
*(Please fill in the details below before sending to the AI)*

**Context:**
- **Goal:** Implement the core mathematical model.
- **Model Type:** [e.g., Linear Programming, Time Series Forecasting, Classification Model]
- **Input Data:** `data/processed/cleaned_data.csv`
- **Key Mathematical Equations/Logic:** [Provide the core formulas or logical steps]

**Request:**
"In the file `src/solution/modeling.py`, please implement a function called `solve_optimization_model`. This function should:
1. Take the cleaned DataFrame as input.
2. Formulate the [Model Type] based on the provided mathematical logic.
3. Use the `scipy.optimize` library to solve the model.
4. Return the solution (e.g., optimal values, status)."

---

## Part 2: Paper Writing

### Prompt 2.1: Results Analysis
*(Please fill in the details below before sending to the AI)*

**Context:**
- **Goal:** Write the results analysis section of the paper.
- **Target Section in `paper/solution/main.tex`:** `\section{Results Analysis}`
- **Relevant Figure:** `results/figures/figure_name.png` (Label: `\ref{fig:figure_label}`)
- **Relevant Table:** `results/tables/table_name.csv`
- **Key Findings to Highlight:** [e.g., The model achieved 95% accuracy, Parameter X is most sensitive, etc.]

**Request:**
"Please write a 300-word analysis for the 'Results Analysis' section of our paper. You must:
1. Refer to the figure `\ref{fig:figure_label}` and explain what it shows.
2. Incorporate key values from the table `results/tables/table_name.csv`.
3. Emphasize the key findings listed above.
4. Maintain a formal and academic tone."