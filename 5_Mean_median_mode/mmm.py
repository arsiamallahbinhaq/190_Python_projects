# list can be modified 

#input list
lst = []
n = int(input("Enter number of elements : "))
for i in range (0,n):
    ele = int(input())
    lst.append(ele)
print("Here the list:", lst)

# Mean
#lst = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
mean = sum(lst)/len(lst)
print("Mean is: ", mean)

# Median
lst.sort()
if len(lst) % 2 == 0:
    m1 = lst[len(lst)//2]
    m2 = lst[len(lst)//2 - 1]
    median = (m1 + m2) / 2
else :
    median = lst[len(lst)//2]
print ("Median is ", median)

# Mode
frequency = {}
for i in lst:
    frequency.setdefault(i,0)
    frequency[i] +=1

frequent = max(frequency.values())
for i, j in frequency.items():
    if j == frequent:
        mode = i
print("Mode is ", mode)