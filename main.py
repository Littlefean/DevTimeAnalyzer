from datetime import datetime
from typing import List, Tuple
from pynput import keyboard
from PIL import Image, ImageDraw
import time

from color_map import COLOR_MAP


class CodeActivityTracker:
    WIDTH_PRE_SECOND = 1  # 每秒多少个px
    IMG_HEIGHT = 30  # px
    BG_COLOR = "black"  # 黑色表示背景，一般深色背景是程序员的护眼习惯。
    KEY_ACTIVE_COLOR = "white"

    def __init__(self):
        self.activity_log: List[Tuple[float, keyboard.Key]] = []
        self.is_tracking = False
        self.listener = None  # 用于存储监听器对象

    def on_press(self, key):
        if self.is_tracking:
            self.activity_log.append((time.time(), key))

    def start_tracking(self):
        self.is_tracking = True
        self.activity_log = []  # 清空之前的记录
        print("开始记录...")
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()

    def stop_tracking(self):
        if self.is_tracking:
            self.is_tracking = False
            print("结束记录...")
            if self.listener:
                self.listener.stop()
                self.listener.join()  # 确保监听器已经停止

    def generate_activity_image(self):
        activity_duration = 1  # 活动状态持续时间（秒）
        if len(self.activity_log) == 0:
            print("没有按键记录，无法生成图片")
            return
            # 计算总时长和初始化画布
        total_duration = int(max(self.activity_log[-1][0] - self.activity_log[0][0] + activity_duration, 1))
        image_width = total_duration * self.WIDTH_PRE_SECOND

        image = Image.new("RGB", (image_width, self.IMG_HEIGHT), color=self.BG_COLOR)
        draw = ImageDraw.Draw(image)

        # 在画布上绘制活动状态
        for timestamp, key in self.activity_log:
            start_pixel = int((timestamp - self.activity_log[0][0]) * self.WIDTH_PRE_SECOND)
            end_pixel = min(start_pixel + int(activity_duration * self.WIDTH_PRE_SECOND), image_width)
            fill_color = COLOR_MAP.get(key, self.KEY_ACTIVE_COLOR)

            draw.rectangle([start_pixel, 0, end_pixel, self.IMG_HEIGHT], fill=fill_color)

        # 保存图片
        now = datetime.now()
        image.save(f"out/{now.year}_{now.month}_{now.day}_{now.hour}_{now.minute}_{now.second}.png")
        print("活动状态图像已保存图片")


def main():
    tracker = CodeActivityTracker()

    while True:
        num = input('输入1：开始记录，输入2：结束记录并保存图片，输入3：退出程序\n')

        if num == '1':
            tracker.start_tracking()  # 启动记录
        elif num == '2':
            tracker.stop_tracking()  # 结束记录
            tracker.generate_activity_image()  # 生成图像
        elif num == '3':
            break  # 退出程序
        else:
            print('无效输入，请重新输入。')


if __name__ == "__main__":
    main()
