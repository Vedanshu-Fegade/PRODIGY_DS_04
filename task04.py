"""Task 04 — analyse real social-media sentiment.

Dataset: TweetEval sentiment (tweets labelled negative, neutral, or positive)
Source: https://github.com/cardiffnlp/tweeteval/tree/main/datasets/sentiment
"""
from collections import Counter
from pathlib import Path
from urllib.request import urlretrieve
import re

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
OUT = ROOT / "outputs"
TEXT_URL = "https://raw.githubusercontent.com/cardiffnlp/tweeteval/main/datasets/sentiment/train_text.txt"
LABEL_URL = "https://raw.githubusercontent.com/cardiffnlp/tweeteval/main/datasets/sentiment/train_labels.txt"
LABELS = {0: "Negative", 1: "Neutral", 2: "Positive"}
STOP_WORDS = {"the", "and", "for", "that", "this", "with", "you", "are", "was", "have", "from", "but", "not", "they", "will", "your", "just", "about", "has", "been", "its", "it's", "our", "all", "out", "get", "https", "http", "amp"}


def load_data() -> pd.DataFrame:
    DATA_DIR.mkdir(exist_ok=True)
    text_file, label_file = DATA_DIR / "train_text.txt", DATA_DIR / "train_labels.txt"
    if not text_file.exists() or not label_file.exists():
        print("Downloading TweetEval sentiment data…")
        urlretrieve(TEXT_URL, text_file)
        urlretrieve(LABEL_URL, label_file)
    texts = text_file.read_text(encoding="utf-8").splitlines()
    labels = [int(item) for item in label_file.read_text(encoding="utf-8").splitlines()]
    return pd.DataFrame({"text": texts, "sentiment": [LABELS[x] for x in labels]})


def top_words(texts: pd.Series, limit: int = 12) -> pd.Series:
    words = []
    for text in texts:
        words.extend(word.lower() for word in re.findall(r"[A-Za-z]{3,}", text)
                     if word.lower() not in STOP_WORDS)
    return pd.Series(dict(Counter(words).most_common(limit))).sort_values()


def main() -> None:
    sns.set_theme(style="whitegrid")
    OUT.mkdir(exist_ok=True)
    df = load_data()
    order = ["Positive", "Neutral", "Negative"]
    plt.figure(figsize=(7, 5))
    sns.countplot(data=df, x="sentiment", hue="sentiment", order=order, legend=False, palette="Set2")
    plt.title("Sentiment Distribution in TweetEval Training Tweets")
    plt.xlabel("Sentiment label")
    plt.ylabel("Tweet count")
    plt.tight_layout()
    plt.savefig(OUT / "sentiment_distribution.png", dpi=180)
    plt.close()

    fig, axes = plt.subplots(1, 2, figsize=(13, 6))
    for axis, sentiment, color in zip(axes, ["Positive", "Negative"], ["#54A24B", "#E45756"]):
        words = top_words(df.loc[df["sentiment"] == sentiment, "text"])
        axis.barh(words.index, words.values, color=color)
        axis.set(title=f"Most Frequent {sentiment} Tweet Terms", xlabel="Occurrences", ylabel="")
    fig.tight_layout()
    fig.savefig(OUT / "sentiment_terms.png", dpi=180)
    plt.close(fig)

    counts = df["sentiment"].value_counts()
    (OUT / "findings.txt").write_text(
        f"Tweets analysed: {len(df):,}\n"
        + "\n".join(f"{label}: {counts.get(label, 0):,} ({counts.get(label, 0) / len(df):.1%})" for label in order)
        + "\nThe term charts are descriptive; they do not by themselves establish causation or public consensus.\n",
        encoding="utf-8",
    )
    print(f"Task 04 complete — figures saved in {OUT}")


if __name__ == "__main__":
    main()
