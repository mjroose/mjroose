def get_full_name(first, middle, last):
    if first is '' or last is '':
        return ''
    elif middle is '':
        return '{} {}'.format(first, last)
    return '{} {} {}'.format(first, middle, last)