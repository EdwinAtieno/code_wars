word= input("Please input seven characters\n ")
Fletter= "#"

while Fletter not in word[0]:
   if len(word) == 7:
       character = input(" enter two character to search\n")
       if len(character) == 2:
           word.find(character)
           if character in word:
                replicate = input(" enter two character to replace\n")
                if len(replicate) == 2:
                    word= word.replace(character, replicate)
                    print(word)
                    if word[0] == "#":
                        break
           else:
                print(word)
       else:
           print(word)
       continue
   else:
       print("you didn't put seven characters, start again")
       break


# to create loop which will stop when one inputs # as the first letter in a string