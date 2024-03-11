from input import *
from output import *
import curses
from curses import wrapper

def main(stdscr):
    uni = University()
    curses_design = CursesDesign(stdscr, uni)
    curses_design.run()
curses.wrapper(main)