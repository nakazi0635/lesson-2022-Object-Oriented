
import numpy as np
import cv2
import my_module.K21085.lecture07_01_module as test


REGION_WIDTH=16
REGION_HIGH=16

def lecture07_01():

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    fgbg = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=16, detectShadows=True)
    red_mask = np.full((1, 1, 3), (0,0,255), dtype=np.uint8)
    white_mask = np.full((REGION_HIGH, REGION_WIDTH, 3), (255,255,255), dtype=np.uint8)
    cv2.imshow('frame',red_mask)

    while(True):
        # PCカメラで撮影した動画（画像を一定間隔ごとに撮影し640x480にリサイズしたもの）から，勾配計算をした画像(laplacian_mask)と背景差分計算をした画像(fgmask_mask)を作成せよ
        # ここから52行目までの一連の処理でlaplacian_maskとfgmask_maskを作成する
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (640, 480))
        rows, cols, channels = resized_frame.shape
        # maskを定義（zeroで埋まっているのでこのままだと真っ暗）
        laplacian_mask = np.zeros((rows, cols, channels), dtype=np.uint8)
        fgmask_mask = np.zeros((rows, cols, channels), dtype=np.uint8)

        frame_gray = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)
        laplacian = cv2.Laplacian(frame_gray, cv2.CV_64F) #ラプラシアン値
        for y in range(rows):
            for x in range(cols):
                if laplacian[y,x] > 10:
                    # implement me
                    #なんでy,xを指定する必要があるのか
                    laplacian_mask[y,x] = np.copy(red_mask)

        # for debug
        # cv2.imshow('frame',laplacian, cmap='gray')
        # cv2.imshow('frame', laplacian_mask)

        ret, fgmask = cv2.threshold(fgbg.apply(resized_frame), 128, 255, cv2.THRESH_BINARY)
        # for y in range(rows):
        #     for x in range(cols):
        #         if fgmask[y,x] == 255:
        #             fgmask[y,x] = 255

        # fgmask_sum = ""
        # fgmask_mean
        fgmask_mean = cv2.countNonZero(fgmask)/(rows*cols)*100
        for y in range(int(rows/REGION_HIGH)):
            for x in range(int(cols/REGION_WIDTH)):
                fgmask_sum = np.sum(fgmask[y*REGION_HIGH:(y+1)*REGION_HIGH,x*REGION_WIDTH:(x+1)*REGION_WIDTH])
                # fgmask_mean = np.mean(fgmask[y*REGION_HIGH:(y+1)*REGION_HIGH,x*REGION_WIDTH:(x+1)*REGION_WIDTH]*100)
                # print(fgmask_sum, fgmask_mean)
                if fgmask_sum >= fgmask_mean:
                    
                # if fgmask_sum[x][y] >= fgmask_mean:
                    # implement me
                    fgmask_mask[y*REGION_HIGH:(y+1)*REGION_HIGH, x*REGION_WIDTH:(x+1)*REGION_WIDTH] = np.copy(white_mask)
                    # pass

        # for debug
        # print(white_mask)
        # print(fgmask_sum, fgmask_mean)

        # cv2.imshow('frame',fgmask_mask)

        # PCカメラで撮影した動画から得た画像の画素を，2つのmask画像を使って以下のように変換せよ
        # fgmask_mask画像が白，かつ，laplacian_maskが赤の場合は元の画素色を維持せよ
        # fgmask_mask画像が白，かつ，laplacian_maskが黒の場合は元の画素色を維持せよ
        # fgmask_mask画像が黒，かつ，laplacian_maskが赤の場合は赤色に変更せよ
        # fgmask_mask画像が黒，かつ，laplacian_maskが黒の場合は黒色に変更せよ
        mask_or = cv2.bitwise_or(laplacian_mask, fgmask_mask)
        masked_frame = cv2.bitwise_and(resized_frame, mask_or)
        cv2.imshow('frame', masked_frame)
        # cv2.imshow('frame', fgmask)

        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break # 'ESC' key is pressed
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print(dir(test))
    lecture07_01()