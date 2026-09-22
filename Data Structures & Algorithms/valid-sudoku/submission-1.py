class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowDict = {}
        colDict = {}
        quadDict = {}
        ans = True

        for i in range(9):
            if not ans:
                break

            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue

                if i not in rowDict:
                    rowDict[i] = set()
                if num in rowDict[i]:
                    ans = False
                    break
                rowDict[i].add(num)

                if j not in colDict:
                    colDict[j] = set()
                if num in colDict[j]:
                    ans = False
                    break
                colDict[j].add(num)

                gridKey = f"{i//3} {j//3}"
                if gridKey not in quadDict:
                    quadDict[gridKey] = set()
                if num in quadDict[gridKey]:
                    ans = False
                    break
                quadDict[gridKey].add(num)

        return ans