n=int(input("enter the numbers of words needed:"))
words=[]
print("enter the words:")
for i in range(0,n):
    y=str(input())
    words.append(y)
print("the listed words are",words)
words.sort()
print("the sorted list is :",words)
    
