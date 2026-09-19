# PRODIGY_DS_04

## Prodigy InfoTech Data Science Internship – Task 04

### Task

Analyze and visualize sentiment patterns in social media data to understand the distribution of positive, neutral, and negative sentiment.

### Dataset

This project uses the **TweetEval Sentiment Dataset**.

The dataset contains tweets labeled as:

- Negative
- Neutral
- Positive

Dataset Source:

https://github.com/cardiffnlp/tweeteval/tree/main/datasets/sentiment

### Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn
- Regular Expressions

### Data Processing

The following steps were performed:

- Loaded TweetEval training tweets and sentiment labels.
- Mapped numerical sentiment labels to:
  - 0 → Negative
  - 1 → Neutral
  - 2 → Positive
- Counted the distribution of sentiment labels.
- Extracted frequently occurring words from positive and negative tweets.
- Removed selected common stop words.
- Generated visualizations to explore sentiment distribution and frequent terms.

### Sentiment Distribution

A total of **45,615 tweets** were analyzed.

| Sentiment | Tweets | Percentage |
|---|---:|---:|
| Positive | 17,849 | 39.1% |
| Neutral | 20,673 | 45.3% |
| Negative | 7,093 | 15.5% |

### Visualizations

#### 1. Sentiment Distribution

`outputs/sentiment_distribution.png`

This chart shows the number of tweets belonging to each sentiment category.

#### 2. Frequent Positive and Negative Terms

`outputs/sentiment_terms.png`

This visualization shows the most frequently occurring terms in positive and negative tweets after basic text processing.

The term-frequency charts are descriptive and do not by themselves establish causation or public consensus.

### Project Structure

```text
PRODIGY_DS_04/
│
├── data/
│   ├── train_text.txt
│   └── train_labels.txt
│
├── outputs/
│   ├── sentiment_distribution.png
│   ├── sentiment_terms.png
│   └── findings.txt
│
├── task04.py
├── README.md
└── requirements.txt
How to Run

Clone the repository:

git clone https://github.com/Vedanshu-Fegade/PRODIGY_DS_04.git

Navigate to the project directory:

cd PRODIGY_DS_04

Install the required libraries:

pip install -r requirements.txt

Run the analysis:

python task04.py

The generated visualizations and findings will be saved in the outputs folder.

Learning Outcomes

Through this task, the following concepts were practiced:

Social media sentiment analysis
Text preprocessing
Regular expressions
Word-frequency analysis
Data visualization
Pandas data analysis
Matplotlib visualization
Seaborn visualization
Exploratory data analysis
Internship

Prodigy InfoTech – Data Science Internship

