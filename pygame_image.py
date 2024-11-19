import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()

    # 背景画像の読み込み
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_width = bg_img.get_width()

    # こうかとん画像の読み込みと反転
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_rct = kk_img.get_rect()
    kk_rct.center = (300, 200)

    # 背景の初期位置
    bg_x = 0
    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        # 押下キーの取得
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]: 
            kk_rct.move_ip(0, -1)
        if key_lst[pg.K_DOWN]: 
            kk_rct.move_ip(0, 1)
        if key_lst[pg.K_LEFT]: 
            kk_rct.move_ip(-1, 0)
        if key_lst[pg.K_RIGHT]: 
            kk_rct.move_ip(1, 0)

        # 背景を右から左に移動
        bg_x = (bg_x - 1) % bg_width  # ループ処理

        # 背景の描画
        screen.blit(bg_img, [bg_x - bg_width, 0])  # 左側の背景
        screen.blit(bg_img, [bg_x, 0])  # 右側の背景

        # こうかとんの描画
        screen.blit(kk_img, kk_rct)

        # 画面更新
        pg.display.update()
        tmr += 1
        clock.tick(200)  # FPSを200に設定

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()