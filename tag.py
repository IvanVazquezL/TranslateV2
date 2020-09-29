from dictionaryEsp import dictionary

input = input()
words = input.split()
paragraph = ""
translateWords = []
listWords = list(dictionary.keys())

print(" ")
print("Words")
print(words)

for word in words:

        if word[-1]==".":
            translateWords.append((word[:-1]).lower())
        elif word[0]=="-":
            if word[-1]=="…":
                translateWords.append((word[1:-1]).lower())
            else:
                translateWords.append((word[1:]).lower())
        elif word[0]=="(":
            translateWords.append((word[1:]).lower())
        elif word[-1]==")":
            translateWords.append((word[:-1]).lower())
        elif word.find("…") > -1:
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
        elif translateWords[-1]== "!":
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
print("Join words")

for index,check in enumerate(translateWords):
    if index == (len(translateWords)-1):
        pass
    else:
        if check=="j’ai":
            if translateWords[index+1] == "ainsi":
                words.insert(index,words[index]+" "+words[index+1])
                del words[(index+1):(index+3)]

                translateWords.insert(index,translateWords[index]+" "+translateWords[index+1])
                del translateWords[(index+1):(index+3)]
                print(words)
            elif translateWords[index+1] == "sauté":
                words.insert(index,words[index]+" "+words[index+1])
                del words[(index+1):(index+3)]

                translateWords.insert(index,translateWords[index]+" "+translateWords[index+1])
                del translateWords[(index+1):(index+3)]
                print(words)
            elif translateWords[index+1] == "vu":
                words.insert(index,words[index]+" "+words[index+1])
                del words[(index+1):(index+3)]

                translateWords.insert(index,translateWords[index]+" "+translateWords[index+1])
                del translateWords[(index+1):(index+3)]
                print(words)

        elif check== "quelque":
            if translateWords[index+1] == "chose":
                words.insert(index,words[index]+" "+words[index+1])
                del words[(index+1):(index+3)]

                translateWords.insert(index,translateWords[index]+" "+translateWords[index+1])
                del translateWords[(index+1):(index+3)]
                print(words)

        elif check== "petit":
            if translateWords[index+1] == "bonhomme":
                words.insert(index,words[index]+" "+words[index+1])
                del words[(index+1):(index+3)]

                translateWords.insert(index,translateWords[index]+" "+translateWords[index+1])
                del translateWords[(index+1):(index+3)]
                print(words)
        elif check== "bien":
            if translateWords[index+1] == "sûr":
                words.insert(index,words[index]+" "+words[index+1])
                del words[(index+1):(index+3)]

                translateWords.insert(index,translateWords[index]+" "+translateWords[index+1])
                del translateWords[(index+1):(index+3)]
                print(words)
        elif check== "j’avais":
            if translateWords[index+1] == "été":
                words.insert(index,words[index]+" "+words[index+1])
                del words[(index+1):(index+3)]

                translateWords.insert(index,translateWords[index]+" "+translateWords[index+1])
                del translateWords[(index+1):(index+3)]
                print(words)
        elif check== "grandes":
            if translateWords[index+1] == "personnes":
                words.insert(index,words[index]+" "+words[index+1])
                del words[(index+1):(index+3)]

                translateWords.insert(index,translateWords[index]+" "+translateWords[index+1])
                del translateWords[(index+1):(index+3)]
                print(words)
        elif check== "qu’est-ce":
            if translateWords[index+1] == "que":
                words.insert(index,words[index]+" "+words[index+1])
                del words[(index+1):(index+3)]

                translateWords.insert(index,translateWords[index]+" "+translateWords[index+1])
                del translateWords[(index+1):(index+3)]
                print(words)

        elif check=="avec":
            if translateWords[index+1] == "moi":
                words.insert(index,words[index]+" "+words[index+1])
                del words[(index+1):(index+3)]

                translateWords.insert(index,translateWords[index]+" "+translateWords[index+1])
                del translateWords[(index+1):(index+3)]
                print(words)
        elif check=="plus":
            if translateWords[index+1] == "tard":
                words.insert(index,words[index]+" "+words[index+1])
                del words[(index+1):(index+3)]

                translateWords.insert(index,translateWords[index]+" "+translateWords[index+1])
                del translateWords[(index+1):(index+3)]
                print(words)
        elif check=="tout":
            if translateWords[index+1] == "seul":
                words.insert(index,words[index]+" "+words[index+1])
                del words[(index+1):(index+3)]

                translateWords.insert(index,translateWords[index]+" "+translateWords[index+1])
                del translateWords[(index+1):(index+3)]
                print(words)
        elif check=="drôle":
            if translateWords[index+1] == "de":
                words.insert(index,words[index]+" "+words[index+1])
                del words[(index+1):(index+3)]

                translateWords.insert(index,translateWords[index]+" "+translateWords[index+1])
                del translateWords[(index+1):(index+3)]
                print(words)
        elif check=="petit":
            if translateWords[index+1] == "prince":
                words.insert(index,words[index]+" "+words[index+1])
                del words[(index+1):(index+3)]

                translateWords.insert(index,translateWords[index]+" "+translateWords[index+1])
                del translateWords[(index+1):(index+3)]
                print(words)
        elif check=="il":
            if translateWords[index+1] == "y":
                if translateWords[index+2] == "a":
                    words.insert(index,words[index]+" "+words[index+1]+" "+words[index+2])
                    del words[(index+1):(index+4)]

                    translateWords.insert(index,translateWords[index]+" "+translateWords[index+1]+" "+translateWords[index+2])
                    del translateWords[(index+1):(index+4)]
                    print(words)
        elif check=="lever":
            if translateWords[index+1] == "du":
                if translateWords[index+2] == "jour":
                    words.insert(index,words[index]+" "+words[index+1]+" "+words[index+2])
                    del words[(index+1):(index+4)]

                    translateWords.insert(index,translateWords[index]+" "+translateWords[index+1]+" "+translateWords[index+2])
                    del translateWords[(index+1):(index+4)]
                    print(words)
        elif check=="s’il":
            if translateWords[index+1] == "vous":
                if translateWords[index+2] == "plaît":
                    words.insert(index,words[index]+" "+words[index+1]+" "+words[index+2])
                    del words[(index+1):(index+4)]

                    translateWords.insert(index,translateWords[index]+" "+translateWords[index+1]+" "+translateWords[index+2])
                    del translateWords[(index+1):(index+4)]
                    print(words)


