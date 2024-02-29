import cv2
import numpy as np
def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transposed = []
    for j in range(cols):
        row = []
        for i in range(rows):
            row.append(matrix[i][j])
        transposed.append(row)
    
    return transposed

def flip(matrix, flipCode):
    rows = len(matrix)
    cols = len(matrix[0])

    flipped = []
    for i in range(rows):
        row = []
        for j in range(cols):
            if flipCode == 0:
                row.append(matrix[rows-i-1][j])   # 沿x轴翻转
            elif flipCode > 0: 
                row.append(matrix[i][cols-j-1])   # 沿y轴翻转
            else:
                row.append(matrix[rows-i-1][cols-j-1]) # 沿原点翻转
        flipped.append(row)
        
    return flipped

def rotate_matrix(src, angle):
    if angle == 90:
        # dst = cv2.transpose(src)
        # dst = cv2.flip(dst, 1)
        dst = transpose(src)
        dst = flip(dst, 1)
    
    elif angle == 180:
        # dst = cv2.flip(src, -1)
        dst = flip(src, -1)

        
    elif angle == 270:
        # dst = cv2.transpose(src)
        # dst = cv2.flip(dst, 0)
        dst = transpose(src)
        dst = flip(dst, 0)

    else:
        dst = src
    return dst


M = np.array([[1, 2, 3], 
              [4, 5, 6],
              [7, 8, 9]], dtype=np.float32)

# 矩阵旋转  
M90 = rotate_matrix(M, 90)
M180 = rotate_matrix(M, 180)
M270 = rotate_matrix(M, 270)

# 输出结果
print('Original matrix:\n', M)
print('Matrix rotated 90 degrees:\n', M90)
print('Matrix rotated 180 degrees:\n', M180) 
print('Matrix rotated 270 degrees:\n', M270)