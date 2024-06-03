class Solution {
public:
    int appendCharacters(string s, string t) {
        int s_ind = 0;
        int t_ind = 0;
        
        while (s_ind < s.size() && t_ind < t.size()){
            // Pair them
            if (s[s_ind] == t[t_ind]){
                s_ind++;
                t_ind++;
            }else{
                s_ind++;
            }
        }

        return t.size() - t_ind;
    }
};