# Literature Review

**Topic:** Predicting the compressive strength of concrete from its mix proportions and curing age using machine learning.

## 1. Yeh (1998)

Yeh, I.-C. (1998). Modeling of strength of high-performance concrete using artificial neural networks. *Cement and Concrete Research*, 28(12), 1797–1808. https://doi.org/10.1016/S0008-8846(98)00165-3

This is the source paper for the dataset used in this project. Yeh compiled laboratory test results for high-performance concrete with cement, blast furnace slag, fly ash, water, superplasticizer, aggregates, and curing age as inputs, and trained an artificial neural network to predict compressive strength. The network predicted strength more accurately than a regression-based model, and the author showed it could be used as a virtual laboratory to explore how changing one mix ingredient affects strength.

## 2. Chou, Tsai, Pham and Lu (2014)

Chou, J.-S., Tsai, C.-F., Pham, A.-D., & Lu, Y.-H. (2014). Machine learning in concrete strength simulations: Multi-nation data analytics. *Construction and Building Materials*, 73, 771–780. https://doi.org/10.1016/j.conbuildmat.2014.09.054

The authors gathered concrete strength data from several countries and compared single machine learning models against ensemble approaches built by voting, bagging, and stacking. Their results support the use of these techniques as simple and efficient tools for simulating compressive strength. For this project, the paper justifies testing an ensemble model alongside a single baseline model.

## 3. Young, Hall, Pilon, Gupta and Sant (2019)

Young, B. A., Hall, A., Pilon, L., Gupta, P., & Sant, G. (2019). Can the compressive strength of concrete be estimated from knowledge of the mixture proportions?: New insights from statistical analysis and machine learning methods. *Cement and Concrete Research*, 115, 379–388. https://doi.org/10.1016/j.cemconres.2018.09.006

This study points out that earlier work relied on small laboratory datasets and analyses more than 10,000 job-site mixtures with their recorded 28-day strengths. The same models were also applied to the Yeh laboratory dataset so that performance on field data and laboratory data could be compared. The authors then used the trained models to design mixtures that reach a target strength at minimum cost and embodied CO2, showing a practical use beyond prediction.

## 4. Feng, Liu, Wang, Chen, Chang, Wei and Jiang (2020)

Feng, D.-C., Liu, Z.-T., Wang, X.-D., Chen, Y., Chang, J.-Q., Wei, D.-F., & Jiang, Z.-M. (2020). Machine learning-based compressive strength prediction for concrete: An adaptive boosting approach. *Construction and Building Materials*, 230, 117000. https://doi.org/10.1016/j.conbuildmat.2019.117000

Feng and colleagues trained an AdaBoost model on the same 1,030 records used here, combining many weak decision-tree learners into one strong predictor. Under 10-fold cross-validation the model reached an average R² above 0.95, outperformed neural network and support vector machine models, and generalised to a separate set of 103 samples. They also found that about 80% of the data was enough for training and that decision trees were the best weak learner, which supports the tree-based models chosen for this project.

## 5. Nguyen, Vu, Vo and Thai (2021)

Nguyen, H., Vu, T., Vo, T. P., & Thai, H.-T. (2021). Efficient machine learning models for prediction of concrete strengths. *Construction and Building Materials*, 266, 120950. https://doi.org/10.1016/j.conbuildmat.2020.120950

This paper compared support vector regression, a multilayer perceptron, gradient boosting, and XGBoost for predicting the compressive and tensile strength of high-performance concrete, with hyperparameters tuned by random search. The two gradient boosting methods gave the best accuracy and were also efficient to train. The finding directly motivates the use of a gradient boosting regressor as one of the models in this experiment.

## Synthesis and gap

Across these studies, nonlinear tree ensembles consistently outperform linear models and are competitive with neural networks on mix-design data. Most studies split the Yeh dataset at random, yet the same mixture appears several times at different curing ages, so a random split can place one mixture in both the training and test sets and overstate accuracy. This project therefore evaluates models with a split grouped by mixture, so that every test mixture is unseen during training.
