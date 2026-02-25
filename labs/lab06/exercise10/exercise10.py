def get_unique_attendees(attendance_logs):
    """Extract list of all unique attendee IDs."""
    unique_attendees = []
    for attendee_id, _ in attendance_logs:
        if attendee_id not in unique_attendees:
            unique_attendees.append(attendee_id)
    return unique_attendees

def count_unique_events(attendance_logs, attendee_id):
    """Count how many unique events this attendee attended."""
    events = []
    for att_id, event_name in attendance_logs:
        if att_id == attendee_id and event_name not in events:
            events.append(event_name)
    return len(events)

def filter_by_threshold(attendees, attendance_logs, min_events):
    """Return sorted list of attendees who attended >= min_events."""
    qualified = []
    for attendee_id in attendees:
        if count_unique_events(attendance_logs, attendee_id) >= min_events:
            qualified.append(attendee_id)
    qualified.sort()
    return qualified

def find_frequent_attendees(attendance_logs, min_events):
    """Find attendees who attended at least min_events unique events."""
    all_attendees = get_unique_attendees(attendance_logs)
    return filter_by_threshold(all_attendees, attendance_logs, min_events)
