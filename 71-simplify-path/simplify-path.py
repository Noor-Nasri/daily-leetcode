class Solution:
    def simplifyPath(self, path: str) -> str:
        real_path = ['']
        path = path.split('/')

        for file in path:
            if not file: continue # was an extra slash, now empty
            elif file == '.': continue
            elif file == '..':
                if len(real_path) == 1: 
                    continue
                
                real_path.pop()
            else:
                real_path.append(file)
            
        if len(real_path) == 1:
            return '/'
            
        return '/'.join(real_path)
                


        