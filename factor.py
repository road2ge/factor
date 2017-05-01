command = raw_input("Would you like to factor a number, find common factors of numbers, or factor a trinomial. \nEnter factor commonFactor or factorial. \nEnter exit to quit. ")

######################################################################################
################################### MADE BY ##########################################
################################# Kale Miller  #######################################
######################################################################################

def findFactors(num, human=False):
    '''Finds all integer factors of an integer'''
    num = int(num)
    factors = []
    if num < 0:
        negative = True
        num *= -1
    else:
        negative = False
    for factor in range(1, int(int(num) ** .5 + 1)):
        if num % factor == 0:
            factors.append(factor)
            factors.append(num / factor)
    if negative:
        factors2 = []
        for k in factors:
            factors2.append(k)
        ite = True
        index = 0
        for i in factors:
            if ite:
                factors[index] = i * -1
            ite = not ite
            index += 1

        ite = False
        index = 0
        for j in factors2:
            if ite:
                factors2[index] = j * -1
            ite = not ite
            index += 1
        factors.extend(factors2)
    if human:
        returnString = ""
        for x in factors:
            returnString += str(x) + ", "
        returnString = returnString[:len(returnString)-2]
        if len(returnString) != 1:
            return returnString
    return factors

def findCommonFactors(numlist, hidden=False):
    '''Finds common factors of a given list of integer arguments'''
    allFactorList = [] # list of all factors. made of multiple lists later on
    commonFactors = [] # list of common factors

    # load the lists into allFactorList
    ind = 0
    for a in numlist:
        a = int(a)
        numlist[ind] = a
        ind += 1

    for i in numlist:
        allFactorList.append(findFactors(i))
    # iterate through factors
    def check(num):
        '''Checks to see if the correct amount of numbers are in allFactorList'''

        # This is only made because I need to have a boolean and can't break
        # loops, to my knowledge.

        correct = 0 # correct needs to be the length of numlist.
        # essentially there should always be one correct, the rest are all the
        # other lists.

        for x in numlist:
            if x % num != 0:
                return False
        return True

    for j in allFactorList:
        for k in j:
            if check(k):
                if k not in commonFactors:
                    commonFactors.append(k)
    return commonFactors

def trinomial(a,b,c):

    print "There is no guarantee that any of this will work."
    print "\nDon't solely rely on this and check your answers as always."
    # a,b,c are ax^2 + bx + c
    returnString = ""
    try:
        d = ((b ** 2) - (4 * a * c)) ** .5
    except:
        return "no solutions/not factorable"
    solution2 = (-1 * b + d) / (2 * a)
    solution1 = (-1 * b - d) / (2 * a)
    factors = findFactors(a * c)

    def factorWay():
        '''Attempt alternate way of finding solutions. Not necessarily more efficent but easier
        to manipulate, sometimes more accurate, and more integers than floats which not only looks
        nicer but can minimize the amount of anonomalous returns including weird decimals and stuff'''
        for i in factors:
            for j in factors:
                if i + j == b and i * j == a * c:
                    solution1 = i
                    solution2 = j
        return solution1, solution2
    facWay = False
    try:
        solution1, solution2 = factorWay()
        facWay = True
    except:
        pass

    def floatEqInt(number):
        '''Essentially returns true if a number is exact (i.e. no decimals except .0) or if an integer'''
        # Convert to float in case of integer
        number = number / 1.0
        # Check if the values are still equivalent
        if int(number) == number:
            return True
        return False
    if facWay:
        if a == 1:
            returnString = "(X + " + str(solution1) + ")(X + " + str(solution2) + ")"
        elif a == -1:
            returnString = "(-X + " + str(solution1) + ")(X + " + str(solution2) + ")"
        elif type(a) != int and not floatEqInt(a):
            returnString = "You probably weren't asked to factor this. Come up with it yourself."
            returnString += "\n the solutions are " + solution1 + solution2
        elif a > 0:
            if solution2 % a == 0 and floatEqInt(solution2):
                returnString = "(" + str(a) + "X + " + str(solution1) + ")(X + " + str(solution2/a) + ")"
            elif solution1 % a == 0 and floatEqInt(solution1):
                returnString = "(" + str(a) + "X + " + str(solution2) + ")(X + " + str(solution1/a) + ")"
        elif a < 0:
            if solution2 % a == 0:
                returnString = "(" + str(a) + "X + " + str(solution1) + ")(X + " + str(solution2/a) + ")"
            else:
                returnString = "(" + str(a) + "X + " + str(solution2) + ")(X + " + str(solution1/a) + ")"
    else:
        returnString = "I doubt you can factor these. Your solutions are" + solution1 + " and " + solution2

    if len(returnString) < 8:
        returnString = "not factorable. Solutions are " + str(solution1) + " and " + str(solution2)
    return returnString

while command.lower() != "exit":
    if command.lower() == "factor":
        numToFactor = input("Enter a number: ")
        print findFactors(numToFactor)
    elif command.lower() == "commonfactor":
        numsToFactor = raw_input("Enter numbers like so: 1,2,3... ").split(",")
        print findCommonFactors(numsToFactor)
    elif command.lower() == "trinomial":
        print "The form for this quadratic will be ax^2 + bx + c"
        a = input("Enter a: ")
        b = input("Enter b: ")
        c = input("Enter c: ")
        print trinomial(a,b,c)
    command = raw_input("Now what would you like to do? ").lower()