def Calculator(string):
    checker = False
    for char in string:
        if '(' in string:
            checker = True
            substrStart = string.find('(')
            tmp = 0
            for substrChar in string[substrStart : len(string) : 1] :     #Reminder it should be len(str) instead of len(str)-1
                if substrChar == '(':
                    tmp += 1
            count = 0 
            for substrChar in string[substrStart : len(string) : 1] :     #Reminder it should be len(str) instead of len(str)-1
                if substrChar == ')':
                    count += 1
                    if count == tmp:
                        substrEnd = string.rfind(substrChar) # rfind() method because find() will always return the first index that meets the condition 
                        return Calculator(string[0:substrStart]+str(Calculator(string[substrStart+1:substrEnd]))+string[substrEnd+1:])  #Reminder it should be substrEnd instead of substrEnd-1
        if '+' in string:
            splitted = string.split("+",1)
            checker = True
            return Calculator(splitted[0]) + Calculator(splitted[1])
        if '-' in string:
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
        elif char == string[-1] and checker == False:
            return float(string)
