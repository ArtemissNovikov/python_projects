import math
def decrypt(encrypted_text, n):
    res = encrypted_text
    #decryption loop
    for i in range(n):
        '''
        in order to decrypt in each loop we have to
        split the string in half and then construct
        a new string consequently adding symbols from second and first half
        '''
        #get string len
        l = math.floor(len(res)/2)
        #split string in half
        half_f = res[:l]
        half_s = res[l:]
        lst = "";
        #construct a new string
        for i in range(l+1):
            #if halfs arent equal len, we need to get symbol from one of them while not trying to access the other out of index range
            if len(half_s) > i:
                lst += half_s[i] 
            if len(half_f) > i:
                lst += half_f[i]           
        res = lst
        
    return res

def encrypt(text, n):
    if n > 0:
        l = len(text)
        lst = [];
        for i in range(l):
            if i % 2 != 0:
                lst.append(text[i]);

        for i in range(l):
            if i % 2 == 0:
                lst.append(text[i]);
        res = "".join(lst)
        return encrypt(res, n-1)
    else:
        return text
