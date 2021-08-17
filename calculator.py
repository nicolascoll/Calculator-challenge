def Calculator(string):
    checker = False
    if '(' in string:
        checker = True
        substrStart = string.find('(')
        tmp = 0
        for substrChar in string[substrStart : len(string) : 1] :    
            if substrChar == '(':
                tmp += 1
        count = 0 
        for substrChar in string[substrStart : len(string) : 1] :     
            if substrChar == ')':
                count += 1
                if count == tmp:
                    substrEnd = string.rfind(substrChar) # rfind() method because find() will always return the first index that meets the condition 
                    return Calculator(string[0:substrStart]+str(Calculator(string[substrStart+1:substrEnd]))+string[substrEnd+1:]) 
    if '+' in string:
        splitted = string.split("+",1)
        checker = True
        return Calculator(splitted[0]) + Calculator(splitted[1])
    if '-' in string:
        if string.find('-') == 0:
            subString = ''
            for strChar in string[1 : len(string) : 1] :
                if strChar not in ['-','+','/','*']:
                    subString += strChar
                else:
                    substrEnd = strChar
                    substrEndIndex = string.index(strChar)
                    return -Calculator(string[1:substrEnd])+strChar+Calculator(string[substrEndIndex+1:])
        else:
            splitted = string.split("-",1)
            checker = True
            return Calculator(splitted[0]) - Calculator(splitted[1])
    if '*' in string:
        splitted = string.split("*",1)
        checker = True
        return Calculator(splitted[0]) * Calculator(splitted[1]) 
    if '/' in string:
        splitted = string.split("/",1)
        checker = True
        return Calculator(splitted[0]) / Calculator(splitted[1])
    elif checker == False:
        return float(string)