print(" ")
print(" ")
for word in words:
    if (word == ":" or word == "«" or word == "»" or word == "?" or word == "!" or word == "2" or word == "1"):
        paragraph += "<span>"+word+"</span> "
    elif word[0]=="-":
        if word[-1]=="." or word[-1]=="…":
            paragraph += "—<span class=\"tooltips\">"+word[1:-1]+"<span><%=  dictionary[\""+(word[1:-1]).lower()+"\"][0] %></span></span>"+word[-1]+" "
        else:
            paragraph += "—<span class=\"tooltips\">"+word[1:]+"<span><%=  dictionary[\""+(word[1:]).lower()+"\"][0] %></span></span> "
    elif word.find("…")> -1:
        paragraph += "<span class=\"tooltips\">"+word+"<span><%=  dictionary[\""+(word[:-1]).lower()+"\"][0] %></span></span> "
    elif word[0]=="(":
        paragraph += "(<span class=\"tooltips\">"+word[1:]+"<span><%=  dictionary[\""+(word[1:]).lower()+"\"][0] %></span></span> "
    elif word[-1]==")":
        paragraph += "<span class=\"tooltips\">"+word[:-1]+"<span><%=  dictionary[\""+(word[:-1]).lower()+"\"][0] %></span></span>) "
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
