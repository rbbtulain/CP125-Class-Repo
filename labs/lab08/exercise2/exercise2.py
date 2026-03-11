def merge_lists(file1, file2, output_file):
    names = set()

    # Read first file
    f = open(file1, "r")
    for line in f:
        names.add(line.strip())
    f.close()

    # Read second file
    f = open(file2, "r")
    for line in f:
        names.add(line.strip())
    f.close()

    # Sort names
    sorted_names = sorted(names)

    # Write to output file
    f = open(output_file, "w")
    for name in sorted_names:
        f.write(name + "\n")
    f.close()

    return len(sorted_names)