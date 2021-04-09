import translators as ts

#v0.1
#I've been testing this out for a while but it seems okay for now
#Uses the translators library with Google Translation API
#Should be okay for regular usage

print("Welcome to the CLI translator")
i = 0
while i == 0:
    exit = 0
    print("Enter your input language (2 Character Abbreviation or Auto): ")
    inputlang = input()
    print()
    print("Enter your input string: ")
    entry = input()
    print()
    print("Enter output language (2 Character Abbreviation): ")
    outputlang = input()
    print()
    print("Output: " + ts.google(entry, from_language = inputlang,to_language = outputlang))
    print()
    print("Are you finished using the translator tool? Enter Y/N: ")
    x = input()
    x = x.lower()
    while exit == 0:
        if x == 'y':
            i = 1
            exit = 1
        elif x == 'n':
            i = 0
            exit = 1
        else:
            "Try again"
print()
print("Thanks for using the quick translator tool.")
print("Goodbye")
