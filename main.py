"""
In this problem, at the beginning my perspective was to go from top to the bottom with always taking the max value and sum them until 
the end. But I realized that when going from top to the bottom, we are just missing some paths that might have greater values than the 
branches we are dealing with. So, we need to looking at all values. I found another way of doing this (of course with some help from the
dynamic programming), instead of looking from top to the bottom, I started to look from bottom to the top with considering all possible 
max values for each branch. Here is how the algorithm works:

1)First, I take each line from a given txt file and create a right triangle with 2D array form like this:

1 0 0 0
8 4 0 0
2 6 9 0
8 5 9 3

2) Then, I replace the prime numbers by zero, since zero is the identity element for sum.

1 0 0 0
8 4 0 0
0 6 9 0
8 0 9 0

3) After that, starting from (n-1)th line where n is the dimension of the array I just sum all the adjacent non-prime values and only get the max ones.
After that process our array looks like this:

1 0 0 0
8 4 0 0
0 15 18 0 

After applying same steps to each row until reaching the top of the triangle we get:

1 0 0 0
23 22 0 0

24 is the final value
"""

import numpy as np

#Here is the function for determining whether a number is prime or not.
#If the number is prime, we return 1 if not we return 0
def prime_num(num):
    count = 0

    #Prime numbers are greater than 1
    if (num > 1):
    	#just simply dividing the number with its factorials, if count is 1 we say it is not a prime number     
        for i in range(2, num):         
            if (num % i) == 0:  
                count = 1
        if count == 1:
            return 0
        else:
            return 1
    else:
        return 0

#file operations
with open('file.txt', 'r') as f:        #read from a file named "file.txt"
    lines = f.read().splitlines()       #splitline looks at the line breaks
    last_line = lines[-1]               #get the last line

    size_last_line = len(last_line.split())     #find the size of last line
    arr = np.zeros((size_last_line, size_last_line), dtype=int)     #create a 2D square array with same size of the last line

    #filling our array with the corresponding triangle values
    for i in range(size_last_line):
        for j in range(len(lines[i].split())):
            word = lines[i].split()         #split the values by space(" ") and obtain them one by one
            arr[i][j] = word[j]             #putting them to the exact places in the array

            #Since prime numbers are not allow to be added, we can eliminate them
			#at the beginning of the all process by just making them 0 which is
			#identity element for summing operation. 
            if(prime_num(arr[i][j])):
            	arr[i][j] = 0

#Here is the part for finding maximum summing path with non-prime numbers
for i in range(size_last_line):
    for j in range(size_last_line-i-1):

    	#If the (n-1)th row of a specific column is zero which means it was
    	#prime before, we ignore it and continue. 
    	if(arr[(size_last_line-1) - i - 1][j] == 0):
    		continue

    	#If both of the numbers we are comparing are zero then this means
    	#we will never reach to the bottom line which is what we dont want.
    	if(arr[(size_last_line-1) - i][j] == 0) and (arr[(size_last_line-1) - i][j+1] == 0):
    		arr[(size_last_line-1) - i - 1][j] = 0
    		continue
    	
    	#If above statement is not satisfied, then we compare the n'th and (n+1)th
    	#elements of given column and choose the biggest one for addition.
    	if (arr[(size_last_line-1) - i][j] > arr[(size_last_line-1) - i][j+1]):
    		arr[(size_last_line-1) - i - 1][j] += arr[(size_last_line-1) - i][j]
    	else:
    		arr[(size_last_line-1) - i - 1][j] += arr[(size_last_line-1) - i][j+1]
    	

print(arr[0][0])        #max sum is added to the first entry of the array


