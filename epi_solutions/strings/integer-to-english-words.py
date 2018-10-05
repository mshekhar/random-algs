class Solution(object):
    LESS_THAN_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                    "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    TENS_MAP = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    POW_MAP = ["", "Thousand", "Million", "Billion"]

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """

        if not num:
            return "Zero"
        words = ""
        i = 0
        while num:
            if num % 1000:
                words = self.helper(num % 1000).strip() + " " + self.POW_MAP[i].strip() + " " + words.strip()
            num /= 1000
            i += 1
        return words.strip()

    def helper(self, num):
        if num < 20:
            return self.LESS_THAN_20[num]
        elif num < 100:
            return self.TENS_MAP[num / 10] + " " + self.helper(num % 10)
        return self.LESS_THAN_20[num / 100] + " Hundred " + self.helper(num % 100)


print Solution().numberToWords(50868)
