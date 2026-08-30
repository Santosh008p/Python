#1. Write a program to find the length of a string without using an inbuilt function.
name=input("Enter your name:")
count=0
for i in name:
    count+=1
print(f'The total character in your name is {count}')

#2. Write a program to count the number of vowels and consonants in a string.
str=input("Enter a string")
vowels="aeiouAEIOU"
vowel_count=0
consonants_count=0

for i in str:
    if i in vowels:
        vowel_count+=1
    else:
        consonants_count+=1

print(f'the number of vowels in the given string is {vowel_count} and the number of consonants in the giveb string is {consonants_count}')

# 3. Write a program to count the number of words in a sentence.
 
sentence=input("Enter your sentence").strip()
space=0
for i in sentence:
    if i==' ' and i+1 !=' ' and i-1 !=' ':
        space+=1
word_count=space+1
print(f'the number of words in your sentence is: {word_count}')##this will work but it will not give the correct answer if there are more than one spaces between the words

sentence=input().strip()
word_count=0
for i in range(len(sentence)):
    if sentence[i]!=' ' and (i==0 or sentence[i-1]==' '):
        word_count+=1

print(f"The number of words in your sentence is: {word_count}")

#4. Write a program to reverse a string.
str=input("Enter your name")
reversed_str=''
for i in range(len(str)-1,-1,-1):
    reversed_str= reversed_str +str[i]
print(reversed_str)

#5.Write a program to check whether a string is a palindrome.
word=input("Enter a word")
reversed=''
for i in range(len(word)-1,-1,-1):
    reversed+=word[i]
if reversed==word:
    print("It's a palindrome word")
else:
    print('It is not a palindrome word')

#6. Write a program to convert a string to uppercase and lowercase without inbuilt case functions.
text=input("Enter a string:")
new_str=''
for ch in text:
    if 'a'<=ch<='z':
        new_str+=chr(ord(ch)-32)
    elif 'A'<=ch<='Z':
        new_str+=chr(ord(ch)+32)
    else:
        new_str+=ch
print(new_str)


#7. Write a program to count the frequency of each character in a string.
text=input("Enter a string:")
for ch in  set(text):
    print(ch, '=',text.count(ch))

#8. Write a program to remove all spaces from a string.
sentence=input("Enter a string:")
result=''
for ch in sentence:
    if ch!=' ':
        result+=ch
print(result)

#9. Write a program to check whether two strings are anagrams of each other.
str1,str2=input("Enter two strings").split()
anagram=True
if len(str1)!=len(str2):
    anagram=False
else:
    for ch in str1:
        if ch not in str2 or str1.count(ch) != str2.count(ch):
            anagram=False
            break
if(anagram):
    print("Anagrams")
else:
    print("Not Anagrams")

#10. Write a program to find the first non-repeating character in a string.
text=input("Enter a string:")
for ch in text:
    if text.count(ch)==1:
        print(ch)
        break

#11. Write a program to replace all occurrences of a character with another character in a string.
    
    
text=input("Enter a Word:")
old=input("enter the character you want to  replace")
new=input('Enter the replacement character')
result=''
for ch in  text:

    if ch==old:
        result+=new
    else:
        result+=ch
        
print(result)

# 12. Write a program to toggle the case of each character in a string.

#Already Done