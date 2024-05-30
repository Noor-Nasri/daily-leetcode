class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1) return s;

        char newString[s.size() + 1];
        newString[s.size()] = '\0';

        int blockSize = (numRows - 1) * 2;
        int numFullBlocks = s.size() / blockSize;
        int sizeLastBlock = s.size() % blockSize;
        //cout << "Inits: Full #" << numFullBlocks << ", last count " << sizeLastBlock << '\n';

        
        for (int ind_diag = 0; ind_diag < s.size(); ind_diag++){
            // must figure out how many elements would be read before it
            //cout << "Investigating element " << ind_diag << " " << s[ind_diag] << '\n';

            int blockNumber = ind_diag / blockSize;
            int rowPlacement = (ind_diag - blockNumber*blockSize) % numRows;
            int prevElementsInRow = (ind_diag - blockNumber*blockSize) / numRows;
            if (prevElementsInRow) rowPlacement = numRows - 2 - rowPlacement;

            //cout << "block # " << blockNumber << ", row # " << rowPlacement << '\n';
            
            // 1 per block for top/bottom, otherwise 2 per block
            int multiplier = (rowPlacement > 0 && rowPlacement < numRows - 1) ? 2 : 1;
            prevElementsInRow += blockNumber*multiplier;
            //cout << "before from row:  " << prevElementsInRow << '\n';

            int prevElementsAbove = 0;
            if (rowPlacement) {
                prevElementsAbove += numFullBlocks; // first row
                //cout << "From first row:  " << prevElementsAbove << '\n';

                prevElementsAbove += (rowPlacement - 1)*numFullBlocks*2; // other rows
                //cout << "From other rows too:  " << prevElementsAbove << '\n';

                prevElementsAbove += min(sizeLastBlock, rowPlacement);
                //cout << "After adding downwards from last cell: " << prevElementsAbove << '\n';

                // final block inclusion
                if (sizeLastBlock > numRows){
                    // After going down, also went up in final cell
                    int rem_diag = sizeLastBlock - numRows;
                    int highest_row = numRows - rem_diag;
                    int above_us = (rowPlacement + 1) - highest_row;
                    if (above_us > 0) prevElementsAbove += above_us;
                    //cout << "After adding downupwards from last cell: " << prevElementsAbove << '\n';
                }

            }

            //cout << "before from above:  " << prevElementsAbove << '\n';
            newString[prevElementsInRow + prevElementsAbove] = s[ind_diag];
        }

        return newString;
    }
};