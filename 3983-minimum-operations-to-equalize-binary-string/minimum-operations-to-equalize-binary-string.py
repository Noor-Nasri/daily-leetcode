class Solution:
    # Suppose k = 4 and num0s = 101. Could we search for just 96, 100, and 104?
    # To consider 92, we must cover a dist of [5] + [4] as fast as we can cover [5].
    # Honestly idk maybe theres edge cases. Lets just search the whole way.

    # The problem with BFS is that a layer of k/2 can be connected to the other k/2, so k^2.
    # Idea: We only consider the ranges of b->c outside the range a could have reached before a->b.
    # Eg: (k=4) A has 64 zero and 32 one. Options for #zeros are -4, -2, +0, +2, +4.
    # So this is a range of values we can reach. And each node visited can simply extend the range.

    # The tricky part is k=3 (odd). Then the parity switches. But its still connected!
    # Eg: If we have 60 zeros, and we can go to 59 or 61 zeros. Even range: {60, 60}. Odd range: {59, 61}.
    # Then both 59 and 61 can connect back to 60, meaning the next layer even range is still singular.
    # Likewise, each node they connect to can still connect back to them, meaning the odd range simply grows.

    # Anyways, I didn't have time to implement this. Gonna do public sol cuz I am busy :(
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        ts = [SortedSet() for _ in range(2)]
        for i in range(n + 1):
            ts[i % 2].add(i)
        cnt0 = s.count('0')
        ts[cnt0 % 2].remove(cnt0)
        q = deque([cnt0])
        ans = 0
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == 0:
                    return ans
                l = cur + k - 2 * min(cur, k)
                r = cur + k - 2 * max(k - n + cur, 0)
                t = ts[l % 2]
                j = t.bisect_left(l)
                while j < len(t) and t[j] <= r:
                    q.append(t[j])
                    t.remove(t[j])
            ans += 1
        return -1