from pathlib import Path


def get_content(src):
    with open(src, encoding='utf-8') as fsrc:
        content = fsrc.readlines()
    fsrc.close()
    return content

content = get_content('angoubun_shuffle.txt')


def analyze_chars_frequency(content):
    frequency = dict.fromkeys((chr(i) for i in range(ord('a'), ord('z')+1)), 0)
    for i in content:
        for j in i:
            if j in frequency:
                frequency[j] += 1
    print(frequency)
    frequency


def decrypt(content, freqency):
    freq_index = ["e","t","a","o","i","h","n","s","r","d","l","u","m","w","c","y","f","g","p","b","v","k","x","j","q","z"] 
    simbols = {" ": " ", ".": ".", ",": ",", "?": "?", '“': '"', "”": '"', "—": "-", ";": ";", "é": "e"}
    
    result = []
    for i in content:
        line = []
        for j in i:
            if 'a' <= j <= 'z':
                line.append(chr( ord("a") + (ord(j) - ord("a") + key)%26 ))
            elif j.isdecimal():
                line.append(j)
            elif j in simbols:
                line.append(simbols.get(j))
        result.append(line)
    return result
        

f = open('decrypt.txt', 'w')
# for i in decrypt(content, get_most_frequent_char(content)):
#     f.write(''.join(i))
#     f.write( '\n')