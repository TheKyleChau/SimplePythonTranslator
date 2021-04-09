import translators as ts

#v0.1-alpha
#File translator format
#Line 1: Input language
#Line 2: Input string
#Line 3: Output language

inputlang = input()
entry = input()
outputlang = input()
print("Output: " + ts.google(entry, from_language = inputlang,to_language = outputlang))
print()
print("Thanks for using the quick translator tool.")
print("Goodbye")
