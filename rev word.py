a=input("Enter A String")
def rev(a):
    r=" ".join(sorted(a,reverse=True))
    print(r)
try:
    rev(a)
except:
    print("invalid input")
    
