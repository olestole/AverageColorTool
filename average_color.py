import sys
import cv2 as cv
import numpy as np

def average_color(image_path):
    try:
        image = cv.imread(image_path)
        b, g, r = cv.split(image)
        b_avg = int(np.average(b))
        g_avg = int(np.average(g))
        r_avg = int(np.average(r))
        average_color = (r_avg, g_avg, b_avg)
        return average_color
    except:
        print("Error: Cannot read image from given path")
        return None
    
def main():
    if (len(sys.argv[1:]) < 1): return

    res = average_color(sys.argv[1])
    if (res is not None):
        print(res)

if __name__ == '__main__':
    main()