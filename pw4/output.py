import curses
menu = ["0. Exit",
        "1. Input students' information",
        "2. Input courses' information",
        "3. Input score for specific course",
        "4. List students' information",
        "5. List courses'  information",
        "6. List score of specific course",  
        "7. List GPA",
        "8. Sort student by GPA"]
class CursesDesign:
    def __init__(self, stdscr, university):
        self.stdscr = stdscr
        self.university = university
        curses.curs_set(0)
        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_WHITE)
        curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)

    def print_menu(self, selected_row_idx):
        self.stdscr.clear()
        h, w = self.stdscr.getmaxyx()

        for idx, row in enumerate(menu):
            x = w // 2 - len(row) // 2
            y = h // 2 - len(menu) // 2 + idx
            if idx == selected_row_idx:
                self.stdscr.attron(curses.color_pair(2))
                self.stdscr.addstr(y, x, row)
                self.stdscr.attroff(curses.color_pair(2))
            else:
                self.stdscr.attron(curses.color_pair(1))
                self.stdscr.addstr(y, x, row)
                self.stdscr.attroff(curses.color_pair(1))

        self.stdscr.refresh()

    def run(self):
        current_row_idx = 0
        self.print_menu(current_row_idx)

        while True:
            key = self.stdscr.getch()
            self.stdscr.clear()

            if key == curses.KEY_UP and current_row_idx > 0:
                current_row_idx -= 1
            elif key == curses.KEY_DOWN and current_row_idx < len(menu) - 1:
                current_row_idx += 1
            elif key == curses.KEY_ENTER or key in [10, 13]:
                if current_row_idx == 0:
                    break
                elif 1 <= current_row_idx <= 8:
                    self.handle_menu_selection(current_row_idx)
                    self.stdscr.refresh()
                    self.stdscr.getch()

            self.print_menu(current_row_idx)
            self.stdscr.refresh()

    def handle_menu_selection(self, selected_row_idx):
        if selected_row_idx == 1:
            self.university.set_students(self.stdscr)
        elif selected_row_idx == 2:
            self.university.set_courses(self.stdscr)
        elif selected_row_idx == 3:
            self.university.set_scores(self.stdscr)
        elif selected_row_idx == 4:
            self.university.list_students(self.stdscr)
        elif selected_row_idx == 5:
            self.university.list_courses(self.stdscr)
        elif selected_row_idx == 6:
            self.university.list_scores(self.stdscr)
        elif selected_row_idx == 7:
            self.university.list_GPA(self.stdscr)
        elif selected_row_idx == 8:
            self.university.sort_student(self.stdscr)
