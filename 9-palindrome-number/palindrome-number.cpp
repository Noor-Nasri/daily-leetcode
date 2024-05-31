class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) return false;
        if (x == 0) return true;

        int numDigits = log10(x) + 1;
        for (int digit = 0; digit <= numDigits/2; digit++){
            int val1 = x / pow(10, digit);
            val1 = val1 % 10;

            int val2 = x / pow(10, numDigits - digit - 1);
            val2 = val2 % 10;
            //cout << "comparing " << val1 << " with " << val2 << '\n';

            if (val1 != val2) return false;
        }

        return true;
    }
};