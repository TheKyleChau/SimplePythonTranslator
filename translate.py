import translators as ts

#CLI-Version
#v0.2-alpha
#I've been testing this out for a while but it seems okay for now
#Uses the translators library with Google Translation API
#Should be okay for regular usage
#Adding usage for multiple translation APIs

print("Welcome to the CLI translator")
i = 0
translator = ''
while i == 0:
    valid = 0
    exit = 0
    while valid == 0:
        print("Enter translator (Google, Yandex, Bing)")
        translator = input()
        translator = translator.lower()
        if translator == 'google':
            valid = 1
        elif translator == 'yandex':
            valid = 1
        elif translator == 'bing':
            valid = 1
        else:
            print("Translator not valid.")
    print("Enter your input language (2 Character Abbreviation or Auto): ")
    inputlang = input()
    print()
    print("Enter your input string: ")
    entry = input()
    print()
    print("Enter output language (2 Character Abbreviation): ")
    outputlang = input()
    print()
    if translator == 'google':
        print("Output: " + ts.google(entry, from_language = inputlang,to_language = outputlang))
    if translator == 'bing':
        print("Output: " + ts.bing(entry, from_language = inputlang,to_language = outputlang))
    if translator == 'yandex':
        print("Output: " + ts.yandex(entry, from_language = inputlang,to_language = outputlang))
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
