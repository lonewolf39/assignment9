# Q.1- Name and handle the exception
try:
    a=3
    if a<4:
        a=a/(a-3)
        print(a)
except ZeroDivisionError:
    print("it is ZeroDivisionError ")

# Q.2- Name and handle the exception
l=[1,2,3]
try:
    print(l[3])
except:
    print("It is IndexError.")

# Q.3- Determine the output
print("""An exception
'after this error occur'""")

# Q.4- Determine the output
print("""Output:
-5.0
a/b result in 0"""

# Q.5- Write example programs of the given errors
try:
    import xyz
except ImportError:
    print("It is import error because no such module is present")
try:
    z=int(input("Enter number"))
except ValueError:
    print("Please enter  number not string")
try:
    l=[1,2,3]
    i=int(input("Enter the index"))
    print(l[i])
except IndexError:
    print("Invalid index")
