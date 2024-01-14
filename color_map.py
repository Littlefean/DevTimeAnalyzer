from pynput import keyboard

COLOR_MAP = {
    # 特殊快捷键，用黄色表示，因为黄色代表灯泡亮了，表示聪明
    keyboard.Key.f1: (255, 214, 97),
    keyboard.Key.f2: (255, 214, 97),
    keyboard.Key.f3: (255, 214, 97),
    keyboard.Key.f4: (255, 214, 97),
    keyboard.Key.f5: (255, 214, 97),
    keyboard.Key.f6: (255, 214, 97),
    keyboard.Key.f7: (255, 214, 97),
    keyboard.Key.f8: (255, 214, 97),
    keyboard.Key.f9: (255, 214, 97),
    keyboard.Key.f10: (255, 214, 97),
    keyboard.Key.f11: (255, 214, 97),
    keyboard.Key.f12: (255, 214, 97),
    keyboard.Key.ctrl: (255, 214, 97),
    keyboard.Key.alt: (255, 214, 97),
    keyboard.Key.cmd: (255, 214, 97),  # 不能用.win，要用.cmd。


    # 删除类的 用红色表示
    keyboard.Key.backspace: (199, 84, 80),
    keyboard.Key.delete: (199, 84, 80),

    # 空格 不那么亮的白色，表示代码意义感不强
    keyboard.Key.space: (175, 177, 179),
    # TAB同理
    keyboard.Key.tab: (175, 177, 179),
    # 回车同理
    keyboard.Key.enter: (175, 177, 179),

    # 方向键类的用蓝色系表示
    keyboard.Key.left: (104, 151, 187),
    keyboard.Key.up: (104, 151, 187),
    keyboard.Key.down: (104, 151, 187),
    keyboard.Key.right: (104, 151, 187),
    keyboard.Key.end: (104, 151, 187),
    keyboard.Key.home: (104, 151, 187),
    keyboard.Key.page_up: (104, 151, 187),
    keyboard.Key.page_down: (104, 151, 187),
}
