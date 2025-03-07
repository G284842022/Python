def mix(str1, str2):
    for i in range(len(str1)):
     print(str1[i]+str2[len(str2)-1-i], end="")

mix("Cmue", "rtpo")