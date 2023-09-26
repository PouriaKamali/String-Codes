text = input('Please, input a string:')
numRows = input('Please, input the Number of Rows:')
textlist = list(text)
textline = []
def line(r):
    for i in r:
        textline.append(textlist[i])
    return textline
for j in range(int(numRows)):
    Sequence = [*range(j,len(text),2*(int(numRows)-1))] + [*range(2*int(numRows)-j-2,len(text),2*(int(numRows)-1))]
    Sequence = list(set(Sequence))
    Sequence.sort()
#    print(Sequence)
    line(Sequence)
FinalText = ''.join(textline)
print('Final text after Zigzag Conversion is: ' + FinalText)