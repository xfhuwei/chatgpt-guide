def remaining_seats(capacity, groups):
    values = [capacity, *groups]
    if any(type(v) is not int or v < 0 for v in values):
        raise ValueError('容量和人数必须是非负整数')
    return capacity - sum(groups)
