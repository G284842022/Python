from pathlib import Path


def get_content(src):
    with open(src, encoding='utf-8') as fsrc:
        content = fsrc.readlines()
    fsrc.close()
    return content


content = get_content('angoubun.txt')


def get_most_frequent_char(content):
    frequency = dict.fromkeys((chr(i) for i in range(ord('a'), ord('z')+1)), 0)
    for i in content:
        for j in i:
            if j in frequency:
                frequency[j] += 1
    print(frequency)
    return max((v, k) for k, v in frequency.items())[1]


def decrypt(content, char):
    simbols = {" ": " ", ".": ".", ",": ",", "?": "?", '“': '"', "—": "-", ";": ";", "é": "e"}
    key = 20
    result = []
    for i in content:
        line = []
        for j in i:
            if 'a' <= j <= 'z':
                print(j, end="")
                line.append(chr( (ord(j) + 20)%26 + 97 )) # chr(( ord(j)) % 26 + ord('a'))
            elif j.isdecimal():
                line.append(j)
            elif j in simbols:
                line.append(simbols.get(j))
        result.append(line)
    return result
        

f = open('decrypt.txt', 'w')
for i in decrypt(content, get_most_frequent_char(content)):
    f.write(''.join(i))
    f.write( '\n')
# print( f.write(decrypt(content, get_most_frequent_char(content))) )
# print(decrypt(content, get_most_frequent_char(content)))


