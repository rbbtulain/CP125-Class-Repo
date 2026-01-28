def manage_roster(enrolled, drop_requests, waitlist):


    for name in drop_requests:
        if name in enrolled:
            enrolled.remove(name)

    if len(enrolled) < 5:

        while len(enrolled) < 7:
            if len(waitlist) > 0:
                student = waitlist.pop()
                enrolled.add(student)
            else:
                break

    return len(enrolled)
