


def isPowerOfTwo(num):
    if(num == 1):
        return True
    

    while(num > 1):
        num = num / 2
        if (num == 2):
            return True
        
    

    return False

print(isPowerOfTwo(3))