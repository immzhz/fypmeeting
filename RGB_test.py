
#说明：RGB IED灯传感器实验

import RPi.GPIO as GPIO
import time
colors = [0xFF0000, 0x00FF00, 0x0000FF, OxFFFF00, OxFPOOFF, OxOOFFFF]
makerobo_R = 11
makerobo_G = 12
makerobo_B = 13
＃初始化程序
def makerobo setup(Rpin, Gpin, Bpin):
  global pins
  global p_R, p_G, p_B
  pins = {'pin_R': Rpin, 'pin_G': Gpin, 'pin_B': Bpin]
  GPIO. setmode (GPIO. BOARD)  ＃采用实际的物理引脚给 GPIO口
  GPIO.setwarnings (False) ＃去除 GPIO 口警告
  for i in pins:
      GPIO. setup (pins[i], GPIO.OUT) ＃设置 pin 模式为输出模式
      GPIO.output (pins[i], GPIO.LOW） ＃由于RGB 三色模块的每个 IE口 灯达到不同亮度所需的电流值是不同的，因此设置的频率也不同
  p_R= GPIO.PWM(pins ['pin_R']. 2000) ＃ 设置频率为 2k日z
  p_G = GPIO. PWM (pins ['pin_G'], 1999)
  p_B = GPIO. PWM (pins['pin_B'], 5000) ＃ 初始化占空比为0(IED 灯熄灭）
  p_R.start (0)
  p_G.start (0)
  p_B.start(0) ＃按比例缩放函数
def makerobo_pwm_map (x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

＃熄灭 RGB LED灯
def makerobo_ off() :
  GPIO.setmode (GPIO.BOARD) # 采用实际的物理引脚给 GPIO 口
  for i in pins: ＃设置 pin 模式为输出模式
    GPIO.setup(pins[i], GPIO.OUT)
    GPIO.output(pins[i], GPIO.LOW)
                                                   
def makerobo_set_Color(col):
  R_val = (col & 0xff0000) >> 16
  G_va = (col & 0x00ff00) >> 8
  B_val = (col & 0x0000ff) >> 0
  #将0~255 同比例缩小到 0~100
  R_val = makerobo_pwm_map(R_val, 0, 255, 0, 100)
  G_val = makerobo_pwm map (G_val, 0, 255, 0, 100)
  B_val = makerobo_pwm map (B_val, 0, 255, 0, 100)

  p_R. ChangeDutyCycle (100-R_val)
  p_G. ChangeDutyCycle (100-G_val)
  p_B. ChangeDutyCycle (100-B_val)
＃循环函数
def makerobo_loop() :
  while True:
    for col in colors:
      makerobo_set_Color (col)
      time.sleep (1)
＃资源释放
def makerobo_destroy () :
  p_R.stop ()
  p_G.stop ()
  P_B.stop ()
  makerobo_off ()
  GPIO.cleanup ()
＃程序入口
if__name__== "__main__":
    try:  
      makerobo_ setup(makerobo_R, makerobo_G, makerobo_B） 
      makerobo_loop ()

    except KeyboardInterrupt:
      makerobo_destroy ()

