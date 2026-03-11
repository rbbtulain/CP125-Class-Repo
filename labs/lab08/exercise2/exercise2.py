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
  
    f1 = open(file1, "r")
    names1 = set(f1.readlines())
    f1.close()


    f2 = open(file2, "r")
    names2 = set(f2.readlines())
    f2.close()

    
    unique_names = names1 | names2


    sorted_names = sorted(unique_names)

    
    f_out = open(output_file, "w")
    for name in sorted_names:
        f_out.write(name)  
    f_out.close()

    return len(sorted_names)


# Test your code here
result = merge_lists(
    "labs/lab08/exercise2/data/list1.txt",
    "labs/lab08/exercise2/data/list2.txt",
    "labs/lab08/exercise2/data/merged.txt"
)
print(f"Unique names: {result}")
