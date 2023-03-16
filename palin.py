def palindrome(inputList):
    
    lengthList= len(inputList)
    for i in range(lengthList): 
        if inputList[i]!=inputList[lengthList-i-1]:
           return False 
    return True
