def solve(A, B):
    # return the max possible sum of elements you can pick :)
    # example array: 1, -6, 10, -2, -9, -5, 2
    # create two arrays -> it can be of anysize literally, take the half

    length = len(A)
    if B == length:
        return sum(A)

    first_arr = A[0:B] # this is from 0 to 47 -> 48 numbers
    second_arr = A[length - B:length] # this is from length - 1 - B (12) to 60

    # first_arr_length = B
    # # second_arr_length = length - B

    # sum up the values in first_arr
    value = 0
    for i in range(B):
        first_arr[i] += value
        value = first_arr[i]

    #and second_arr
    value = 0
    for i in range(len(second_arr) - 1 , -1, -1):
        second_arr[i] += value
        value = second_arr[i]
    
    print(first_arr)
    print(second_arr)

    result = -10**9
    for i in range(B):
        if i == B - 1:
            cmpres = first_arr[i]
        else:
            cmpres = first_arr[i] + second_arr[i + 1] # cai second arr di tu 0 den 47
        result = max(result, cmpres, second_arr[0])
    
    print(result)

# A = [1,2,3,4,5]
# A = [ -533, -666, -500, 169, 724, 478, 358, -38, -536, 705, -855, 281, -173, 961, -509, -5, 942, -173, 436, -609, -396, 902, -847, -708, -618, 421, -284, 718, 895, 447, 726, -229, 538, 869, 912, 667, -701, 35, 894, -297, 811, 322, -667, 673, -336, 141, 711, -747, -132, 547, 644, -338, -243, -963, -141, -277, 741, 529, -222, -684, 35 ]
# B = 48

A = [ -969, -948, 350, 150, -59, 724, 966, 430, 107, -809, -993, 337, 457, -713, 753, -617, -55, -91, -791, 758, -779, -412, -578, -54, 506, 30, -587, 168, -100, -409, -238, 655, 410, -641, 624, -463, 548, -517, 595, -959, 602, -650, -709, -164, 374, 20, -404, -979, 348, 199, 668, -516, -719, -266, -947, 999, -582, 938, -100, 788, -873, -533, 728, -107, -352, -517, 807, -579, -690, -383, -187, 514, -691, 616, -65, 451, -400, 249, -481, 556, -202, -697, -776, 8, 844, -391, -11, -298, 195, -515, 93, -657, -477, 587 ]
B = 81
solve(A, B)