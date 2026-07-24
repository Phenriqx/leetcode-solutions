import java.util.*;

class Solution {
    public boolean isValidSudoku(char[][] board) {
        Map<Integer, Integer> countRow;
        Map<Integer, Integer> countCol;
        List<Map<Integer, Integer>> countBoxes = new ArrayList<>();
        for (int k = 0; k < 9; k++)
            countBoxes.add(new HashMap<>());

        for (int i = 0; i < board.length; i++) {
            countRow = new HashMap<>();
            countCol = new HashMap<>();
            for (int j = 0; j < board[i].length; j++) {
                // sub box verification
                int blockRow = i / 3;
                int blockCol = j / 3;
                int boxID = (blockRow * 3) + blockCol;

                // row verification
                if (Character.isDigit(board[i][j])) {
                    int rowNum = Character.getNumericValue(board[i][j]);
                    if (countRow.containsKey(rowNum) || countBoxes.get(boxID).containsKey(rowNum))
                        return false;
                    else {
                        countRow.put(rowNum, 1);
                        countBoxes.get(boxID).put(rowNum, 1);
                    }
                }

                // column verification
                if (Character.isDigit(board[j][i])) {
                    int colNum = Character.getNumericValue(board[j][i]);
                    if (countCol.containsKey(colNum))
                        return false;
                    else
                        countCol.put(colNum, 1);
                }
            }
        }

        return true;
    }
}