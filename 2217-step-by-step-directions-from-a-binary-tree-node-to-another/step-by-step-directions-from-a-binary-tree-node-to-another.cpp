/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    pair<bool, bool> oneWayDirections(TreeNode* root, int value1, stack<char>& dirs1, int value2, stack<char>& dirs2){
        // changed it to be a single pass through of path->node
        if (root == NULL) return {false, false};

        pair<bool, bool> result1 = oneWayDirections(root->left, value1, dirs1, value2, dirs2);
        pair<bool, bool> result2 = oneWayDirections(root->right, value1, dirs1, value2, dirs2);
        pair<bool, bool> new_results = {false, false};
        
        // first, fix new_results
        if (result1.first || result2.first || root->val == value1) new_results.first = true;
        if (result1.second || result2.second || root->val == value2) new_results.second = true;

        // Now adjust path based on children
        if (result1.first) dirs1.push('L');
        else if (result2.first) dirs1.push('R');

        if (result1.second) dirs2.push('L');
        else if (result2.second) dirs2.push('R');

        return new_results;
    }


    string getDirections(TreeNode* root, int startValue, int destValue) {
        stack<char> dir_start = {};
        stack<char> dir_dest = {};
        oneWayDirections(root, startValue, dir_start, destValue, dir_dest);

        // remove common pathing
        while (!dir_start.empty() && !dir_dest.empty() && dir_start.top() == dir_dest.top()){
            dir_start.pop();
            dir_dest.pop();
        }

        // create final string
        int len_result = dir_start.size() + dir_dest.size();
        char result[len_result + 1];
        result[len_result] = '\0';
        for (int ind = 0; ind < dir_start.size(); ind++){
            result[ind] = 'U';
        }

        for (int ind = dir_start.size(); ind < len_result; ind++){
            result[ind] = dir_dest.top();
            dir_dest.pop();
        }

        return result;
    }
};