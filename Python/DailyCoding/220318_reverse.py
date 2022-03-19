class Solution:
    def reverse(self, x: int) -> int: 
        # if x > 0:  # handle positive numbers  
        #     a =  int(str(x)[::-1])  
        # if x <=0:  # handle negative numbers  
        #     a = -1 * int(str(x*-1)[::-1])  
        # # handle 32 bit overflow  
        # mina = -2**31  
        # maxa = 2**31 - 1  
        # if a not in range(mina, maxa):  
        #     return 0  
        # else:  
        #     return a
         
        # check negative
        strX = str(x)
        if (strX[0] == '-'): 
            negative = True
            strX = strX[1:]
        else: negative = False
            
        # reverse digit
        i = len(strX) - 1
        d = 0
        while i >= 0:
            d = 10*d + int(strX[i])
            i -= 1
          
        if d not in range(-2**31, 2**31 - 1):
            return 0
        else:
            if negative:
                return d * -1
            else:
                return d