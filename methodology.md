# Methodology

## 1. Refined research question

How accurately can the compressive strength of concrete (MPa) be predicted from its mix proportions and curing age for **mixtures the model has never seen**, and do nonlinear tree ensembles (Random Forest, Gradient Boosting) with domain-informed ratio features outperform a linear regression baseline?

Two supporting questions follow from the literature review:

- **RQ-a:** Do engineered ratio features (for example water-to-cement and water-to-binder ratios) improve accuracy over the raw ingredient quantities?
- **RQ-b:** How much does a random train/test split overstate accuracy compared with a split grouped by mixture?

## 2. Dataset description

| Item | Detail |
|---|---|
| Source | UCI Machine Learning Repository, *Concrete Compressive Strength* (Yeh, 1998) |
| Size | 1,030 rows, 9 columns, no missing values |
| Unit of observation | One laboratory strength test of one mixture at one curing age |
| Target | Concrete compressive strength, MPa (range about 2.3–82.6) |

**Features (8, all numeric):**

| Feature | Unit | Notes |
|---|---|---|
| Cement | kg/m³ | Never zero |
| Blast furnace slag | kg/m³ | Zero in 466 rows (supplementary cementitious material not used) |
| Fly ash | kg/m³ | Zero in 566 rows |
| Water | kg/m³ | |
| Superplasticizer | kg/m³ | Zero in 379 rows |
| Coarse aggregate | kg/m³ | |
| Fine aggregate | kg/m³ | |
| Age | days | 14 distinct values from 1 to 365; 28 days is the most common |

**Limitations:**

- **Repeated mixtures.** The 1,030 rows contain only about 430 distinct mixtures; many are tested at several ages. Rows are therefore not independent, and a random split leaks mixture information into the test set.
- **Laboratory data from a single compilation.** Results may not transfer to job-site concrete, where curing, placement, and material variability differ (Young et al., 2019).
- **Missing explanatory variables.** No cement type, aggregate type or size, admixture chemistry, curing temperature or humidity, or specimen geometry.
- **Uneven age coverage.** Very early (1 day) and very late (120–365 days) ages have few records, so predictions there are less reliable.
- **Small size** for complex models, which limits hyperparameter tuning and favours simpler ensembles.

## 3. Data cleaning plan

1. Rename the long original column headers to short snake_case names.
2. Check types, missing values, and physical plausibility of ranges (no negative quantities, age between 1 and 365 days, positive strength).
3. **Treat zeros as genuine values**, not missing data: a zero means the ingredient was not used in that mixture.
4. **Remove exact duplicate rows** (25 found in exploration).
5. **Average replicate tests:** where the same mixture at the same age has more than one strength value, replace them with their mean so that each mixture–age pair appears once.
6. **Keep statistical outliers** in strength and quantities, because they reflect real high-strength or unusual mixes rather than recording errors; flag them in the exploratory analysis only.
7. **Assign a mixture ID** to each unique combination of the seven ingredient quantities; this ID drives the grouped split.

## 4. Feature engineering plan

Concrete strength is governed largely by the water-to-binder ratio (Abrams' law) and by hydration over time, so ratios carry more signal than absolute quantities.

| Engineered feature | Definition | Rationale |
|---|---|---|
| `binder` | cement + slag + fly ash | Total cementitious content |
| `w_c` | water / cement | Classic Abrams' law ratio |
| `w_b` | water / binder | Ratio that accounts for supplementary materials |
| `scm_frac` | (slag + fly ash) / binder | Share of binder replaced by slower-reacting materials |
| `sp_b` | superplasticizer / binder | Admixture dosage relative to binder |
| `agg_b` | (coarse + fine aggregate) / binder | Paste content indicator |
| `fine_frac` | fine aggregate / total aggregate | Grading indicator |
| `log_age` | ln(age) | Strength gain is roughly logarithmic in time |

Two feature sets are compared: **raw** (the 8 original variables) and **engineered** (the 7 ingredients plus the 8 features above). Features are standardised for the linear model only; tree models do not need scaling.

## 5. Models and rationale

| Model | Why |
|---|---|
| **Linear Regression** (standardised inputs) | Transparent baseline; tests how far a linear relationship, helped by ratio and log-age features, can go |
| **Random Forest Regressor** | Bagged tree ensemble that captures nonlinear interactions (for example age × binder) with little tuning and is robust on small data; supported by ensemble results in Chou et al. (2014) |
| **Gradient Boosting Regressor** | Boosted tree ensemble that the literature reports as the strongest learner on this problem (Feng et al., 2020; Nguyen et al., 2021) |

Hyperparameters for the two ensembles are tuned with a small randomised search using 5-fold `GroupKFold` cross-validation on the training set only.

## 6. Evaluation design and metrics

**Split.** A `GroupShuffleSplit` holds out 20% of mixtures (all ages of each held-out mixture) as the test set, with a fixed random seed. Model selection uses grouped cross-validation on the remaining 80%. For RQ-b, the best model is also evaluated under an ordinary random 80/20 split to measure leakage.

**Metrics.**

| Metric | Role | Why |
|---|---|---|
| **RMSE (MPa)** | Primary | In the units engineers use, and penalises large errors more heavily; an over-predicted strength is a safety concern |
| **MAE (MPa)** | Secondary | Typical error size, less sensitive to a few large misses |
| **R²** | Secondary | Share of variance explained; allows comparison with published results |

Results are also checked with predicted-versus-actual plots, residuals by curing age, and feature importances to confirm that the model behaves in line with concrete engineering knowledge.

## References

- Chou, J.-S., Tsai, C.-F., Pham, A.-D., & Lu, Y.-H. (2014). *Construction and Building Materials*, 73, 771–780.
- Feng, D.-C., et al. (2020). *Construction and Building Materials*, 230, 117000.
- Nguyen, H., Vu, T., Vo, T. P., & Thai, H.-T. (2021). *Construction and Building Materials*, 266, 120950.
- Yeh, I.-C. (1998). *Cement and Concrete Research*, 28(12), 1797–1808.
- Young, B. A., Hall, A., Pilon, L., Gupta, P., & Sant, G. (2019). *Cement and Concrete Research*, 115, 379–388.
