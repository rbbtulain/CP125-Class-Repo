def synchronize_databases(legacy_list, modern_set, blacklist):

    legacy_set = set()

    for record_id, email in legacy_list:
        if email not in blacklist:
            legacy_set.add(record_id)
    lost_set = legacy_set - modern_set
    ghost_set = modern_set - legacy_set




    return lost_set, ghost_set