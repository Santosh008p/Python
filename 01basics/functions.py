def greet_user():
    print("Hello Santosh")
    print("Welcome to programming World!")


print("Start")
greet_user()
print("Finished")

def greet_User(first_name, last_name):
    print(f'hello {first_name} {last_name}')


greet_User('santosh', 'parajuli')
greet_User(last_name='parajuli', first_name='santosh') #Keyword Argument


###return statement
def square(number):
    return number*number


print(square(3))

def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "😊",
        ":()": "😔"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output
    

    
    

messege=input(">")
print(emoji_converter(messege))