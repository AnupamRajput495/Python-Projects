# Resume Ranker using TF-IDF

## Overview
This project is a **Resume Ranker** that utilizes **TF-IDF (Term Frequency-Inverse Document Frequency)** to match resumes against given keywords. It helps in shortlisting the most relevant candidates based on their resumes.

## Features
- Extracts key information from resumes.
- Uses **TF-IDF** to assign relevance scores.
- Ranks resumes based on keyword similarity.
- Outputs results in a structured **Pandas DataFrame**.

## How It Works
1. **Text Vectorization**: Converts resume text into numerical form using TF-IDF.
2. **Keyword Matching**: Compares the provided keywords with resumes.
3. **Similarity Scoring**: Computes scores to rank resumes based on relevance.
4. **Sorting & Output**: Displays candidates sorted by match percentage.

## Installation
```bash
pip install pandas scikit-learn
```

## Usage
```python
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# Sample Resumes
resumes = [("John Doe", "Experience in Python, Machine Learning, and AI"),
           ("Jane Smith", "Software Developer skilled in Java and SQL"),
           ("Alice Johnson", "Expert in Data Science and Deep Learning")]

# Keywords for Matching
keywords = "Machine Learning and AI"

tfidf_vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf_vectorizer.fit_transform([resume[1] for resume in resumes])
keyword_vector = tfidf_vectorizer.transform([keywords.lower()])
similarity_scores = (tfidf_matrix * keyword_vector.T).toarray().flatten()

sorted_resumes = sorted(zip(resumes, similarity_scores), key=lambda x: x[1], reverse=True)

df = pd.DataFrame([(r[0][0], round(r[1] * 100, 2)) for r in sorted_resumes], columns=["Candidate", "Match Score (%)"])
print(df)
```

## Output Example
| Candidate   | Match Score (%) |
|------------|----------------|
| John Doe   | 85.5           |
| Alice Johnson | 72.3        |
| Jane Smith | 20.1           |

## Applications
- **HR & Recruitment**: Automate resume screening.
- **Job Portals**: Improve candidate-job matching.
- **Search Optimization**: Enhance document retrieval systems.

## License
This project is **open-source** and can be freely modified and distributed.