def canonical_email(addr):
    '''Canonicalize a Gmail address.

    Gmail addresses may contain periods in the username which are ignored.
    Additionally, the username may contain a ``+`` followed by any arbitrary
    text which is ignored.

    Arguments:
        addr (str): The Gmail address.

    Returns:
        str:
            The cannonical email address.
    '''
    # Split the address into a user and host.
    # This raises a value error if there is not exactly one '@' symbol.
    (full_username, host) = addr.split('@')

    # The username may include one or more '+' symbols.
    # Everything after the first can be ignored.
    (username, *extras) = full_username.split('+')

    # The username may contain '.' symbols which are ignored.
    # We split the name at each '.' then recombine with '' as the separator.
    username_parts = username.split('.')
    username = ''.join(username_parts)

    # The canonical email address is simple:
    return f'{username}@{host}'
