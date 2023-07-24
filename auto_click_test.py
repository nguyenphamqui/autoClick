import pyautogui, time
delay = float(input('Nhap thoi gian delay: '))
click = int(input('Nhap so lan click'))

print("de chuot vao cho can click")
print("start click in ...")
for i in range(5, 0, -1):
 print(i)
 time.sleep(1)

x,y = pyautogui.position()
for _ in range(click):
 print(x, ' - ' ,y)
 pyautogui.click(x,y)
 time.sleep(delay)


xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
aaaaaaaaaaaaaaaaaaaaaaaaa
zzzzzzzzzzzzzzzzzzz