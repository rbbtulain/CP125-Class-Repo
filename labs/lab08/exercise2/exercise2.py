# Lab 08 Exercise 2: Text File Merger
# Write your code below:

def merge_lists(file1, file2, output_file):
    """
    Merge two lists of names, remove duplicates, and sort.

    Args:
        file1: path to first list file
        file2: path to second list file
        output_file: path to output file

    Returns:
        int: count of unique names
    """
    # list1
    list1 = open(file1, "r")
    lines1 = list1.readlines()
    list1.close()

    # list2
    list2 = open(file2, "r")
    lines2 = list2.readlines()
    list2.close()

    #empty list 
    result = []

    for line in lines1:
        if line not in lines2:
            result.append()

    result.sort()

    merge = open(output_file, "w")
    for name in result:
        merge.write(name + "\n")
    merge.close()

    
    return len(result)


    



# Test your code here
result = merge_lists("data/list1.txt", "data/list2.txt", "data/merged.txt")
print(f"Unique names: {result}")
