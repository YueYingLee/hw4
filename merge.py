def merge(list1, list2): 
    
  newList=[]
  i=0
  j=0
  while i < len(list1) and j < len(list2):
     if list1[i] <=list2[j]:
        newList.append(list1[i])
        i = i+ 1
 
     else:
        newList.append(list2[j])
        j = j+ 1
 
#take care the remaining elements 
  if (i<len(list1)):
    newList.extend(list1[i:]) 
  if (j<len(list2)):
    newList.extend(list2[j:])
  return newList
