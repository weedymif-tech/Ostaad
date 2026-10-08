# Ostaad — Predicting Concrete Compressive Strength from Mix Design

Research design and experiment on predicting the compressive strength of concrete (MPa) from its mix proportions and curing age, using the UCI Concrete Compressive Strength dataset (Yeh, 1998).

## Repository contents

| File | Purpose |
|---|---|
| `literature_review.md` | Summaries of five sources on machine learning for concrete strength prediction |
| `methodology.md` | Research question, dataset, cleaning, feature engineering, models, and evaluation plan |
| `experiment.ipynb` | Cleaning, feature engineering, model training, and evaluation (outputs retained) |
| `data/Concrete_Data.csv` | UCI Concrete Compressive Strength dataset, converted from the original `.xls` |
| `requirements.txt` | Python packages needed to rerun the notebook |

## Reproduce

```bash
pip install -r requirements.txt
jupyter nbconvert --to notebook --execute --inplace experiment.ipynb
```

## Data licence

Reuse of the dataset is unlimited with retention of the copyright notice for Prof. I-Cheng Yeh and the following paper: I-Cheng Yeh, "Modeling of strength of high performance concrete using artificial neural networks," *Cement and Concrete Research*, 28(12), 1797–1808 (1998). Source: [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/165/concrete+compressive+strength).
