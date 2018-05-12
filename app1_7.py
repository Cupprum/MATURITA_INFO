import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel(root)
    riesenie7_support.init(root, top)
    root.mainloop()


w = None


def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel(root)
    top = New_Toplevel(w)
    riesenie7_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_New_Toplevel():
    global w
    w.destroy()
    w = None


class New_Toplevel:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 

        top.geometry("901x818+529+144")
        top.title("New Toplevel")
        top.configure(height="580")
        top.configure(highlightcolor="black")
        top.configure(width="740")



        self.can39 = Canvas(top)
        self.can39.place(relx=0.11, rely=0.06, relheight=0.59, relwidth=0.72)
        self.can39.configure(borderwidth="2")
        self.can39.configure(relief=RIDGE)
        self.can39.configure(selectbackground="#c4c4c4")
        self.can39.configure(width=640)

        self.Entry1 = Entry(top)
        self.Entry1.place(relx=0.11, rely=0.67,height=41, relwidth=0.41)
        self.Entry1.configure(background="white")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(selectbackground="#c4c4c4")

        self.Button1 = Button(top)
        self.Button1.place(relx=0.6, rely=0.67, height=37, width=197)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(text='''Enter''')


if __name__ == '__main__':
    vp_start_gui()
