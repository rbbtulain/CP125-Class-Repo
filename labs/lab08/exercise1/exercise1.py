def filter_passing_scores(input_file, output_file):
   
    score = open(input_file, "r")
    lines = score.readlines()
    score.close()

    count = 0

  
    passing = open(output_file, "w")

    for row in lines:
        student_id = row[0,2,4,6,8,10]
        score = [1,3,5,7,9,11]

    if score >= 80:
            passing.write(f"{student_id} {score}\n")
            count += 1

    passing.close()

    return count