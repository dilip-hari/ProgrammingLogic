s=input()
count=0
for i in range(0,len(s)//2):
    if s[i]!=s[len(s)-1-i]:
        count=count+1
if count>0:
    print("not palindrome")
else:
    print("palindrome")
