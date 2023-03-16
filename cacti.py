def cacti_number(array):
    
   cactiNum=0
   for i in range (len(array)):
     for j in range (len(array[0])):  
     
       canPlantCacti = True
       if array[i][j] == 0 :
            if (i > 0 and array[i-1][j] != 0):
                canPlantCacti = False
            elif (i < len(array) - 1 and array[i+1][j] != 0):
                canPlantCacti = False
            elif (j > 0 and array[i][j-1] != 0):
                canPlantCacti = False
            elif (j < len(array[0]) - 1 and array[i][j+1] != 0):
                canPlantCacti = False
            
            if canPlantCacti == True:
                array[i][j] = 1;
                cactiNum = cactiNum + 1;
          
   return cactiNum
