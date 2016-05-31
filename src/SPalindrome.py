import time
# function to check for palindrome
def palindrome(n):
    # replace all new lines
    n = n.replace('\n', "")
    # replace all spaces
    # THIS ASSUMES ONLY ONE SPACE BETWEEN WORDS
    n = n.replace(" ", "")
    # put all letters as lowercase
    n = n.lower()
    # return if the word front and back match
    return n == n[::-1]
# main
if __name__ == '__main__':
    # take time of start of program
    program_start = time.time()
    # create array to hold words
    array = []
    # create array to hold values to detertime
    # at which position of the array array
    # is a palindrome or not
    palindromeArray = []
    # open file for each word
    with open("Palindromes.txt", "r") as f:
        # read in each word
        for line in f:
            # append word to array
            array.append(line)
    # take start time of the actually work
    function_start = time.time()
    # loop array and determine palindromes
    for i in range(len(array)):
        # check if current word is palindrome or not
        palinOrNot = palindrome(array[i])
        # if current word is a palindrome
        if (palinOrNot == True):
            # mark array with a 1
            palindromeArray.append(1)
        # if current word is NOT a palindrome
        else:
            # mark array with a 0
            palindromeArray.append(0)
    # take start time of the actually work
    function_end = time.time()
    for i in range (len(array)):
        # if word is not palindrome
        # if result is 1
        if palindromeArray[i] != 1:
            # print word
            print(array[i])
    # take end time of program
    program_end = time.time()
    # display time of entire program
    print("Time elapsed of entire program: ", (program_end - program_start))
    # display time of function
    print("Time elapsed of the function: ", (function_end - function_start))

    # alternate version
    '''

    import time

    def palindrome(n):
        n = n.replace('\n', "")
        n = n.replace(" ", "")
        n = n.lower()
        #print(n)
        #print(n[::-1])
        return n == n[::-1]

    with open("Palindromes.txt", "r") as f:
        t1 = time.time()
        array = []
        palindromeArray = []
        for line in f:
            array.append(line)
            #print(line)
            palinOrNot = palindrome(line)
            if (palinOrNot == True):
                palindromeArray.append(1)
                #print("Palindrome")
            else:
                #print("Not palindrome")
                palindromeArray.append(0)


    t2 = time.time()


    for i in range(len(palindromeArray)):
        if palindromeArray[i] == 0:
            print(i, end = " ")
            print(array[i])

    print("\nTime elapsed in seconds: ", t2 - t1)
    '''