class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):

        binn=str(bin(n))
        arr=[]

        if len(binn)<34:
            for i in range(34-len(binn)):
                arr.append(0)


        for i in range(len(binn)-2):
            arr.append(binn[i+2])


        ans=""

        for j in range(len(arr)):
            ans += str(arr[len(arr)-1-j])

        print(ans)

        return int(ans,2)
        


        

        
