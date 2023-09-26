text=input()
textlist=list(text)
n=len(textlist)
finaltext=''
i=1
while i<n:
    k=-1
    for j in range(i-1,-1,-1):
        if textlist[j]==textlist[i]:
            k=j
    if k!=-1:
        if i>len(finaltext):
            finaltext=textlist[0:i]
        for t in range(k+1):
            del textlist[0]
        n=n-k-1
    i=i-k
finaltext=''.join(finaltext)
print(finaltext)