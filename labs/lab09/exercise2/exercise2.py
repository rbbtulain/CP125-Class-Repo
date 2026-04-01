import pandas as pd

def compare_averages(filename):
    df = pd.read_csv(filename)

    math_avg = round(df['Math'].mean(), 1)
    sci_avg = round(df['Science'].mean(), 1)
    eng_avg = round(df['English'].mean(), 1)

    averages = {
        "Math": math_avg,
        "Science": sci_avg,
        "English": eng_avg
    }

    best = max(averages, key=averages.get)
    worst = min(averages, key=averages.get)

    averages["best_subject"] = best
    averages["worst_subject"] = worst

    return averages