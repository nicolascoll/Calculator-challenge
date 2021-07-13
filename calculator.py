def Calculator(str):
    checker = False
    for char in str:
        if checker == False:
             if char in ('+','-','(','*','/'):
                checker = True
        if char == '(':
            firstbracketindex = str.find(char)
            tmp = 0
            for substrChar in str[firstbracketindex : len(str) - 1 : 1] : 
                if substrChar == '(':
                    tmp += 1
            substrStart = str.find(char)
            count = 0 
            for substrChar in str[str.find(char) : len(str) - 1 : 1] :
                if substrChar == ')':
                    count += 1
                    if count == tmp:
                        substrEnd = str.find(char)
                        return Calculator(str[substrStart:substrEnd]) 
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
        elif char == str[-1] and checker == False:# Not sure if its gonna compare to the value or the reference
            return str
