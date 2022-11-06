def encode(text: str, key: str) -> str:
    nt = ''
    for i in range(len(text)):
        move = ord(key[i % len(key)]) - 96
        nlint = (ord(text[i]) - 97 + move) % 26 + 97
        nlstr = chr(nlint)
        nt += nlstr
    return nt


def decode(text: str, key: str) -> str:
    nt = ''
    for i in range(len(text)):
        move = ord(key[i % len(key)]) - 96
        nlint = (ord(text[i]) - 97 - move) % 26 + 97
        nlstr = chr(nlint)
        nt += nlstr
    return nt


print(encode('aldehyd', 'kvet'))
print(decode('lhiysui', 'kvet'))
