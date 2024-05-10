"""
Container with Most Water
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Input: height = [1,1]
Output: 1
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #print(height)
        max_area = 0

        area = 0
        left = 0
        right = 1
        end = False
        areas_calculated = 0
        while left < len(height) - 1:
            if height[left] < height[right]:
                area = (right - left) * height[left]
                areas_calculated += 1
            else:
                area = (right - left) * height[right]
                areas_calculated += 1
            
            right += 1
            newright = right + 1
            while (right < len(height)-1 and height[right] < height[newright]):
                right += 1
                newright += 1

            if area > max_area:
                max_area = area
            if right == len(height):
                newleft = left + 1
                while (newleft < len(height) - 1 and height[newleft] < height[left]):
                    newleft += 1
                left = newleft
                right = left
            if end:
                break

        print(areas_calculated)
        return max_area



#solution I got was 2 and 6
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #print(height)
        max_area = 0
        area = 0
        left = 0
        right = len(height) - 1
        optimal_right = 0
        areas_calculated = 0
        new_left = False
        #testing for one value of left
        while left < len(height) - 1:
            print "left is " + str(left)
            if height[left] < height[right]:
                area = (right - left) * height[left]
                areas_calculated += 1
            else:
                area = (right - left) * height[right]
                areas_calculated += 1
            
            if area > max_area:
                print "max area is from left " + str(left) + " and right " + str(right)
                max_area = area
                optimal_right = right
            #print "\nnew loop iteration, left is " + str(left) + " right is " + str(right)

            if right <= left + 1:
                #print "loop terminating, left is " + str(left) + " right is " + str(right)
                #break
                new_left = True
            if not new_left:
                newright = right - 1
                while (newright > left + 1 and height[newright] < height[right]):
                    #print "left is " + str(left) + " and newright is " + str(newright)
                    newright -= 1
            
            #print "final newright is " + str(newright)
            
            if (new_left or height[newright] <= height[right]):  #this means a better right could not be found
                newleft = left + 1
                while (newleft < len(height) - 1 and height[newleft] < height[left]):
                    newleft += 1
                left = newleft
                right = len(height) - 1
                #print "resetting left to " + str(left) + " and restart right to " + str(right)

            else:
                right = newright

                
        print(areas_calculated)
        return max_area