# CUMCM 2025 模板 (CUMCM-2025-Template)

## 项目的python项目使用`uv`进行包管理
## 为2025年CUMCM作准备
---

## 目录结构详解

本模板的结构如下：

```
.
├── data/
│   ├── raw/              # 存放原始数据
│   └── processed/        # 存放预处理后的数据
├── paper/
│   ├── template/         # 存放可复用的LaTeX模板文件
│   │   ├── cumcm.cls
│   │   └── main.tex
│   └── solution/         # 存放本次竞赛的最终论文
│       ├── main.tex
│       ├── references.bib
│       └── figures/
├── results/
│   ├── figures/          # 存放代码生成的所有图表
│   ├── tables/           # 存放代码生成的关键数据表
│   └── logs/             # 存放运行日志
├── src/
│   ├── template/         # 存放模板化的、可复用的代码模块
│   │   ├── data_processing.py
│   │   ├── modeling.py
│   │   └── visualization.py
│   └── solution/         # 存放针对本次赛题的具体实现代码
│       ├── prompts.md    # 存放与AI协作的指令记录
│       ├── main.py
│       ├── problem1.py
│       └── problem2.py
├── .gitignore            # Git忽略配置文件
├── README.md             # 本指南
└── tmpl.texorigin        # 社区下载的tex文件
```

### 各部分用途说明

*   **`data/`**: 所有数据的存放地。`raw` 用于存放原始数据，`processed` 用于存放清洗后的数据。
*   **`src/`**: 源代码目录，分为两部分：
    *   `template/`: 存放高度抽象、可跨赛题复用的代码模块（如特定算法、绘图函数）。
    *   `solution/`: 存放本次赛题的具体代码实现。`prompts.md` 是核心，用于记录和迭代与AI协作的指令。
*   **`paper/`**: 论文目录，同样分为两部分：
    *   `template/`: 存放官方 `cumcm.cls` 和一个干净的 `main.tex` 结构模板。
    *   `solution/`: 本次竞赛的最终论文工作区。
*   **`results/`**: 存放所有代码运行产生的输出，是连接代码与论文的桥梁。
*   **`pyproject.toml`**: 定义项目依赖和元数据，使用 `uv` 进行管理。

---

## 标准工作流程 (Standard Workflow)

1.  **`Step 0: 环境初始化`**:
    *   创建虚拟环境: `uv venv`
    *   激活虚拟环境: `source .venv/bin/activate` (Linux/macOS) 或 `.venv\Scripts\activate` (Windows)
    *   安装依赖: `uv pip install -r pyproject.toml`
2.  **`Step 1: 数据准备`**: 将原始数据放入 `data/raw/`。
3.  **`Step 2: AI辅助编码`**: 打开 `src/solution/prompts.md`，根据题目要求，设计清晰的指令，引导AI在 `src/solution/` 目录下生成数据处理、模型建立和可视化的代码。可复用 `src/template/` 中的模块。
4.  **`Step 3: 执行与分析`**: 运行 `src/solution/main.py`，生成图、表、日志等结果到 `results/` 目录。
5.  **`Step 4: AI辅助写作`**: 将 `results/` 目录下的关键输出作为上下文，结合 `paper/solution/main.tex` 的结构，在 `prompts.md` 中设计指令，引导AI完成论文初稿的撰写。
6.  **`Step 5: 迭代与完善`**: 审阅、修改和完善代码与论文，直至最终提交。

---

## AI协作指南 (AI Collaboration Guide)

`src/solution/prompts.md` 是AI协作的中央枢纽。所有对AI的请求都应在此记录、迭代和优化。

#### **编码任务**

*   **策略**: 将复杂问题分解为小任务，为每个任务提供清晰的上下文和输入输出规范。
*   **示例指令 (记录于 `prompts.md`)**:
    ```markdown
    ### Prompt for Data Cleaning (Problem 1)

    **Context:**
    - Raw data is located at `data/raw/problem1_data.csv`.
    - The data contains missing values denoted as 'NA'.
    - The 'timestamp' column is in string format.

    **Request:**
    Please write a Python function in `src/solution/problem1.py` named `clean_data`. This function should:
    1. Load the CSV file into a pandas DataFrame.
    2. Convert the 'timestamp' column to datetime objects.
    3. Fill missing numerical values using the column median.
    4. Return the cleaned DataFrame.
    
    You can use modules from `src/template/data_processing.py` if needed.
    ```

#### **论文写作任务**

*   **策略**: 为AI提供精确的数据、图表引用和写作要求（如语气、长度、关键点）。
*   **示例指令 (记录于 `prompts.md`)**:
    ```markdown
    ### Prompt for Results Analysis (Chapter 4.1)

    **Context:**
    - The analysis is for the results section in `paper/solution/main.tex`.
    - The relevant figure is `results/figures/figure2_model_fit.png`.
    - The corresponding data is in `results/tables/model_summary.csv`.

    **Request:**
    Please write a 250-word analysis for Chapter 4.1. The analysis must:
    1. Refer to Figure 2 (`\ref{fig:model_fit}`) and describe the model's goodness of fit.
    2. Quote the R-squared value from the summary table.
    3. Explain the implications of these results for the problem solution.
