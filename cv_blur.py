# -*- coding = utf-8 -*-
"""
cv.blur 是否 in-place?
default 并非 in-place; 若欲 in-place, 设置 function_blue(a, ksize, dst=a)
"""
import cv2 as cv
import numpy as np
if __name__ == '__main__':
    a = np.zeros((3,3), dtype=np.uint8)
    a[1,1] = 5
    b = cv.medianBlur(a, 3)
    c = cv.GaussianBlur(a, ksize=(3,3), sigmaX=0)
    print(a) # [[0 0 0], [0 5 0], [0 0 0]]
    print(b) # [[0 0 0], [0 0 0], [0 0 0]]
    print(c) # [[1 1 1], [1 1 1], [1 1 1]]
    cv.medianBlur(a, 3, dst=a)
    print(a) # [[0 0 0], [0 0 0], [0 0 0]]