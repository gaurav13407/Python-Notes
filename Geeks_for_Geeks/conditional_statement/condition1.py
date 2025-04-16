##Check the status
class Solution:
    def __init__(self,a,b,flag):
        self.a=a
        self.b=b
        self.flag=flag
    def checkStatus(self):
        if (self.a>0 or self.b>0) and not self.flag:
            return True
        elif(self.a<0 and self.b<0) and self.flag:
            return True
        else:
            return False
        
        # code here
solution1=Solution(1,-1,False)
print(solution1.checkStatus())
   

"""#{ 
 # Driver Code Starts.

# Driver Code
def main():
    
    # Testcase input
    testcases = int(input())
    
    # Looping through testcases
    while(testcases > 0):
        a = int(input())
        b = int(input())
        flag = input()
        
        if(flag == "True"):
            flag = True
        else:
            flag = False
        
        if(Solution().checkStatus(a, b, flag) is True):
            print ("True")
        else:
            print ("False")
        
        testcases -= 1
        print("~")
 
if __name__ == '__main__':
    main()
# } Driver Code Ends"""