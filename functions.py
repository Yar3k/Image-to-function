import cv2
import numpy as np

#Returns [H x W x RGB]
def image_reader(path):
    return [np.array(cv2.imread(path))]

'''
Starts splitting horizontally
Returns in order: [1, 3]
                  [2, 4]
'''
def image_hsplit(img_arr, splitter):
    new_arr = []
    if splitter == 1:
        return img_arr

    for part in img_arr:
        spl = np.array_split(part, 2, axis=1)
        new_arr.append(spl[0])
        new_arr.append(spl[1])
    
    return image_vsplit(new_arr, splitter/2)

'''
Starts splitting vertically
Returns in order: [1, 2]
                  [3, 4]
'''
def image_vsplit(img_arr, splitter):
    new_arr = []
    if splitter == 1:
        return img_arr
        
    for part in img_arr:
        spl = np.array_split(part, 2, axis=0)
        new_arr.append(spl[0])
        new_arr.append(spl[1])
    
    return image_hsplit(new_arr, splitter/2)

#Returns rounded list of each split (RGB)
def arr_rounder(splits):
    result = []
    for split in splits:
        result.append(np.average(split, axis=(0, 1)))
    return result
