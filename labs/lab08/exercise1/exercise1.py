def filter_passing_scores(input_file, output_file):
   
    score = open(input_file, "r")
    lines = score.readlines()
    score.close()

    count = 0

  
    passing = open(output_file, "w")

    if score >= 80:
            passing.write(f"{student_id} {score}\n")
            count += 1

    passing.close()

    return count