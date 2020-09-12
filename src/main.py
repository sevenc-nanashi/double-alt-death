"""
＿人人人人人人人人人人人人人人人＿
＞       Double Alt Death       ＜
＞Created by 名無し。(@MNoNamer)＜
￣^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y^Y￣
"""

import pyperclip
import unicodedata
import keyboard
import time
import math
import os
import sys
import tkinter as tk
from tkinter import ttk
from threading import Thread
from functools import partial
from PIL import Image, ImageTk
import wx.adv
import webbrowser
end_flag=False
def callback(url):
    webbrowser.open_new(url)

TRAY_TOOLTIP = 'Double Alt Death'
if os.path.exists('./alt_death.ico'):
    TRAY_ICON = './alt_death.ico'
else:
    TRAY_ICON = './src/alt_death.ico'

def create_menu_item(menu, label, func):
    item = wx.MenuItem(menu, -1, label)
    menu.Bind(wx.EVT_MENU, func, id=item.GetId())
    menu.Append(item)
    return item


class TaskBarIcon(wx.adv.TaskBarIcon):
    def __init__(self,frame):
        wx.adv.TaskBarIcon.__init__(self)
        self.myapp_frame = frame
        self.set_icon(TRAY_ICON)

    def CreatePopupMenu(self):
        menu = wx.Menu()
        create_menu_item(menu, '情報', self.menu_info)
        create_menu_item(menu, '終了', self.menu_exit)
        return menu

    def set_icon(self, path):
        icon = wx.Icon(wx.Bitmap(path))
        self.SetIcon(icon, TRAY_TOOLTIP)        

    def menu_info(self, event):
        root = tk.Tk()
        root.title(u"Double Alt Death")
        if os.path.exists('./alt_death.ico'):
            root.iconbitmap('./alt_death.ico')
        else:
            root.iconbitmap('./src/alt_death.ico')
        root.resizable(width=False, height=False)
        root.geometry('300x200')
        root.after(10, lambda: root.focus_force())
        if os.path.exists('./alt_death.png'):
            icon = ImageTk.PhotoImage(file='./alt_death.png')
        else:
            icon = ImageTk.PhotoImage(file='./src/alt_death.png')
        title_img = ttk.Label(root ,image=icon)
        title_img.pack(pady=10)
        info_label=tk.Label(root, text="作者： 名無し。(@MNoNamer)")
        info_label.bind("<Button-1>", lambda e: callback("http://www.twitter.com/mnonamer"))
        info_label.pack(anchor=tk.NW,padx=20)
        info_label=tk.Label(root, text="Github:\ngithub.com/sevenc-nanashi/double-alt-death",justify='left')
        info_label.bind("<Button-1>", lambda e: callback("http://github.com/sevenc-nanashi/double-alt-death"))
        info_label.pack(anchor=tk.NW,padx=20)
        info_label=tk.Button(root, text="OK",command=lambda: root.destroy())
        info_label.pack(side="bottom",padx=10,fill=tk.X,pady=10)  
        root.mainloop()
        

    def menu_exit(self, event):
        global end_flag
        end_flag=True
        self.myapp_frame.Close()

class My_Application(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "", size=(1,1))
        panel = wx.Panel(self)
        self.myapp = TaskBarIcon(self)
        self.Bind(wx.EVT_CLOSE, self.onClose)
    
    def onClose(self, evt):
        global end_flag
        self.myapp.RemoveIcon()
        self.myapp.Destroy()
        self.Destroy()
        sys.exit()


modes=["突然の死","空白","全角空白","濁点"]
current_mode=0
last_time=None
last_cb=""
def text_len(text):
    count = 0
    for c in text:
        count += 2 if unicodedata.east_asian_width(c) in 'FWA' else 1
    return count

def death_generator(message):
    r=list(map(lambda m: m.replace("\r","").replace("\n",""),message.split("\n")))
    ml=0
    for ir in r:
        if text_len(ir) > ml:
            ml=text_len(ir)
    header="＿"
    if ml % 2 == 0:
        header+="人"*(ml//2)
    else:
        header+="人"*math.ceil(ml//2/2)
        header+=" "    
        header+="人"*math.ceil(ml//2/2)
    header+="＿"    
    mid=""
    lr_int=text_len(header)-4
    for ir in r:
        mid+="＞"
        sc=lr_int-text_len(ir)
        if sc % 2 == 0:
            mid+=" "*(sc//2)
            mid+=ir
            mid+=" "*(sc//2)
        else:
            mid+=" "*(sc//2)
            mid+=ir
            mid+=" "*(sc//2)
            mid+=" "
        mid+="＜"+"\n"
    footer="￣"
    for fi in range(lr_int):
        footer+="^" if fi % 2 == 0 else "Y"
    return header+"\n"+mid+footer+"￣"
def launch_tray():
    MyApp = wx.App()
    My_Application()
    MyApp.MainLoop()
Thread(target=launch_tray).start()
while not end_flag:
    time.sleep(0.01)
    if keyboard.is_pressed('right alt'):
        while keyboard.is_pressed('right alt') and not end_flag:
            pass
        t_end = time.time() + 0.1
        while time.time() < t_end and not end_flag:
            if keyboard.is_pressed('right alt'):
                cb=pyperclip.paste()
                if cb != "":
                    
                    try:
                        if keyboard.is_pressed('right shift'):
                            root = tk.Tk()
                            root.attributes("-topmost", True)
                            root.title(u"Double Alt Death")
                            if os.path.exists('./alt_death.ico'):
                                root.iconbitmap('./alt_death.ico')
                            else:
                                root.iconbitmap('./src/alt_death.ico')
                            root.resizable(width=False, height=False)
                            root.after(10, lambda: root.focus_force())
                            root.bind(
                                '<FocusOut>',lambda e: root.destroy()
                            )
                            root.bind(
                                '<Return>',lambda e: root.destroy()
                            )
                            def change_mode_keyu(event):
                                global current_mode
                                current_mode-=1
                                current_mode%=len(modes)
                                combo.current(current_mode)
                            root.bind(
                                '<Up>',change_mode_keyu
                            )
                            def change_mode_keyd(event):
                                global current_mode
                                current_mode+=1
                                current_mode%=len(modes)
                                combo.current(current_mode)
                            root.bind(
                                '<Down>',change_mode_keyd
                            )  
                            combo = ttk.Combobox(root, state='readonly')
                            combo["values"] = modes
                            combo.current(current_mode)
                            def change_mode(event):
                                global current_mode
                                current_mode=modes.index(combo.get())
                                root.destroy()
                            
                            combo.bind(
                                '<<ComboboxSelected>>',change_mode
                            ) 
                            
                            combo.pack()
                                
                            Thread(target=root.mainloop()).start
                        sd=""   
                        if current_mode == 0:
                            sd = death_generator("\n".join(cb.split("\n")))
                        elif current_mode == 1:
                            sd=" ".join(list(cb))
                        elif current_mode == 2:
                            sd="　".join(list(cb))
                        elif current_mode == 3:
                            sd=""
                            for t in list(cb):
                                sd+=t+'゛'
                        pyperclip.copy(sd)
                            
                    except Exception as e:
                        raise e
                    last_time=time.time()
                    last_cb=cb
                break
        while keyboard.is_pressed('right alt'):
            pass

