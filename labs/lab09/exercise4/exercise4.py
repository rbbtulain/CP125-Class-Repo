import pandas as pd
import matplotlib.pyplot as plt


def show_science_distribution(filename):
    df = pd.read_csv(filename)
    
    science_score = df["Science"]

    plt.hist(science_score, bins=10)
    plt.title("Science Score Distribution")
    plt.xlabel("Science Score")
    plt.ylabel("Frequency")
   
    plt.show()

    return len(science_scores)


