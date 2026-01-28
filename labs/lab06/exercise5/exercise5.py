def audit_zero_trust(baseline_set, current_log_list):

   authorized_set = set()


   current_set = set(current_log_list)


   for user_id in current_set:
      if user_id in baseline_set:
         authorized_set.add(user_id)

   alerts = current_set - baseline_set

   inactive = baseline_set - current_set

   return authorized_set, alerts, inactive
