#Qn 1 
# i)
#A knook is a chess piece that combines the moves of a knight and a rook.
#It can attack in an 'L' shape like a knight, and in straight lines like a rook.
#Write code to determine the arrangements of 4 knooks on a 4x4
#chessboard such that no two knooks can attack each other.
#Use a 4 letter string of the form '1234' to represent the arrangement of knooks,
#where the 1st, 2nd, 3rd and 4th characters represent the row number of the knook

#Solution:
def check_knook(arrangement):
    for i in range(1,len(arrangement)-1):
        oregano = int(arrangement[i])
        if abs(int(arrangement[i-1]) - oregano) == 2 or abs(int(arrangement[i+1])- oregano) == 2:
            return False
        if abs(int(arrangement[i-2]) - oregano) == 1 or abs(int(arrangement[i+2]) - oregano) == 1:
            return False    
    return True

#ii)
#Generalise this to n knooks on a n x n chessboard, where 0 <= n <= 8.
#itertools.permutations(string) returns an iterable of the permutations of a string
#Example: 
# for item in itertools.permutations('123'):
#       print(item)
# will give 
# ('1', '2', '3')
# ('1', '3', '2')
# ('2', '1', '3')
# ('2', '3', '1')
# ('3', '1', '2')
# ('3', '2', '1')          
#Solution:
import itertools
def n_knooks(n):
    lst = []
    string_n = ''.join([str(i) for i in range(1, n + 1)])
    for item in itertools.permutations(string_n):
        if check_knook(item):
            lst.append(''.join(item))
    return lst

#Qn 2)
#A magic square is a n x n grid filled with distinct positive integers.
#The sum of the integers in each row, column and diagonal is equal.
#A method of constructing odd order magic squares follows: 
#Place 1 in the middle cell of the top row.
#Move up one row and right one column to place the next number.
#Wrap around if the move goes out of bounds.
#If the target cell is already occupied, move down one row instead.
#Repeat until all n**2 numbers are placed.

#Write code to generate a magic square of odd order n using the method above.[10 marks]
#Print result in a readable format, and return the 2D array representing the magic square.
#Note: This is an extremely easy giveaway question.
def magic_square(n):
    grid =[[0 for _ in range(n)] for _ in range(n)]
    x,y = 0,n//2
    for i in range(1,n**2 + 1):
        while grid[x][y] != 0:
            x += 1
        grid[x][y] = i
        x -= 1
        y += 1
        x %= n
        y %= n
    for item in grid:
        print(item)
    return grid
#Part 2 of Qn 2)
#Write code to determine if a given n x n grid is a magic square.[5 marks]
def is_magic_square(grid):
    n = len(grid)
    magic_sum = sum(grid[0]) #Sum of first row as magic sum
    #Check rows and columns
    for i in range(n):
        if sum(grid[i]) != magic_sum or sum(grid[j][i] for j in range(n)) != magic_sum:
            return False
    #Check diagonals
    if sum(grid[i][i] for i in range(n)) != magic_sum or sum(grid[i][n-1-i] for i in range(n)) != magic_sum:
        return False
    return True
#Comments: https://en.wikipedia.org/wiki/Siamese_method, no change from original.

#Qn 3a)
#Obfuscation is the practice of making code difficult to understand.
#Based on the following code, determine what the functions do
#Hint: Try several inputs, and observe the outputs. 
#Hint: It is related to boolean logic.
#Only the final answer is required. Working will be considered if it benefits the answer.
def 𰻝𰻝面1(a):
    return bool((int(a)+1)%2)
def 𰻝𰻝面2(a,b):
    return 𰻝𰻝面1(a & b)
def 𰻝𰻝面3(a,b):
    return 𰻝𰻝面1(a | b)
def 𰻝𰻝面4(a,b):
    第一 = 𰻝𰻝面2(a,a)
    第二 = 𰻝𰻝面2(b,b)
    第三 = 第一 & 第二
    第四 = 𰻝𰻝面3(第三, 第三)
    第五 = a & 第一
    第六 = 第四^第五
    return 第六
