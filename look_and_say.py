#11
#21
#1211
#111221
#?

num = "11" #We defined it as a string for convert it to a list.
arr = list(num) #Converted to list.
convert_int = list(map(int, arr)) #we converted the elements to integer.
print(convert_int)
next_one = []

for j in range(4):
    i = 0

    while (i < len(convert_int)):
        c = 1
        
        #In this loop below, first the iter is checked to avoid getting a range error. If the next element of the list is the same as the current element, the counter is increased by 1.
    
        while (i+1 < len(convert_int) and convert_int[i] == convert_int[i+1]): 
            i += 1
            c += 1
        
        #When the loop is finished, the amount of the number and itself are added to the list.
        
        next_one.append(c)
        next_one.append(convert_int[i])
        
        i += 1
    
    print(next_one)
    
    convert_int.clear()
    
    #We continue the pattern by assigning the next number to the convert_int list.

    for k in range(len(next_one)):
        convert_int.append(next_one[k]) 
    
    next_one.clear()

    

