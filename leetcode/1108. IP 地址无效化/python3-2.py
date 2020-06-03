class Solution:
    def defangIPaddr(self, address:str) -> str:
        return address.replace('.', '[.]')

ip = Solution()
print(ip.defangIPaddr('153.321.212.'))