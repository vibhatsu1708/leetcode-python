# Flipping an Image
# Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.
# To flip an image horizontally means that each row of the image is reversed.
# For example, flipping [1,1,0] horizontally results in [0,1,1].
# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
# For example, inverting [0,1,1] results in [1,0,0].

def flipAndInvertImage (image) :
    for i in range (len(image)) :
        start = 0
        end = len(image[0])-1
        while (start < end) :
            image[i][start], image[i][end] = image[i][end], image[i][start]
            start += 1
            end -= 1
    for i in range (len(image)) :
        for j in range (len(image)) :
            if image[i][j] == 1 :
                image[i][j] = 0
            elif image[i][j] == 0 :
                image[i][j] = 1
    return image
print(flipAndInvertImage(image = [[1,1,0],[1,0,1],[0,0,0]]))