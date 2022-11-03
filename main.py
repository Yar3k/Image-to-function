import functions
import cv2

def main():
    """ Test functions """
    img = functions.image_reader("test.jpg")
    rez = functions.image_hsplit(img, 16)
    idx = 0
    for r in rez:
        cv2.imwrite(str(idx) + "split.png",r)
        idx+=1

    print(functions.arr_rounder(rez))
    return 0

if __name__ == "__main__":
    main()