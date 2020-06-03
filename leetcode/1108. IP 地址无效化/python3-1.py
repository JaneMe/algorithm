class Solution:
    def defangIPaddr(self, address: str) -> str:
        newAddress = ''
        for i in address:
            if(i == '.'):
                newAddress += '[.]'
            else:
                newAddress += i
        return newAddress
ip = Solution()
newIp = ip.defangIPaddr("19.2.34.423.31")
print(newIp)