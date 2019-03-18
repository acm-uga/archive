def run_length_encoding(text):
    assert 1 < len(text)

    char = text[0]
    count = 1
    output = ''

    for c in text[1:]:
        if c == char:
            count += 1
        else:
            output = f'{output}{char}{str(count)}'
            count = 1
            char = c

    output = f'{output}{char}{str(count)}'
    count = 1
    char = c

    return output