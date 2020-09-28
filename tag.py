from dictionaryEsp import dictionary

input = input()
words = input.split()
paragraph = ""
translateWords = []
listWords = list(dictionary.keys())

for word in words:

    if word[-1]==".":
        translateWords.append((word[:-1]).lower())
    elif word[-1]==",":
        translateWords.append((word[:-1]).lower())
    else:
        translateWords.append(word.lower())

    if translateWords[-1]== "«":
        translateWords.pop()
    elif translateWords[-1]== "»":
        translateWords.pop()
    elif translateWords[-1]== ":":
        translateWords.pop()
    elif translateWords[-1]== "1":
        translateWords.pop()
    elif translateWords[-1]== "2":
        translateWords.pop()
    elif translateWords[-1]== "?":
        translateWords.pop()

print(" ")
print("Translate Words")
print(translateWords)

differenceWords = list(set(translateWords) - set(listWords))

print(" ")
print("difference Words")
print(differenceWords)

print(" ")
print("Words translate")
for translation in differenceWords:
    print("\""+translation+"\" : [\"untranslated\"],")

print(" ")
print(" ")
for word in words:
    if (word == ":" or word == "«" or word == "»" or word == "?" or word == "2" or word == "1"):
        paragraph += "<span>"+word+"</span> "
    elif (word[-1] == "." or word[-1] == ","):
        if word[:-1] == "»":
            paragraph += "<span>"+word+"</span> "
        elif word[:-1] == "1":
            paragraph += "<span>"+word+"</span> "
        elif word[:-1] == "2":
            paragraph += "<span>"+word+"</span> "
        else:
            paragraph += "<span class=\"tooltips\">"+word[:-1]+"<span><%=  dictionary[\""+(word[:-1]).lower()+"\"][0] %></span></span>"+word[-1]+" "
    else:
        paragraph += "<span class=\"tooltips\">"+word+"<span><%=  dictionary[\""+word.lower()+"\"][0] %></span></span> "

print(paragraph)
