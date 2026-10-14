# Ostaad — Predicting Concrete Compressive Strength from Mix Design

Research design and experiment on predicting the compressive strength of concrete (MPa) from its mix proportions and curing age, using the UCI Concrete Compressive Strength dataset (Yeh, 1998).

## Final outputs

- **Paper:** [`paper.md`](paper.md)
- **Notebook:** [`experiment.ipynb`](experiment.ipynb)
- **Slides:** [`slides.pptx`](slides.pptx) ([PDF](slides.pdf))

## Repository contents

| File | Purpose |
|---|---|
| `literature_review.md` | Summaries of five sources on machine learning for concrete strength prediction |
| `methodology.md` | Research question, dataset, cleaning, feature engineering, models, and evaluation plan |
| `experiment.ipynb` | Cleaning, feature engineering, model training, and evaluation (outputs retained) |
| `data/Concrete_Data.csv` | UCI Concrete Compressive Strength dataset, converted from the original `.xls` |
| `paper.md` | Final research paper: abstract, introduction, methodology, results, discussion, conclusion, references |
| `slides.pptx` / `slides.pdf` | 6-slide presentation: problem, method, results, takeaway |
| `figures/` | Charts used in the paper and slides |
| `make_figures.py` | Builds the figures from the notebook results |
| `make_slides.py` | Builds `slides.pptx` from the figures |
| `references.bib` | Reference library (BibTeX, Zotero-importable) |
| `requirements.txt` | Python packages needed to rerun the notebook |

## Reproduce

```bash
pip install -r requirements.txt
jupyter nbconvert --to notebook --execute --inplace experiment.ipynb
python make_figures.py
python make_slides.py
```

## Data licence

Reuse of the dataset is unlimited with retention of the copyright notice for Prof. I-Cheng Yeh and the following paper: I-Cheng Yeh, "Modeling of strength of high performance concrete using artificial neural networks," *Cement and Concrete Research*, 28(12), 1797–1808 (1998). Source: [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/165/concrete+compressive+strength).
