user={
    "name": "Santosh",
    "age": 23,
    "is_loggedIn":True

}
user["name"]="santosh parajuli"
print(user["name"])
print(user.get("age"))
print(user.get("birthdate","9 march 2003"))

phone=input("Enter your phone number: ")
digits={
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"Seven",
    "8":"Eight",
    "9":"Nine"
}
output=""
for ch in phone:
    output+=digits.get(ch,"!") + " "
print(output)

messege=input(">")
words=messege.split(' ')
emojis={
   ":)":"😊",
   ":()":"😔"
}

output=""
for word in words:
   output+= emojis.get(word,word) + " "
print(output)