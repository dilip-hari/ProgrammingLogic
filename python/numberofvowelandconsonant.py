s=input()
vowel=0
gap=0
for i in range(0,len(s)):
    if s[i]=="a" or s[i]=="e" or s[i]=="i" or s[i]=="o" or s[i]=="u":
        vowel=vowel+1
    elif s[i]==" ":
        gap=gap+1
consonant=len(s)-vowel-gap
print(consonant)
print(vowel)
