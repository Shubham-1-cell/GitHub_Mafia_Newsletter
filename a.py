#take the str parameter being passed and return a compressed version of the string using the Run-length encoding algorithm. 
def StringChallenge(strParam):
    # your code goes here
    output = ''
    count = 1
    for i in range(len(strParam)-1):
        if strParam[i] == strParam[i+1]:
            count += 1
        else:
            output += strParam[i] + str(count)
            count = 1
    output += strParam[-1] + str(count)
    if len(output) >= len(strParam):
        return strParam
    else:
        return output
print (StringChallenge('aabbccc'))