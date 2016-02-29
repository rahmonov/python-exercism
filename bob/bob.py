def hey(message):
    message = message.strip()

    if message.isupper():
        return 'Whoa, chill out!'
    if message.endswith('?'):
        return 'Sure.'
    if not message:
        return 'Fine. Be that way!'

    return 'Whatever.'
