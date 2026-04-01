import pandas as pd

def explore_data(filename):
    df = pd.read_csv(filename)

    row = df.shape[0]

    subj1 = list(df.columns)[2]
    subj2 = list(df.columns)[3]
    subj3 = list(df.columns)[4]

    math_avg = float(df["Math"].mean())

    highest_score = max(df["Math"])

    name = df.loc[df["Math"] == highest_score, 'Name'].values[0]

    return {
        "total_students": row,
        "subjects": [subj1, subj2, subj3],
        "math_average": f"{math_avg}:.1}",
        "highest_math_student": name
    }