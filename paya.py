#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import datetime
import colorama as co
import subprocess as sp

spz = "-"*45

def inizio():
	t = datetime.datetime.now()
	log =f'''
	 _____              _   _   _ 
	|  ___|__ _ __     / \ | |_(_)
	| |_ / _ \ '__|   / _ \| __| |
	|  _|  __/ |     / ___ \ |_| |
	|_|  \___|_|    /_/   \_\__|_|      

	Follow My GitHub https://www.github.com/fer-ati  <3

	'''

	print(log)

	for dt in os.uname():
		print(f" [*]Sys Info [{dt}]")
	
def term_kali():
	x = "/root/.zshrc"

	with open(x,"wr") as root_tes:
		root_tes.read()
		root_tes.close()

def aptu():
	sp.run([

		f"sudo apt update"
	
	 ],shell=True)
	print("Complete Update")

def tools():
	x = "sudo apt install -y "
	lt = [
		   
		 "plank","neofetch","etherape",
		 "geany","armitage","inxi",
		 "torbrowser-launcher","snapd",
		 "gimp","inkscape"
		 
		]

	for oh in lt:
		sp.run([

			f"{x}{oh}"
		
		 ],shell=True)

		print(f"\n\n{spz}\nCompletato il tool = {oh}\n{spz}\n")

def snap_co():
	sp.run([

		f"systemctl snapd start && snap install code --classic"

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

	if os.name.upper == "POSIX":
		aptu()
		tools()
		snap_co()
	
	else:		
		try:
				
			mes_er()
		
		except:
			quit()