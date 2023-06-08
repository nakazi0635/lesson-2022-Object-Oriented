import numpy as np
import cv2
import my_module.K21085.lecture07_01_module as my_module



def lecture07_01():

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while(True):
        # PCカメラで撮影した動画（画像を一定間隔ごとに撮影し640x480にリサイズしたもの）から，勾配計算をした画像(laplacian_mask)と背景差分計算をした画像(fgmask_mask)を作成せよ
        # ここから52行目までの一連の処理でlaplacian_maskとfgmask_maskを作成する
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (640, 480))

        masked_frame = my_module.img_imput(resized_frame)
        cv2.imshow('frame', masked_frame)

        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break # 'ESC' key is pressed
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # print(dir(test))
    lecture07_01()