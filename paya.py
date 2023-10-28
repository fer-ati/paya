#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os,random
import time,datetime
import colorama as co
import subprocess as sp

spz = "-"*45
okkey = co.Fore.GREEN + "✓" + co.Fore.RESET
col_li = [
	
	co.Fore.RED,co.Fore.BLUE,
	co.Fore.YELLOW,co.Fore.CYAN,
	co.Fore.MAGENTA,co.Fore.GREEN
		  
 ] 

def inizio():
	t = datetime.datetime.now()
	st = "\n"*25
	log =f'''
	 _____              _   _   _ 
	|  ___|__ _ __     / \ | |_(_)
	| |_ / _ \ '__|   / _ \| __| |
	|  _|  __/ |     / ___ \ |_| |
	|_|  \___|_|    /_/   \_\__|_|      

	Follow My GitHub https://www.github.com/fer-ati  <3

	'''

	print(random.choice(col_li),log,co.Fore.RESET)
	print(f"\n {spz}\n\n")

	for dt in os.uname():
		print(f" [*]Sys Info [{dt}]")

	time.sleep(1.3)
	print(f"\n\n {spz}{st}")
	
	sp.run([

		f"figlet Python3"

	 ],shell=True),print("\n"*14)
	time.sleep(3.2)

def aptu():
	sp.run([

		f"sudo apt update"
	
	 ],shell=True)
	print("Complete Update")

def tools():
	x = "sudo apt install -y "
	lt = [
		   
		 "plank","bleachbit","etherape",
		 "geany","armitage","inxi",
		 "torbrowser-launcher","snapd",
		 "gimp","inkscape","neofetch"
		 
		]

	for oh in lt:
		sp.run([

			f"{x}{oh}"
		
		 ],shell=True)

		print(f"\n\n{spz}\n\n[{okkey}] Completato il tool = {oh}\n\n{spz}\n")

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
	
	else:		
		try:
				
			mes_er()
		
		except:
			quit()
