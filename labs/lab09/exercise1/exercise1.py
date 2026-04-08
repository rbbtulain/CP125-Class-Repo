import pandas as pd

def explore_data(filename):

    df = pd.read_csv(filename)
    
    row = df.shape[0]
    

    subject = ["Math", "Science", "English"]
    

    math_avg = float(df["Math"].mean())

    highest_score = max(df["Math"])

    name = df.loc[df["Math"] == highest_score, 'Name'].values[0]
    

    return {
        "total_students": row,
        "subjects": subject,
        "math_average": math_avg,
        "highest_math_student": name
    }

result = explore_data("data/students.csv")
print(result)
# {
#     "total_students": 25,
#     "subjects": ["Math", "Science", "English"],
#     "math_average": 84.0,
#     "highest_math_student": "Hassan"
# }