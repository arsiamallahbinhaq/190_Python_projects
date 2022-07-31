from time import time
start = time()

#Python prgoram to create acronyms
word = input("Enter the word: ")

#word = "Development and Operations"
text = word.split()
a = " "
for i in text:
    a = a + str(i[0]).upper()
print(a)
print(text)

end = time()
execution_time = end - start
print("Execution Time : ", execution_time)