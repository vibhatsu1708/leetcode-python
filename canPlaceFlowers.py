# Can Place Flowers
# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

def canPlaceFlowers(flowerbed, n):
    count = 0
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0:
            leftEmpty = (i == 0) or (flowerbed[i-1] == 0)
            rightEmpty = (i == len(flowerbed)-1) or (flowerbed[i+1] == 0)
            if leftEmpty and rightEmpty:
                flowerbed[i] = 1
                count += 1
    return count >= n
print(canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 2))