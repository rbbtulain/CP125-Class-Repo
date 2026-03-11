def filter_passing_scores(input_file, output_file):
    # Read the file
    f = open(input_file, "r")
    lines = f.readlines()
    f.close()

    count = 0

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