def Calculator(str):
    checker = False
    for char in str:
        if checker == False:
             if char in ('+','-','(','*','/'):
                checker = True
        if char == '(':
            substrStart = str.find(char)
            tmp = 0
            for substrChar in str[substrStart : len(str) : 1] :     #Dont understand why it should be len(str) instead of len(str)-1
                if substrChar == '(':
                    tmp += 1
            count = 0 
            for substrChar in str[substrStart : len(str) : 1] :     #Dont understand why it should be len(str) instead of len(str)-1
                if substrChar == ')':
                    count += 1
                    if count == tmp:
                        substrEnd = str.find(substrChar)
                        return Calculator(str[substrStart+1:substrEnd]) #Dont understand why it should be substrEnd instead of substrEnd-1
        if char == '+':
            splitted = str.split("+")
            return Calculator(splitted[0]) + Calculator(splitted[1])
        if char == '-':
            splitted = str.split("-")
            return Calculator(splitted[0]) - Calculator(splitted[1])
       
        if char == '*':
            splitted = str.split("*")
            return Calculator(splitted[0]) * Calculator(splitted[1])
        if char == '/':
            splitted = str.split("/")
            return Calculator(splitted[0]) / Calculator(splitted[1])
        elif char == str[-1] and checker == False:
            return float(str)
