class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        #doesn't pass all test cases and doesn't implement a stack
        i = len_a = len(asteroids) - 1
        result = []
        #reverse traverse
        while i > 0:
            print (asteroids[i], asteroids[i-1])
            print (asteroids)
            if asteroids[i] < 0 and asteroids[i-1] > 0:
                if -asteroids[i] > asteroids[i-1]:
                    asteroids[i-1] = asteroids[i]
                elif -asteroids[i] == asteroids[i-1]:
                    asteroids.pop(i-1)
                    asteroids.pop(i-1)
                    i -= 1
                    continue
                asteroids.pop(i)
            elif asteroids[i] > 0 and asteroids[i-1] < 0:
                if asteroids[i] > -asteroids[i-1]:
                    asteroids[i-1] = asteroids[i]
                elif asteroids[i] == -asteroids[i-1]:
                    asteroids.pop(i-1)
                    asteroids.pop(i-1)
                    i -= 1
                    continue
                asteroids.pop(i)
            elif asteroids[i] == asteroids[i-1]:
                asteroids.pop(i)

                
            i -= 1

        return asteroids