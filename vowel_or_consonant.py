i = input()
ip = i.lower()
if(ip.isalpha()):
    if(ip == 'a' or ip == 'e' or ip == 'i' or ip == 'o' or ip == 'u'):
        print("vowel")
    else:
        print("consonant")
else:
    print("invalid")
