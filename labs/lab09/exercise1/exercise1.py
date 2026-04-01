import pandas as pd

def explore_data(filename):
    df = pd.read_csv(filename)

    return {
        "total_students": len(df),
        "subjects": ['Math', 'Science', 'English'],
        "math_average": round(df['Math'].mean(), 1),
        "highest_math_student": df.loc[df['Math'].idxmax(), 'Name']
    }