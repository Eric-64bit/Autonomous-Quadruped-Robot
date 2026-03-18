from sense_hat import SenseHat
import time

sense = SenseHat()

# 设置要显示的文字
text = "Hello world! "
# 设置文字颜色 (RGB)
text_color = (0, 255, 255)  # 青色
back_color = (0, 0, 0)      # 背景黑色

# 无限循环显示

sense.show_message(text, scroll_speed=0.05, text_colour=text_color, back_colour=back_color)

