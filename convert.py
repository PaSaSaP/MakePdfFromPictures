#!/usr/bin/env python
import cv2 as cv

for i in range(1, 10):
    f = f'N{i}.png'
    img = cv.imread(f)
    cv.imwrite(f'N{i}.jpg', img)
