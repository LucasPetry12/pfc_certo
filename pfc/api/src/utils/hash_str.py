import hashlib


def hash_str(string):

    text = string.strip()
    text = hashlib.sha256(str(string).encode('utf-8'))
    text = text.hexdigest()

    return text


def compare(string, pass_hash):
    compare = hash_str(string)
    if compare == pass_hash:
        return 'É igual'
    else:
        return 'Senha errada'
