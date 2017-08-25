def total_seconds(dt):
    # Keep backward compatibility with Python 2.6 which doesn't have
    # this method
    if hasattr(dt, 'total_seconds'):
        return dt.total_seconds()
    else:
        return (dt.microseconds + 0.0 + (dt.seconds + dt.days * 24 * 3600) * 10 ** 6) / 10 ** 6