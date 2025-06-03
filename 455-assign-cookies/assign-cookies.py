class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        children = sorted(g)
        cookies = sorted(s)
        numContent = 0
        child_ind = 0
        cookie_ind = 0

        while child_ind < len(children) and cookie_ind < len(s):
            if cookies[cookie_ind] >= children[child_ind]:
                numContent += 1
                child_ind += 1
            
            cookie_ind += 1

        return numContent
