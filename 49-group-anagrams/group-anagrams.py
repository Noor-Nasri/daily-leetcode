class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupings = {}
        ASCII_A = ord('a')

        for string in strs:
            values = [0 for i in range(26)]
            for char in string:
                values[ord(char) - ASCII_A] += 1
            
            mapped = tuple(values)
            if mapped in groupings:
                groupings[mapped].append(string)
            else:
                groupings[mapped] = [string]

        return groupings.values()
