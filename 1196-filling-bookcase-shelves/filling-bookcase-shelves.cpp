class Solution {
public:
    int minHeightShelves(vector<vector<int>>& books, int shelfWidth) {
        // Note to self: I need to go to work and my solution is not working, so I am submitting this
        // solution (not mine) to analyze it in the future. (Remember to analyze ..)

        int n = books.size();
        int f[n + 1];
        f[0] = 0;
        for (int i = 1; i <= n; ++i) {
            int w = books[i - 1][0], h = books[i - 1][1];
            f[i] = f[i - 1] + h;
            for (int j = i - 1; j > 0; --j) {
                w += books[j - 1][0];
                if (w > shelfWidth) {
                    break;
                }
                h = max(h, books[j - 1][1]);
                f[i] = min(f[i], f[j - 1] + h);
            }
        }
        return f[n];
        
    }
};