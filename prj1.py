Python 2.7.3 (default, Apr 10 2012, 23:31:26) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import msvcrt
>>> import time
>>> 
>>> fin=10
>>> co=0
>>> a=0
>>> 
>>> print"PRESS ENTER TO START"
PRESS ENTER TO START
>>> raw_input()
s_time=time.time()
's_time=time.time()'
>>> while(1):
	key=msvcrt.getch()
	if key=='\xe0':
		co=co+1
		print"D"
		if co==fin:
			break

		
fin=10
co=0
while(1):
	key=msvcrt.getch()
	if key=='\xeo':
		co=co+1
		print"\n\t\t  S",
		if co==fin:
			break
fin=10
co=0
while(1):
	key=mscvrt.getch()
	if key=='\xe0':
		co=co+1
		print"D",
		if co==fin:
			break
print"\n"

time_elapsed=time.time()-s_time
print"\nCONGRATS YOU JUST FINISHED THE GAME!"
print"TIME ELAPSED IS%s SECS"%str(round(time_elapsed))
