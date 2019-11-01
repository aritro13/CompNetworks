import operator

sender_data = input("Enter Binary data to send: ")

def xor(a, b): 
    result = [] 
    for i in range(1, len(b)): 
        result.append(str(operator.xor(int(a[i]),int(b[i]))))
    return ''.join(result)
   
def mod2div(divident, divisor): 
    pick = len(divisor) 
    tmp = divident[0 : pick] 
    while pick < len(divident): 
        if tmp[0] == '1': 
            tmp = xor(divisor, tmp) + divident[pick] 
        else:
            tmp = xor('0'*pick, tmp) + divident[pick] 
        pick += 1
    if tmp[0] == '1': 
        tmp = xor(divisor, tmp) 
    else: 
        tmp = xor('0'*pick, tmp)
    checkword = tmp
    return checkword


def encodeData(data, key): 
    l_key = len(key) 
    appended_data = data + '0'*(l_key-1) 
    remainder = mod2div(appended_data, key) 
    codeword = data + remainder 
    return codeword  

def decodeData(data, key): 
    l_key = len(key) 
    appended_data = data + '0'*(l_key-1) 
    remainder = mod2div(appended_data, key) 
    return remainder 

key = "1010"

ans = encodeData(sender_data,key) 
receiver_data = ans

print("Message Received: "+receiver_data)
ans = decodeData(receiver_data, key) 
print("Remainder after decoding is: "+ans) 


