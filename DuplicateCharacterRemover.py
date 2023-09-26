text=input()
textlist=list(text)
n=len(textlist)
i=1
while i<n:
    k=0
    for j in range(i-1,-1,-1):
        if textlist[j]==textlist[i]:
            k=1
    if k==1:
        del textlist[i]
        n=n-1
    else:
        i=i+1
Textlist=''.join(textlist)
print(Textlist)