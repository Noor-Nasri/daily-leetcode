class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        line = [words[0]]
        length = len(words[0])
        cur = 1

        while cur < len(words):
            word = words[cur]
            if len(word) + length + len(line) > maxWidth: 
                if len(line) == 1: 
                    # Just 1 word, special case
                    lines.append(line[0] + " "*(maxWidth - length))

                else:
                    # Make new line
                    evenSpaces = (maxWidth - length)//(len(line) - 1)
                    extraSpaces = (maxWidth - length)%(len(line) - 1)
                    for j in range(extraSpaces):
                        line[j] += " "
                    lines.append((" "*evenSpaces).join(line))

                # Restart line
                line = [word]
                length = len(word)
            else:
                line.append(word)
                length += len(word)

            cur += 1
        
        # Add last line
        extraSpaces = (maxWidth - length) - (len(line) - 1)
        lines.append(" ".join(line) + " "*extraSpaces)

        return lines

        