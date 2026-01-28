def audit_blocklists(list_a, list_b, list_c):
    universal = list_a & list_b & list_c
    redundant = (list_a & list_b | list_b & list_c | list_a & list_c)
    list_a_unique = list_a - (list_b | list_c)

    return universal, redundant, list_a_unique

# Example usage:
list_a = {"malware.exe", "virus.zip"}
list_b = {"spyware.dll", "malware.exe"}
list_c = {"adware.bat", "malware.exe"}
universal, redundant, list_a_unique = audit_blocklists(list_a, list_b, list_c)
print(f"Universal threats: {universal}")