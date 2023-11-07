#!/usr/bin/env python3

import time 
import pyautogui as pg

'''

Touch preferens System 1920x1080
By Fer-Ati

'''

def orologio_1():
	pg.click(1818,12,2)
	pg.rightClick()
	pg.click(1761,81)
	pg.click(1160,558)
	pg.click(1090,623)
	pg.click(826,671)
	pg.click(1146,812)

def volume_2():
	pg.click(1615,14)
	pg.click(1465,61)
	pg.click(1599,126)
	pg.click(1278,129)
	pg.click(1292,132)
	
def add_wid_3():
	pg.click(956,6)
	pg.rightClick()
	pg.click(1038,158)
	pg.click(1104,167)

def inser_4():
	pg.moveTo(858,699)
	pg.dragTo(1220,9,duration=1)
	pg.moveTo(1127,346)
	pg.click()
	pg.typewrite("network")
	pg.moveTo(882,402)
	pg.dragTo(1256,21,duration=1)
	pg.moveTo(850,441)
	pg.dragTo(1182,19,duration=1)
	
	pg.click(1178,305)
	add_wid_3()
	
	pg.moveTo(1127,346)
	pg.click()
	pg.typewrite("system load")
	pg.moveTo(904,384)
	pg.dragTo(1559,27,duration=1)
	pg.click(1178,305)

def apr_mod_5():
	#pg.moveTo(1263,17)
	#pg.rightClick()
	
	pg.click(1349,82)
	pg.moveTo(1146,19)
	pg.rightClick()
	pg.click(1202,73)
	pg.moveTo(1067,19)
	pg.rightClick()
	pg.click(1123,80)
	pg.moveTo(1028,20)
	pg.rightClick()
	pg.click(1092,86)

def mod_val_6():
	pg.click(851,644)
	pg.click(855,699)
	pg.click(1112,803)
	
	pg.click(1118,356)
	pg.click(1029,477)
	pg.click(1017,389)
	pg.click(1017,389)
	pg.click(1017,389)
	pg.click(1017,389)
	pg.click(895,417)
	pg.click(1053,591)
	pg.click(1007,649)
	pg.click(800,705)
	pg.click(1040,734)
	pg.click(1040,734)
	pg.click(1040,734)
	pg.click(970,628)
	pg.click(804,517)
	pg.click(1153,702)
	pg.click(955,662)
	pg.click(959,521)
	pg.click(1145,698)
	pg.click(1114,778)

	pg.click(1288,490)
	pg.click(1099,607)
	pg.click(1301,423)

if __name__ == "__main__":
	x = str(input("Avvio Tracking pixel [y,n]")).upper()
	
	if x == "Y":
		
		while True:
			x = pg.position()
			print(x)
			time.sleep(5.3)

	else:
		pass

	orologio_1()
	volume_2()
	add_wid_3()
	inser_4()
	apr_mod_5()
	mod_val_6()
	
