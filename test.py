

import cv2
import time
from Tool.GetHP import boss_hp, player_hp
from Tool.UserInput import User
from Tool.WindowsAPI import grab_screen
from Tool.Actions import take_action, restart
from Tool.Helper import pause_game
import os



action = 11
# actions = [13,13, 3,3, 7,6, 12,6, 10, 4,4]
actions = [action, action, action, action, action]
while True:
    paused = True
    paused = pause_game(paused)
    for a in actions:
        print(1)
        take_action(a)






# window_size = (0,0,1920,1017)
# station_size = (230, 230, 1670, 930)
# WIDTH = 768
# HEIGHT = 407

# hp_station = cv2.cvtColor(cv2.resize(grab_screen(station_size),(WIDTH,HEIGHT)),cv2.COLOR_BGR2GRAY)
# boss_blood = boss_hp(hp_station, 570)
# last_hp = boss_blood
# next_self_blood  = player_hp(hp_station)

# min_hp = 9

# check_point = (612, 187)
# while True:
#     hp_station = cv2.cvtColor(cv2.resize(grab_screen(window_size),(WIDTH,HEIGHT)),cv2.COLOR_BGR2GRAY)
#     # print(hp_station[401][386], " ", hp_station[401][387]," ", hp_station[401][388])
#     # station = cv2.resize(cv2.cvtColor(grab_screen(station_size), cv2.COLOR_RGBA2RGB),(WIDTH,HEIGHT))
#     next_boss_blood = boss_hp(hp_station, last_hp)
#     print(next_boss_blood)
#     # print(boss_blood)
#     # last_hp = boss_blood
#     # boss_blood = next_boss_blood
#     # print(hp_station[95][40])
#     # if(hp_station[40][95] != 56 and hp_station[300][30] > 20 and hp_station[200][30] > 20):
#     #     # print("Not in game yet")
#     #     continue
#     # next_self_blood = player_hp(hp_station)
#     # if next_self_blood - min_hp < 0 and next_self_blood - min_hp > -3:
#     #     print(next_self_blood)
#     #     min_hp = next_self_blood
#     # if next_self_blood ==9 and min_hp != 9:
#     #     print("----------------------------------------")
#     #     min_hp = 9
#     # cv2.circle(hp_station, (95, 40), 5, (255, 0, 0), 4, 1)
#     # cv2.line(hp_station,(96, 400), (666, 400), (255, 255, 255), 4, 1)
#     # print(station[187][612])
#     # cv2.imshow( "ss", hp_station)



#     if cv2.waitKey(5) & 0xFF == ord('q'):
#         break
# cv2.waitKey()# 视频结束后，按任意键退出
# cv2.destroyAllWindows()




'''
170
195
217
242
4
21
37
49
62

'''