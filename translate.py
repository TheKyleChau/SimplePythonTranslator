import translators as ts

print("Welcome to the CLI translator")
i = 0
while i == 0:
    exit = 0
    print("Enter your input language (2 Character Abbreviation or Auto): ")
    inputlang = input()
    print("Enter your input string: ")
    entry = input()
    print("Enter output language (2 Character Abbreviation): ")
    outputlang = input()
    print("Output: " + ts.google(entry, from_language = inputlang,to_language = outputlang))
    print("Are you finished using the translator tool? Enter Y/N: ")
    x = input()
    x.lower()
    while exit == 0:
        if x == 'y':
            i = 1
            exit = 1
        elif x == 'n':
            i = 0
            exit = 1
        else:
            "Try again"
print("Thanks for using the quick translator tool.")
