class Solution {
public:
    int maxArea(vector<int>& height) {
        // Took me a while because I was thinking DP
        // This is a simple 2 pointer problem
        // At (s, e), if s < e, then all other choices (s, _) have < area

        int left = 0;
        int right = height.size() - 1;
        int bestArea = 0;

        while (left < right){
            int area = 0;
            if (height[left] <= height[right]){
                area = height[left] * (right - left);
                left++;
            }else{
                area = height[right] * (right - left);
                right--;
            }

            if (area > bestArea) bestArea = area;
        }

        return bestArea;

    }
};