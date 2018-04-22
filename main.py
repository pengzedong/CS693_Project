import tkinter as tk
import tkinter.filedialog
from LOC import LOC
from LCOM4 import LOCM4
from CBO import CBO
from DIT import DIT
from NOC import NOC
from WMC import WMC

window = tk.Tk()
window.title('CS693 project')
window.geometry('600x800')

a = tk.Label(window, text='CS693 project', font=('Arial', 12), width=15, height=1)
a.grid(row=0,column=0)
var = tk.StringVar()

file_list = []


def get_file():
    global file_list
    file_name = ''
    in_path = tkinter.filedialog.askopenfilenames()
    # print(in_path[0])
    # print(LOC.countline(in_path[0]))
    file_list = in_path
    for i in in_path:
        file_name += i + '\n'
    var.set(file_name)
    return in_path

def medels_select_LOC():
    global file_list
    info = ''
    while file_list == []:
        get_file()
    for i in file_list:
        metrics = LOC(i,var3.get(),var4.get(),var5.get())
        metrics.count_line()
        info += str(i) + '\n' + metrics.count_line() + '\n'
    r7.config(var2.set(info))

b = tk.Button(window, text="choose file", width=15, height=1, command=get_file)
b.grid(row=1,column=0)

c = tk.Label(window, textvariable=var, width=50, height=2)
c.grid(row=2,column=0)

var2=tk.StringVar()


    # print(metrics.count_line())


def medels_select_LCOM4():
    global file_list
    info=''
    while file_list == []:
        get_file()
    for i in file_list:
        metrics = LOCM4(i)
        metrics.count_LOCM()
        info += str(i) + '\n' + metrics.count_LOCM() + '\n'
    r7.config(var2.set(info))

def medels_select_CBO():
    global file_list
    info=''
    while file_list == []:
        get_file()
    for i in file_list:
        metrics = CBO(i)
        metrics.count_CBO()
        info += str(i) + '\n' + metrics.count_CBO() + '\n'
    r7.config(var2.set(info))

def medels_select_DIT():
    global file_list
    info=''
    while file_list == []:
        get_file()
    for i in file_list:
        metrics = DIT(i,var6.get())
        metrics.count_DIT()
        info += str(i) + '\n' + metrics.count_DIT() + '\n'
    r7.config(var2.set(info))

def medels_select_NOC():
    global file_list
    info=''
    while file_list == []:
        get_file()
    for i in file_list:
        metrics = NOC(i)
        metrics.count_NOC()
        info += str(i) + '\n' + metrics.count_NOC() + '\n'
    r7.config(var2.set(info))

def medels_select_WMC():
    global file_list
    info=''
    while file_list == []:
        get_file()
    for i in file_list:
        if var7.get()==1:
            metrics = WMC(i)
            metrics.count_WMC_on()
            info += str(i) + '\n' + metrics.count_WMC_on() + '\n'
        else:
            metrics = WMC(i)
            metrics.count_WMC_off()
            info += str(i) + '\n' + metrics.count_WMC_off() + '\n'
    r7.config(var2.set(info))


r1 = tk.Radiobutton(window, text='LOC', width=15, height=1, variable=var2, command=medels_select_LOC)
r1.grid(row=3,column=0)
var3 = tk.IntVar()
var4 = tk.IntVar()
var5 = tk.IntVar()
var6 = tk.IntVar()
var7 = tk.IntVar()
r1_1 = tk.Checkbutton(window, text='LOC(Comments)', variable=var3, onvalue=1,offvalue=0,height=1, width=20,command=medels_select_LOC)
r1_1.grid(row=3,column=1)

r1_2 = tk.Checkbutton(window, text='LOC(Empty lines)', variable=var4, onvalue=1,offvalue=0,height=1, width=20,command=medels_select_LOC)
r1_2.grid(row=4,column=1)
r1_3 = tk.Checkbutton(window, text='LOC(Import)', variable=var5, onvalue=1,offvalue=0,height=1, width=20,command=medels_select_LOC)
r1_3.grid(row=5,column=1)


r2 = tk.Radiobutton(window, text='LCOM4', width=15, height=1, variable=var2, command=medels_select_LCOM4)
r2.grid(row=8,column=0)
r2 = tk.Radiobutton(window, text='CBO', width=15, height=1, variable=var2, command=medels_select_CBO)
r2.grid(row=9,column=0)
r2 = tk.Radiobutton(window, text='DIT', width=15, height=1, variable=var2, command=medels_select_DIT)
r2.grid(row=10,column=0)
r2_1 = tk.Checkbutton(window, text='DIT(Object)', variable=var6, onvalue=1,offvalue=0,height=1, width=20,command=medels_select_DIT)
r2_1.grid(row=10,column=1)

r2 = tk.Radiobutton(window, text='NOC', width=15, height=1, variable=var2, command=medels_select_NOC)
r2.grid(row=12,column=0)
r2 = tk.Radiobutton(window, text='WMC', width=15, height=1, variable=var2, command=medels_select_WMC)
r2.grid(row=13,column=0)
r2_2 = tk.Checkbutton(window, text='WMC(Constructor)', variable=var7, onvalue=1,offvalue=0,height=1, width=20,command=medels_select_WMC)
r2_2.grid(row=13,column=1)

r7 = tk.Label(window, width=50, textvariable=var2,height=25)

r7.grid(row=14,column=0)



window.mainloop()


