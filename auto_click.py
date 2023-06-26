import pyautogui
import time
import threading
from pynput.keyboard import Listener, KeyCode

delay = 0.001 
button = pyautogui.PRIMARY # Nút chuột để click (PRIMARY hoặc SECONDARY)
start_stop_key = KeyCode(char='s')
exit_key = KeyCode(char='e')

class ClickMouse(threading.Thread):
 def __init__(self, delay, button):
  super(ClickMouse, self).__init__()
  self.delay = delay
  self.button = button
  self.running = False
  self.program_running = True

def start_clicking(self):
 self.running = True

def stop_clicking(self):
 self.running = False

def exit(self):
 self.stop_clicking()
 self.program_running = False

def run(self):
 while self.program_running:
  while self.running:
   pyautogui.click(self.button) # Click chuột ở vị trí hiện tại của con trỏ
time.sleep(self.delay)
time.sleep(0.1)

mouse = pyautogui.Controller() # Tạo một đối tượng để điều khiển chuột
click_thread = ClickMouse(delay, button) # Tạo một luồng để click chuột
click_thread.start()

def on_presskey():
 if key == start_stop_key:
  if click_thread.running:
   click_thread.stop_clicking() # Dừng click chuột nếu đang click
  else:
   click_thread.start_clicking() # Bắt đầu click chuột nếu không đang click
 elif key == exit_key:
  click_thread.exit() # Thoát khỏi chương trình
  listener.stop() # Dừng lắng nghe sự kiện bàn phím

 with Listener(on_press=on_press) as listener: # Tạo một đối tượng để lắng nghe sự kiện bàn phím
  listener.join() # Chờ cho đến khi listener dừng lại