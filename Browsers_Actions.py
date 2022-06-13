from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

#driver = webdriver.Chrome(executable_path="")
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())


#Browser action 1 > Open Web
driver.get("https://google.com")
sleep(3)

#Browser action 2 > Title
#window_title = driver.title
# print(window_title)

#Browser action 3 > Back
# driver.get("https://wikipedia.com")
# sleep(1)
# driver.back()
# sleep(1)

#Browser action 4 > Forward
# driver.forward()

#Browser action 5 > Refresh
# driver.refresh()
# sleep(2)

#Browser action 6 > Open new window and switch to it (Tab)
# driver.switch_to.new_window('tab')
# sleep(3)

#Browser action 7 > Open new window and switch to it (Window)
# driver.switch_to.new_window('window')
# driver.get("https://digikala.com")
# sleep(3)


#Browser action 8 > Current window handle
# digikala_window = driver.current_window_handle
# print('digikala handle: ' + str(digikala_window))

#Browser action 9 > All handles
# all_handles = driver.window_handles
# print('all handles: ' + str(all_handles))

#Browser action 10 > Switch
# driver.switch_to.window(all_handles[0])
# sleep(3)

#Browser action 11 > Close tab
# driver.close()
# sleep(3)

#Browser action 12 > Quite session
# driver.quit()

#Browser action 13 > Window size
# window_size = driver.get_window_size()  #{'width': 1051, 'height': 806}
# print(window_size)
# width = window_size['width']
# height = window_size['height']
# print(width)
# print(height)

#Browser action 14 > Set Window size
# driver.set_window_size(800, 600)
# sleep(1)
# size = driver.get_window_size()
# assert size['width'] == 802
# print(size)

#Browser action 15 > Get window position
# current_position = driver.get_window_position()
# print(current_position)
# sleep(2)

#Browser action 16 > Set window position
# driver.set_window_position(400,500)
# sleep(2)
# assert driver.get_window_position()['x'] == 400

#Browser action 17 > Minimize window
# driver.minimize_window()
# sleep(2)

#Browser action 18 > Maximize window
# driver.maximize_window()
# sleep(2)

#Browser action 18 > Full screen window
# driver.fullscreen_window()
# sleep(2)

