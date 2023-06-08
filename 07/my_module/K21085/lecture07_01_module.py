import cv2
import numpy as np

REGION_WIDTH=16
REGION_HIGH=16

fgbg = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=16, detectShadows=True)
red_mask = np.full((1, 1, 3), (0,0,255), dtype=np.uint8)
white_mask = np.full((REGION_HIGH, REGION_WIDTH, 3), (255,255,255), dtype=np.uint8)

def img_imput(resized_frame):
    rows, cols, channels = resized_frame.shape
    laplacian_mask = np.zeros((rows, cols, channels), dtype=np.uint8)
    fgmask_mask = np.zeros((rows, cols, channels), dtype=np.uint8)

    frame_gray = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)
    laplacian = cv2.Laplacian(frame_gray, cv2.CV_64F) #ラプラシアン値
    for y in range(rows):
        for x in range(cols):
            if laplacian[y,x] > 10:
                laplacian_mask[y,x] = np.copy(red_mask)

    # ret, fgmask = cv2.threshold(fgbg.apply(resized_frame), 128, 255, cv2.THRESH_BINARY)
    fgmask = fgbg.apply(resized_frame)

    fgmask_mean = cv2.countNonZero(fgmask)/(rows*cols)*100
    for y in range(int(rows/REGION_HIGH)):
        for x in range(int(cols/REGION_WIDTH)):
            fgmask_sum = np.sum(fgmask[y*REGION_HIGH:(y+1)*REGION_HIGH,x*REGION_WIDTH:(x+1)*REGION_WIDTH])
            if fgmask_sum >= fgmask_mean:
                fgmask_mask[y*REGION_HIGH:(y+1)*REGION_HIGH, x*REGION_WIDTH:(x+1)*REGION_WIDTH] = np.copy(white_mask)
            print(fgmask_mean, fgmask_sum)

    # PCカメラで撮影した動画から得た画像の画素を，2つのmask画像を使って以下のように変換せよ
    # fgmask_mask画像が白，かつ，laplacian_maskが赤の場合は元の画素色を維持せよ
    # fgmask_mask画像が白，かつ，laplacian_maskが黒の場合は元の画素色を維持せよ
    # fgmask_mask画像が黒，かつ，laplacian_maskが赤の場合は赤色に変更せよ
    # fgmask_mask画像が黒，かつ，laplacian_maskが黒の場合は黒色に変更せよ
    mask_or = cv2.bitwise_or(laplacian_mask, fgmask_mask)
    masked_frame = cv2.bitwise_and(resized_frame, mask_or)
    return masked_frame