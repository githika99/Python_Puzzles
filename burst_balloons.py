def findMinArrowShots(points):
        #combine the ranges 
        if not points:
            return 0
        points.sort()
        print(points)
        new_ranges = [points[0]]
        output = len_p = len(points)

        i = 1
        while i < len_p:
            if points[i][0] <= points[i-1][1]:
                #wrote it like this to make it clearer to understand
                points[i-1]= [points[i-1][0], max(points[i][1], points[i-1][1])]   
                points.remove(points[i])
                i -= 1
                len_p -= 1
                output -= 1
            i += 1
        
        return output

if __name__ == "__main__":
     print(findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))