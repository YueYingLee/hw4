def sort_dictionary(inputDictionary):
    ageDict = {}
    result = []
#key is names, values are the tuple which include phone num and age   
    for i in inputDictionary:
        name = i
        phoneNum = inputDictionary[i][0]
        age = inputDictionary[i][1]
        if age not in ageDict:
            ageDict[age] = [(name, phoneNum)]
        else:
            ageDict[age].append((name, phoneNum))
            
    for j in sorted(ageDict.keys()) :
        result += ageDict[j]
    return result
