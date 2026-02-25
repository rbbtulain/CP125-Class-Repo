def get_student_courses(enrollments, student_id):
    """Return set of courses this student has completed."""
    completed = []
    for sid, course in enrollments:
        if sid == student_id and course not in completed:
            completed.append(course)
    return set(completed)
    
def find_missing_courses(completed_courses, required_courses):
    """Return set of required courses not yet completed."""
    missing = []
    for required in required_courses:
        if required not in completed_courses:
            missing.append(required)
    return set(missing)

def build_student_report(students, enrollments, required_courses):
    """Return sorted list of tuples (student_id, missing_count) for students with missing courses."""
    report = []
    for student_id in students:
        completed = get_student_courses(enrollments, student_id)
        missing = find_missing_courses(completed, required_courses)
        report.append((student_id, len(missing)))
    return sorted(report, key=lambda x: x[1], reverse=True)

def find_incomplete_students(enrollments, required_courses):
    """Find students who haven't completed all required courses."""
    incomplete = []
    students = set(sid for sid, _ in enrollments)
    for student_id in students:
        completed = get_student_courses(enrollments, student_id)
        missing = find_missing_courses(completed, required_courses)
        if missing:
            incomplete.append(student_id)
    return incomplete