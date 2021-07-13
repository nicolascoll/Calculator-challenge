def Calculator(str):
    checker = False
    for char in str:
        if checker == False:
             if char in ('+','-','(','*','/'):
                checker = True
        if char == '(':
            firstbracketindex = str.find(char)
            for char in str[firstbracketindex : len(str) - 1 : 1] :
                tmp = 0
                if char == '(':
                    tmp += 1
            substrStart = str.find(char)
            for char in str[str.find(char) : len(char) - 1 : 1] :
                count = 0 
                if char == ')':
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
