ASCII_CHAR_124 = 124
ASCII_CHAR_42 = 42

s = "|*|*|*|*|*|*|*|**"
arrStart = [0,1]
arrEnd = [4,13]

# arrStart = [2]
# arrEnd = [6]

# def startWith()


def numbersOfItems(s,startIndices,endIndices):
    numOfRounds = 0
    countIfFirst = True
    while numOfRounds < len(startIndices): 
        newString = s[startIndices[numOfRounds] -1: endIndices[numOfRounds]+1]
        for letter in newString:
            if ord(letter) == ASCII_CHAR_42 and countIfFirst:
                print(letter)
                countIfFirst = False
                break
            countIfFirst=1
            # print(letter)
            # newString2 = newString2 + letter
            # if ord(letter) == ASCII_CHAR_124:
            #     print(f"here is start:  {letter}" )
            # if ord(letter) == ASCII_CHAR_42:
            #     newString = newString + letter
            #     print(f"you are inside astimate: {letter}")
            # print(newString2)
        print(startIndices[numOfRounds],endIndices[numOfRounds])
        numOfRounds+=1    
    quit()
    
numbersOfItems(s,arrStart,arrEnd)


# def numbersOfItems(s,startIndices,endIndices):
#     numOfRounds = 0
#     isInside = False
#     countSymbols = 0
#     countAllProducts = 0
#     productsNotClosed = 0
#     nextChar = 0
#     isExist = False
#     notExist = True
#     newString = s[startIndices[numOfRounds] : endIndices[numOfRounds]]
#     print(len(startIndices))
#     while numOfRounds < len(startIndices):
#         for letter in newString:
#             if ord(letter) == ASCII_CHAR_124:
#                 nextLetter = 1
#                 # print("here")
#                 # print(newString[nextLetter+1])
#                 # while letter == "|":
#                 i = 0
#                 while nextLetter < len(newString) or not isExist or letter != "|":
#                     nextLetter += 1
#                     countAllProducts+=1
#                     isExist = True
#                     break
#                     # if newString[nextLetter] == "|":
#                     #     isExist = True
#                     #     notExist = False
#                     #     i = 1
#                     # else:
#                     #     nextLetter += 1
                        
#                 if not isExist:
#                     print("no end for this one...")
#                     break;
#                 isInside = True
#                 nextLetter = 0
#             # if ord(letter) == ASCII_CHAR_42 and isInside:
#             #     print(letter)
                    
#             if ord(letter) == ASCII_CHAR_42 and not isInside:
#                     productsNotClosed+=1
                    
#             if ord(letter) == ASCII_CHAR_124 and not isInside:
#                 print(letter)
#         numOfRounds+=1
#         print(f"\ncount of products: {countAllProducts}")
#         # print(f"\ncount of product not closed: {productsNotClosed}")
#         countAllProducts = 0
#         productsNotClosed = 0
#     quit()
    
# numbersOfItems(s,arrStart,arrEnd)







                    # while countSymbols == 0:
                    #     while ord(letter) == ASCII_CHAR_124:
                    #         print(f"inside {letter}")
                    #         countAllProducts+=1
                    #     countSymbols = 1
                    # for item in letter:
                    #     if ord(letter) != 124:
                    #         print(item)
                    #         countAllProducts+=1
                    #     else:
                    #         countSymbols = 1
                # elif ord(letter) != 124 and countSymbols == 0:
                #     print(letter)
                #     countAllProducts+=1     
                
                
                
                
                
            #test    
            
            #      while countSymbols == 0:
            # for letter in newString:
            # while ord(letter) == ASCII_CHAR_124:
            #     print(f"inside {letter}")
            #     countAllProducts+=1
            #     countSymbols = 1
            #     for item in letter:
            #         if ord(letter) != 124:
            #             print(item)
            #             countAllProducts+=1
            #         else:
            #             countSymbols = 1
            #         elif ord(letter) != 124 and countSymbols == 0:
            #             print(letter)
            #             countAllProducts+=1     
    # while numOfRounds < len(startIndices):
        
        # for letter in newString:
            
        #     if ord(letter) == ASCII_CHAR_124:
        #         print(letter)
        #         isInside = True
                
        #     if ord(letter) == ASCII_CHAR_42 and isInside:
        #         print(letter)
                
        #     if ord(letter) == ASCII_CHAR_42 and not isInside:
        #         None
            
            # if ord(letter) == ASCII_CHAR_124 and not isInside:
            #     print(letter)
            
            # if ord(letter) == ASCII_CHAR_124:
            #     isInside = False
            #     print(letter, isInside)
            # else:
            #     isInside = True
            #     print(letter, isInside)
            
            # if isInside:
            #     countAllProducts+=1
            
            # if ord(letter) == ASCII_CHAR_124 and countSymbols == 0:
            #     print(newString[nextChar])
            #     nextChar+=1
            #     countSymbols = 1
            # if ord(letter) == ASCII_CHAR_124 and countSymbols == 1:
            #     if newString[nextChar] == newString[len(startIndices)]:
            #         print(newString[nextChar])
            #         nextChar +=1
            #         countSymbols = 0
            #     print(newString[nextChar])
            #     nextChar+=1
            #     countSymbols = 0
            #     print(f"{letter} start")
            #     nextLetter = 0
                # while nextLetter < len(newString):
                #     if newString[nextLetter] == "|":
                #         nextLetter+=1
                #         countSymbols = 1
                    # print(f"here you are {newString[nextLetter]}")
                    # nextLetter+=1
                # countSymbols = 1
                # while len(newString)-1:
                #     if nextLetter < len(newString):
                #         if newString[nextLetter] == "|" and testCountSymbol == 0:
                #             nextLetter+=1
                #             testCountSymbol = 1
                #             print(newString[nextLetter] )
                #             if newString[nextLetter] == "*" and testCountSymbol ==1:
                #                 print(newString[nextLetter])
                #                 countAllProducts+=1
                #             else:
                #                 break
                #         nextLetter +=1
                #     else:
                #         break
                # countSymbols = 1
            # elif(ord(letter) == 124 and countSymbols != 0):
            #     countSymbols = 0
            #     print(f"{letter} end")
        # numOfRounds+=1
        # print(f"next cell. \n" )