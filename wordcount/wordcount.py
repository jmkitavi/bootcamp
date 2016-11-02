def words(text):
    text = text.replace('\t', ' ')
    text = text.replace('\n', ' ')
    tokens = text.split(' ')

    result = {}
    for token in tokens:
        if token not in ['', '\n', '\t']:
            if token not in result:
                if token.isdigit():
                    key = int(token)
                else:
                    key = token
                result.update({key: tokens.count(token)})
    return result