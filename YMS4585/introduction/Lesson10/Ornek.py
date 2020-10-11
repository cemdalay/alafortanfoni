import os
os.system("Clear")


def CustomStrip(param, *chars):

    i = 0

    while i < (len(chars)**2):
        if param[0] in chars:
            param = param.strip(param[0])
        if(param[len(param) - 1] in chars):
            param = param.strip(param[len(param) - 1])
        else:
            break
        i += 1
    return param


result = CustomStrip('&@?-_Bilge Adam Beşiktaş&@?-_', '@', '?', '-', '_', '&')
print(result)
