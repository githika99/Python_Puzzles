class Solution:
    def maximalSquare(self, matrix) -> int:
        max_size = 0
        m = len(matrix)             #number of rows
        n = len(matrix[0])          #number of cols

        for row in range(m):
            print()
            for col in range(n):
                if matrix[row][col] == "0":
                    print("0", end = " ")
                else:
                    print("1", end = " ")
        print()
        print()

        for row in range(m):
            end, curr_size = 0, 0
            start = -1
            for col in range(n):
                if matrix[row][col] == "0":
                    start = -1
                elif matrix[row][col] == "1" and start == -1:
                    print("matrix[", row, "][", col, "] == 1")
                    start = col
                    curr_size = 1
                    max_size = max(max_size, curr_size)
                elif matrix[row][col] == "1" and start != -1:
                    print("matrix[", row, "][", col, "] == 1")
                    end = col
                    print("start ", start, "end ", end)
                    #check next row
                    check_row = row + 1
                    while check_row < m and check_row-row <= end - start + 1:
                        for i in range(start, end + 1):
                            if matrix[check_row][i] != "1":
                                if i < n-2:
                                    start = i+1
                                else:
                                    start = -1
                                break
                        check_row += 1
                    if check_row-row == end - start + 1:
                        curr_size = (end - start + 1) * (end - start + 1)
                        max_size = max(max_size, curr_size)
        return max_size
                    


if __name__ == "__main__":
    lst = [["0","0","1","0"],["1","1","1","1"],["1","1","1","1"],["1","1","1","0"],["1","1","0","0"],["1","1","1","1"],["1","1","1","0"]]
    my_instance = Solution()
    max_size = my_instance.maximalSquare(lst)
    print("max_size", max_size)
