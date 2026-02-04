"""
Question : b) Write a Python program to remove the nth index character from a non-
empty string.
"""

word=input("Enter the string - ")
first=word[0]
reesult=first
for i in range(1,len(word)):
    current=word[i]
    if current==first:
        reesult+="$"
    else:
        reesult+=current
print(reesult)