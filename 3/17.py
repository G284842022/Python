from pathlib import Path


def get_content(src):
    with open(src, encoding='utf-8') as fsrc:
        content = fsrc.readlines()
    fsrc.close()
    return content

content = get_content('angoubun_shuffle.txt')


def analyze_chars_frequency(content):
    frequency = {chr(i): 0 for i in range(ord('a'), ord('z')+1)}
    for i in content:
        for j in i:
            if j in frequency:
                frequency[j] += 1
    return sorted(frequency, key=frequency.get, reverse=True)


def decrypt(content, freqency):
    freq_index = ["e","t","a","o","i","h","n","s","r","d","l","u","m","w","c","y","f","g","p","b","v","k","x","j","q","z"]
    l = {a: b for a, b in zip(freqency, freq_index)}
    simbols = {" ": " ", ".": ".", ",": ",", "?": "?", '“': '"', "”": '"', "—": "-", ";": ";", "é": "e"}
    result = []

    for i in content:
        line = []
        for j in i:
            if 'a' <= j <= 'z':
                line.append(l[j])
            elif j.isdecimal():
                line.append(j)
            elif j in simbols:
                line.append(simbols.get(j))
        result.append(line)
    return result
        

f = open('decrypt.txt', 'w')
for i in decrypt(content, analyze_chars_frequency(content)):
   f.write(''.join(i))
   f.write( '\n')