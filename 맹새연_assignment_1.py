num = int(input('숫자 입력 : ')) # Get value for 'num' from the user
i = 1 # Set the value of 'i' to 1
while (i <= num) : # While (i <= num) do 
    count = str(i).count('3') + str(i).count('6') + str(i).count('9') # Set the value of 'count' to counting how many '3', '6', and '9' exist in i  
    if count == 2: # If 'count' is equal to 2 then
        print('**', end = ' ') # print '**' and tap once (don't go to a new line)
    elif count == 1: # If 'count' is equal to 1 then
        print('*', end = ' ') # print '*' and tap once (don't go to a new line)
    elif count == 0: # If 'count' is equal to 0 then
        print(i, end = ' ') # print i and tap once (don't go to a new line)
    i = i + 1 # Add 1 to the value of 'i'