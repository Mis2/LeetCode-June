#Validate IP Address
#17-06-2020

class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        if IP.count('.') == 3:
            return self.validateIPv4(IP)
        elif IP.count(':') == 7:
            return self.validateIPv6(IP)
        else:
            return 'Neither'
        
    def validateIPv4(self, IP):
        nums = IP.split('.')
        for num in nums:
            if len(num) == 0 or len(num) > 3:
                return 'Neither'
            if num[0] == '0' and len(num) != 1 or not num.isdigit() or int(num) > 255:
                return 'Neither'
        return 'IPv4'
    
    def validateIPv6(self, IP):
        nums = IP.split(':')
        hexdigits = '0123456789abcdefABCDEF'
        
        for num in nums:
            if len(num) == 0 or len(num) > 4 or not all(c in hexdigits for c in num):
                return 'Neither'
        return 'IPv6'    