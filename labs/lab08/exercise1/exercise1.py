def filter_passing_scores(input_file, output_file):
    # Read the file
    f = open(input_file, "r")
    lines = f.readlines()
    f.close()

<<<<<<< HEAD
    count = 0
=======
    Args:
        input_file: path to input file (student_id and score on alternating lines)
        output_file: path to output file
>>>>>>> 048e96cb9e64c6144eb3cb4797597ba992221557

    # Open output file
    f = open(output_file, "w")

    # Process lines two at a time
    for i in range(0, len(lines), 2):
        student_id = lines[i].strip()
        score = int(lines[i + 1].strip())

        if score >= 80:
            f.write(f"{student_id} {score}\n")
            count += 1

    f.close()

    return count