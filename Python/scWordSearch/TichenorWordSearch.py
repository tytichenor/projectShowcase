#initializations
masterList=[]
howManyFound=0

######READ IN TEXT FILE
with open('Book1.csv','r') as file:
    for line in file.readlines():
        currentlist=line.strip().split(",")
        masterList.append(currentlist)

def checkForGoodData():
    length = len(masterList[0])
    for l in masterList:
        if length != len(l):
            print('Bad data - Check word search')
            print("")
            break
    else:
        print("This is good data!")
        print("")

        #change the second parameters to look for any word
        mainSearch(masterList,'BINARY')
        mainSearch(masterList,'COMPUTERSCIENCE')
        mainSearch(masterList,'DECIMAL')
        mainSearch(masterList,'HEXADECIMAL')
        mainSearch(masterList,'JUPYTER')
        mainSearch(masterList,'MATPLOTLIB')
        mainSearch(masterList,'NOTEBOOK')
        mainSearch(masterList,'OCTAL')
        mainSearch(masterList,'PANDAS')
        mainSearch(masterList,'POWERSHELL')
        showHowManyFound()



def mainSearch(lettersList,wordToFind):
    global howManyFound
    firstLetter=wordToFind[0]
    ################CREDIT - HELP FROM BLAKE#################
    for i in range(len(lettersList)):
        for j in range(len(lettersList[i])):
            # if first Letter is in the list[i] in the [j] index of that specific list, then...
            if firstLetter == lettersList[i][j]:

                # call the left to right search -sending the parameters
                tryVar=leftToRight(i,j,wordToFind)
                if tryVar is not None:
                    # the +1 is because of the indexes starting at zero 
                    print(f'{wordToFind} has been found in row {i+1} and column {j+1}. ---- Look to the right.')
                    howManyFound+=1
                elif rightToLeft(i,j,wordToFind) is not None:
                    print(f'{wordToFind} has been found in row {i+1} and column {j+1}. ---- Look to the left.')
                    howManyFound+=1
                elif downLook(i,j,wordToFind) is not None:
                    print(f'{wordToFind} has been found in row {i+1} and column {j+1}. ---- Look down.')
                    howManyFound+=1
                elif upLook(i,j,wordToFind) is not None:
                    print(f'{wordToFind} has been found in row {i+1} and column {j+1}. ---- Look up.')  
                    howManyFound+=1              
                elif diagonal1(i,j,wordToFind) is not None:
                    print(f'{wordToFind} has been found in row {i+1} and column {j+1}. ---- Look to the bottom right.')   
                    howManyFound+=1      
                elif diagonal2(i,j,wordToFind) is not None:
                    print(f'{wordToFind} has been found in row {i+1} and column {j+1}. ---- Look to the bottom left.') 
                    howManyFound+=1  
                elif diagonal3(i,j,wordToFind) is not None:
                    print(f'{wordToFind} has been found in row {i+1} and column {j+1}. ---- Look to the top right.')  
                    howManyFound+=1    
                elif diagonal4(i,j,wordToFind) is not None:
                    print(f'{wordToFind} has been found in row {i+1} and column {j+1}. ---- Look to the top left.')   
                    howManyFound+=1                  


#i-x j-y
#i is the list ----- j is the index inside of that list

####LtoR####
def leftToRight(i,j,wordToFindDif):
    #flag ref - https://www.geeksforgeeks.org/use-of-flag-in-programming/
    # at this point, there is a letter that has been found in the data set - and is ready to be checked through these different directions
    flag=True
    # goes through each letter in the word that it thinks it could have found
    for m in range(len(wordToFindDif)):
        #checks that the word can fit in the row 
        if j+m < len(masterList[i]):
            if wordToFindDif[m] == masterList[i][j+m]:
                pass
            else:
                flag=False
                break
        else:
            flag=False
            break
    if flag==True:
        return i,j
           
####RtoL####            
def rightToLeft(i,j,wordToFindDif):
    flag=True
    # goes through each letter in the word that it thinks it could have found
    for m in range(len(wordToFindDif)):
        #checks that the word can fit in the row 
        if j+m < len(masterList[i]):
                                                #looks backwards
            if wordToFindDif[m] == masterList[i][j-m]:
                pass
            else:
                flag=False
                break
        else:
            flag=False
            break
    if flag==True:
        return i,j

####DOWN####
def downLook(i,j,wordToFindDif):
    flag=True
    for m in range(len(wordToFindDif)):
        if (i+m) < len(masterList):
            if wordToFindDif[m] == masterList[i+m][j]:
                pass
            else:
                flag=False
                break
        else:
            flag=False
            break
    if flag==True:
        return i,j
    
####UP####
def upLook(i,j,wordToFindDif):
    flag=True
    for m in range(len(wordToFindDif)):
        if (i-m) >= 0:
            if wordToFindDif[m] == masterList[i-m][j]:
                pass
            else:
                flag=False
                break
        else:
            flag=False
            break
    if flag==True:
        return i,j

####DIAGONAL1####
def diagonal1(i,j,wordToFindDif):
    flag=True
    for m in range(len(wordToFindDif)):
        #if the pattern found is less than the length of the list AND  the pattern found is less than the length of the list index
        if (i+m) < len(masterList) and (j+m)<len(masterList[i]):
                                            #only part that changes with the different diagonal directions
            if wordToFindDif[m] == masterList[i+m][j+m]:
                pass
            else:
                flag=False
                break
        else:
            flag=False
            break
    if flag==True:
        return i,j

####DIAGONAL2####
def diagonal2(i,j,wordToFindDif):
    flag=True
    for m in range(len(wordToFindDif)):
        #if the pattern found is less than the length of the list AND  the pattern found is less than the length of the list index
        if (i+m) < len(masterList) and (j-m)>=0:
                                            #only part that changes with the different diagonal directions
            if wordToFindDif[m] == masterList[i+m][j-m]:
                pass
            else:
                flag=False
                break
        else:
            flag=False
            break
    if flag==True:
        return i,j

####DIAGONAL3####
def diagonal3(i,j,wordToFindDif):
    flag=True
    for m in range(len(wordToFindDif)):
        #if the pattern found is less than the length of the list AND  the pattern found is less than the length of the list index
        if (i-m) >= 0 and (j+m)<len(masterList[i]):
                                            #only part that changes with the different diagonal directions
            if wordToFindDif[m] == masterList[i-m][j+m]:
                pass
            else:
                flag=False
                break
        else:
            flag=False
            break
    if flag==True:
        return i,j

####DIAGONAL4####
def diagonal4(i,j,wordToFindDif):
    flag=True
    for m in range(len(wordToFindDif)):
        #if the pattern found is less than the length of the list AND  the pattern found is less than the length of the list index
        if (i-m) >= 0 and (j-m) >= 0:
                                            #only part that changes with the different diagonal directions
            if wordToFindDif[m] == masterList[i-m][j-m]:
                pass
            else:
                flag=False
                break
        else:
            flag=False
            break
    if flag==True:
        return i,j
    
def showHowManyFound():
    global howManyFound
    print("")
    print(f'{howManyFound} words have been found')


# MAIN LOOP - STARTS THE PROGRAM 
checkForGoodData()