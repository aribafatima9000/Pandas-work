num = int(input("Enter a number: "))
if str(num) == str(num)[::-1]:
    print("Palindrome ")
else:
    print("Not Palindrome ")





def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

num = int(input("Enter number: "))
print("Factorial:", factorial(num))



lst = [12, 45, 67, 89, 34, 67]
largest = max(lst)
lst.remove(largest)
second_largest = max(lst)
print("Second largest:", second_largest)



sentence = input("Enter a sentence: ").split()
freq = {}
for word in sentence:
    freq[word] = freq.get(word, 0) + 1
print("Word frequencies:", freq)




matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

transpose = [[0]*3 for _ in range(3)]

for i in range(3):
    for j in range(3):
        transpose[j][i] = matrix[i][j]

print("Transpose:")
for row in transpose:
    print(row)




num = int(input("Enter a number: "))
digits = str(num)
power = len(digits)
if sum(int(d)**power for d in digits) == num:
    print("Armstrong ")
else:
    print("Not Armstrong ")


lst = [2,3,4,4,5,6,2,7,8,9,5]
unique = []
for x in lst:
    if x not in unique:
        unique.append(x)
print("Without duplicates:", unique)



sentence = input("Enter sentence: ").split()
longest = max(sentence, key=len)
print("Longest word:", longest)




students = {"Ali":85,"Sara":92,"John":78,"Fatima":95,"Ahmed":88}
top3 = sorted(students.items(), key=lambda x: x[1], reverse=True)[:3]
print("Top 3 Students:", top3)



num = int(input("Enter number: "))
rev = int(str(num)[::-1])
print("Reverse:", rev)



lst = [2,3,4,5]
product = 1
for x in lst:
    product *= x
print("Product:", product)




s = input("Enter string: ")
unique = ""
for ch in s:
    if ch not in unique:
        unique += ch
print("Unique characters:", unique)



lst = [1,2,3,4,5]
if lst == sorted(lst):
    print("List sorted ascending")
elif lst == sorted(lst, reverse=True):
    print("List sorted descending")
else:
    print("Not sorted")





matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
n = len(matrix)
p_sum = s_sum = 0
for i in range(n):
    p_sum += matrix[i][i]
    s_sum += matrix[i][n-i-1]
print("Primary diagonal:", p_sum)
print("Secondary diagonal:", s_sum)



def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

lst = [2,3,4,5,6,7,11,15,17,20]
primes = [x for x in lst if is_prime(x)]
print("Primes:", primes)




num = int(input("Enter number: "))
print("Binary:", bin(num)[2:])




s = input("Enter string: ")
vowels = "aeiouAEIOU"
v, c = 0, 0
for ch in s:
    if ch.isalpha():
        if ch in vowels:
            v += 1
        else:
            c += 1
print("Vowels:", v, "Consonants:", c)





n = int(input("Enter n: "))
a, b = 0, 1
while a <= n:
    print(a, end=" ")
    a, b = b, a+b




lst = [1,2,3,4,5]
last = lst.pop()
lst.insert(0, last)
print("Rotated:", lst)




import string
s = input("Enter sentence: ").lower()
if set(string.ascii_owercase).issubset(set(s)):
    print("Pangram ")
else:
    print("Not Pangram ")
