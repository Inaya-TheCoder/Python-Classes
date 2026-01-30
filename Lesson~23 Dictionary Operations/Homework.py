a = {"Alice's age": 10,"Sarah's age": 12,"John's age": 10,"Mike's age": 13,"Emma's age": 10}
print ("The original dictionary is : "+ str(a))
b = int(input("Enter a specific age from the given Dictionary:"))

result = 0
for i in a:
    if (a[i] == b):
        result = result+1
print ("Frequency of",b,"is :",result)
