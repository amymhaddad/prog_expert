def new_range(start, stop, step):
    current = start

    while current != stop:

        if (
            (step > 0 and current >= stop)
            or (start < 0 and step > 0)
            or (start >= 0 and step < 0)
        ):
            break

        current += step
        yield current - step
