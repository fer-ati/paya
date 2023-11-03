#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os,random
import time,datetime
import colorama as co
import subprocess as sp

spz = "-"*45
col_li = [
	
	co.Fore.RED,co.Fore.BLUE,
	co.Fore.YELLOW,co.Fore.CYAN,
	co.Fore.MAGENTA,co.Fore.GREEN
		  
 ]
 
log =f'''
	 _____              _   _   _ 
	|  ___|__ _ __     / \ | |_(_)
	| |_ / _ \ '__|   / _ \| __| |
	|  _|  __/ |     / ___ \ |_| |
	|_|  \___|_|    /_/   \_\__|_|      

	Follow My GitHub https://www.github.com/fer-ati  <3

	'''

okkey = co.Fore.GREEN + "✓" + co.Fore.RESET


def inizio():
	t = datetime.datetime.now()
	ar = 0

	print(random.choice(col_li),log,f"\n{spz}{co.Fore.RESET}\n\n")
	for dt in os.uname():
		ar += 1
		print(f" [{okkey}] Sys Info [{dt}]")

		if ar == 5:
			print(
				
				f" [{okkey}] Orario = {t.strftime('%H:%M:%S')}\n",
		 		f"[{okkey}] Data = {t.strftime('%Y/%M/%d')}\n" 
		     )
			
			break

		else:
			continue	
			
	time.sleep(1.3)
	print(f"\n\n {spz}")

def aptu():	
	sp.run([

		f"figlet Python3"

	 ],shell=True)
	time.sleep(3.2)

	sp.run([

		f"sudo apt update && clear"
	
	 ],shell=True)
	
	print(
		
		 random.choice(col_li),log,f"\n{co.Fore.RESET}\n",
		 f"\n\n{spz}\n\n[{okkey}] Update Down\n\n{spz}\n"
		 
		 )
	
	time.sleep(2.6)

def tools():
	x = "sudo apt install -y "
	y = " && "
	cl = " clear "
	lt = [
		   
		 "plank","bleachbit",
		 "geany","armitage",
		 "inxi","etherape",
		 "torbrowser-launcher",
		 "gimp","inkscape",
		 "neofetch","snapd",
		 "figlet","zenmap-kbx"
		 
		]

	for oh in lt:
		sp.run([

			f"{x}{oh}{y}{cl}"
		
		 ],shell=True)

		print(f"""
			
			{random.choice(col_li)}\n{log}{co.Fore.RESET}
			{spz}\n\n[{okkey}] Completato il tool = {oh.title()}\n\n{spz}\n
			
			""")

def snap_co():
	x = "sudo "
	sp.run([

		f"{x} systemctl start snapd && {x} snap install code --classic"

	 ],shell=True)

def mes_er():
	x = 0
	air = " "

	print("\n\n",co.Fore.RED)
	for ner in range(10):
		print(f"{air*ner} Systema Non Compatibile")
	
	print(co.Fore.RESET)
	time.sleep(1.2),quit()

if __name__ == "__main__":
	inizio()

	if os.name.upper() == "POSIX":
		aptu()
		tools()
		snap_co()
		mes_er()

	else:		
		try:
			mes_er()
		
		except:
			quit()
