##Linear search

def linear_search(n,a,key):
    f = 0
    for i in range (n):
        if (a[i] == key):
            f = 1
            pos = i+1
            break
    if f == 1 :
        print("Number is on position no.",pos)
    else:
        print("number not found")

n = int(input("Enter length of the list: "))
a = []
for i in range(n):
    value = int(input("Enter values in list :"))
    a.append(value)

key = int(input("Enter number to search: "))

linear_search(n,a,key)
