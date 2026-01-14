
def clean_sessions(pool, sessions, dead_servers):
    """
    Verify dead servers in pool, remove their sessions, and return sorted list.
    """
    alive_servers = set(pool) - set(dead_servers)
    cleaned_sessions = [s for s in sessions if s[0] in alive_servers]
    return sorted(cleaned_sessions)


# Test
pool = ("srv-A", "srv-B", "srv-C", "srv-D")
sessions = [("srv-B", "cli-1"), ("srv-A", "cli-2"), ("srv-C", "cli-3"),
            ("srv-B", "cli-4"), ("srv-D", "cli-5")]
dead = ["srv-B", "srv-D"]

result = clean_sessions(pool, sessions, dead)
print(f"Cleaned Sessions: {result}")
# Expected: [('srv-A', 'cli-2'), ('srv-C', 'cli-3')]
