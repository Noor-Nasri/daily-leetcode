class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        unordered_map<char, int> magazine_counts;
        
        //for (char c = 'a'; c <= 'z'; c++) magazine_counts[c] = 0;
        for (char c : magazine) magazine_counts[c]++;

        for (char c : ransomNote){
            if (!magazine_counts[c]) return false;

            magazine_counts[c]--;
        }

        return true;
    }
};