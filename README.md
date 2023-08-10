## Sentence Similarity Model for Requirements Analysis

![Python](https://img.shields.io/badge/-Python-000000?style=flat&logo=Python)
![Scikit-Learn](https://img.shields.io/badge/-Scikit.Learn-000000?style=flat&logo=Scikit-Learn)
![Pandas](https://img.shields.io/badge/-Pandas-000000?style=flat&logo=Pandas)
![NLTK](https://img.shields.io/badge/-NLTK-000000?style=flat&logo=NLTK)

> This a generalized version of the project. The specific code, architecture, and data are property of the client and
> cannot be fully shared.

A `Text Similarity` model to support the requirements analysis phase for [CN](https://www.linkedin.com/company/cn/), in 
the railways industry.

### Business Problem

Over 118 L1 requirements were elicited from the stakeholders. The business wanted to ensure that the requirements were
not redundant and that they were linked to the business goals. The business also wanted to identify similar requirements
to group them together and avoid duplication of work.

### Implementation

#### Data

The data was provided in a `xlsx` file containing the `requirements traceability matrix (RTM)`. The RTM is a table that
shows the relationship between the requirements and the other artifacts of the project. The RTM is used to make sure
that each requirement adds business value by being linked to a business goal.

#### Preprocessing

The data was preprocessed using `NLTK`. The requirements were tokenized, lemmatized, and vectorized using `TF-IDF`.
The `TF-IDF` vectorizer was used to transform the requirements into a matrix of TF-IDF features. The `TF-IDF` features
were then used to calculate the cosine similarity between the requirements.

#### Results

Below matrix shows the top `cosine similarity` between the requirements.

<img align="center" src="https://github.com/danvargg/requirements-similarity/blob/main/images/sim_matrix.png">

### Business Results

The business was able to use the model to identify similar requirements and decrease elicited requirements redundancy by
8%.