#Solution:
#𰻝𰻝面1(a) returns not a
#𰻝𰻝面2(a,b) returns a NAND b
#𰻝𰻝面3(a,b) returns a NOR b
#𰻝𰻝面4(a,b) returns a OR b
#The first three functions are easily seen
#The 1st function converts a to an integer, adds 1, then mods 2.
#Stepwise for the 4th:
#xn is used for 第n
#x1 = a NAND a = not a
#x2 = b NAND b = not b
#x3 = x1 AND x2 = not a AND not b = not(a OR b)
#x4 = X3 NOR X3 = not x3 OR x3 = a OR b
#x5 = a AND x1 = a AND not a = 0
#x6 = x4 XOR x5 = a OR b OR 0 = a OR b

#Qn 4)
#Arther is told to write questions for C.B Paul Science Quiz.
#Unfortunately, he pon, and did not write any questions.
#He has a time interval in which he needs to fill up with excuses.
#There are n excuses, each with a time interval and a believability score
#Arther can only use one excuse at a time, and the time intervals of the excuses cannot overlap.
#Write code to determine the maximum total believability score Arther can achieve.
#10 marks

#The excuses are a list of tuples, where each tuple contains the start time, end time and believability score of an excuse.
def max_believability(excuses):
    excuses.sort(key=lambda x: x[1]) #Sort by end time
    n = len(excuses)
    dp = [0] * n
    dp[0] = excuses[0][2] #Believability score of first excuse
    for i in range(1, n):
        dp[i] = max(dp[i-1], excuses[i][2]) #Max of not taking or taking current excuse
        for j in range(i-1, -1, -1):
            if excuses[j][1] <= excuses[i][0]: #If excuse j ends before excuse i starts
                dp[i] = max(dp[i], dp[j] + excuses[i][2]) #Max of not taking or taking current excuse with previous best
                break
    return dp[-1]

#Comments: Arther stop ponning lol.


#Qn 5)
#A person is looking for buried treasure in a grid of n x n spaces. 
#Each space has a suspicion value from 0 to 100, with higher values indicating a higher likelihood of treasure being buried there.
#Write code to determine the coordinates of least and most suspicious spots in the form of a tuple of lists.
#Eg if top left is least and bottom right is most, output should be:
#([0,0],[n,n])
#5 marks

#Solution
def find_suspicious_spots(grid):
    least_suspicious = [0,0]
    most_suspicious = [0,0]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] < grid[least_suspicious[0]][least_suspicious[1]]:
                least_suspicious = [i,j]
            if grid[i][j] > grid[most_suspicious[0]][most_suspicious[1]]:
                most_suspicious = [i,j]
    return (least_suspicious, most_suspicious)

#The person now decides to search for a local maxima
#A local maxima is a spot that has a suspicion value greater 
#Than its 8 neighbours (or fewer if on the edge of the grid).
#Write code to determine the coordinates of all local maxima in the grid
#5 marks
def local_maxima(grid):
    local_maxima_coords = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            is_local_maxima = True
            for x in range(max(0, i-1), min(len(grid), i+2)):
                for y in range(max(0, j-1), min(len(grid[0]), j+2)):
                    if grid[i][j] < grid[x][y]:
                        is_local_maxima = False
                        break
                if not is_local_maxima:
                    break
            if is_local_maxima:
                local_maxima_coords.append([i,j])
    return local_maxima_coords

#If no local maxima exists, the person searches all the spaces in descending suspicion order.
#Write code to determine the order of coordinates the person will search in this case
#5 marks
def search_order(grid):
    coords = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            coords.append((grid[i][j], [i,j])) #Tuple of suspicion value and coordinates
    coords.sort(key=lambda x: x[0], reverse=True) #Sort by suspicion value in descending order
    #Lambda is used, but not necessary
    return [coord[1] for coord in coords] #Return only the coordinates in the sorted order

#Comments: NYJC(iykyk)

#Qn 6)
#Write a one line implementation of the quicksort algorithm.
def quicksort_1line(arr):return arr if len(arr) <= 1 else quicksort_1line([item for item in arr if item < arr[len(arr)//2]]) + [arr[len(arr)//2]] + quicksort_1line([item for item in arr if item > arr[len(arr)//2]])
