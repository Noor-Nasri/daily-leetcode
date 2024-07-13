class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        originals = [(positions[i], healths[i], directions[i] == "R") for i in range(len(positions))]
        items = sorted(originals, key= lambda x: x[0])

        final_healths = {}
        moving_forward = [] # O(n), cuz each element can go through the stack, but in total the stack is touched O(n)

        def handle_left(health, pos):
            if not moving_forward: # Nothing behind us
                final_healths[pos] = health
                return

            collision, col_pos = moving_forward.pop()
            if collision == health:
                return # both die
            elif collision < health: 
                # remove front element, keep going
                handle_left(health - 1, pos)
            else:
                moving_forward.append((collision - 1, col_pos)) # took damage, but held the line

        for pos, health, direction in items:
            if direction:
                moving_forward.append((health, pos))
            else:
                handle_left(health, pos)

        for health, pos in moving_forward:
            final_healths[pos] = health
        
        # Now just need to return in order they gave us 
        result = []

        for pos in positions:
            if pos in final_healths:
                result.append(final_healths[pos])
        return result


        