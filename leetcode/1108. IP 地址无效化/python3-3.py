class Solution:
    def defangIPaddr(self, address:str) -> str:
        listAddress = address.split('.')
        return '[.]'.join(listAddress)

ip = Solution()
newIp = ip.defangIPaddr("19.2.34.423.31")
print(newIp)