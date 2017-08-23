# example taken from https://github.com/detritus429/Stopwatch-on-curses/blob/master/stopwatch.py 
import curses #, curses.wrapper
from datetime import datetime
from datetime import timedelta

currentBase=datetime.now()
currentElapsed=timedelta()
allElapsed=timedelta()
Stdscr=None

def init_stopwatch():
	global allElapsed
	global currentElapsed
	global currentBase
	currentBase=datetime.now()
	currentElapsed=timedelta()
	allElapsed=timedelta()


def pass_wrapper():
	pass

def pause_running():
		global allElapsed
		global currentElapsed
		global currentBase
		stdscr=Stdscr
		stdscr.nodelay(0)
		buttonhit.get(stdscr.getch())()
		currentBase=datetime.now()
		allElapsed=allElapsed+currentElapsed
		elapsed=timedelta()
		stdscr.nodelay(1)

buttonhit= { ord('q'): exit,
			 ord('r'): init_stopwatch,
			 ord(' '): pause_running
		   }

def button_down(stdscr):
	buttonhit.get(stdscr.getch(),pass_wrapper)()
	return True

def get_current_elapsed():
	return datetime.now()-currentBase

def curses_function(stdscr):
	global Stdscr
	Stdscr=stdscr
	curses.curs_set(0) # switch off the cursor
	stdscr.nodelay(1) # set non-blocking getch()
	stdscr.addstr(0,0,"space - Start/stop",	curses.A_REVERSE)
	stdscr.addstr(1,0,"r - Reset",curses.A_REVERSE)
	stdscr.addstr(2,0,"q - Quit", curses.A_REVERSE)
	global currentElapsed
	global allElapsed
	while(button_down(stdscr)):
		currentElapsed=get_current_elapsed()
		stdscr.addstr(10,10,str(allElapsed+currentElapsed))
		stdscr.refresh()


# start application
curses.wrapper(curses_function)
