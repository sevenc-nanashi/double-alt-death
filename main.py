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
import tkinter as tk
from tkinter import ttk
from threading import Thread
from functools import partial
modes=["突然の死","空白","全角空白"]
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

while True:
    time.sleep(0.01)
    if keyboard.is_pressed('right alt'):
        while keyboard.is_pressed('right alt'):
            pass
        t_end = time.time() + 0.1
        while time.time() < t_end:
            if keyboard.is_pressed('right alt'):
                cb=pyperclip.paste()
                if cb != "":
                    
                    try:
                        if keyboard.is_pressed('right shift'):
                            root = tk.Tk()
                            root.attributes("-topmost", True)
                            root.title(u"Double Alt Death")
                            root.iconbitmap('./alt_death.ico')
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
                        pyperclip.copy(sd)
                            
                    except Exception as e:
                        raise e
                    last_time=time.time()
                    last_cb=cb
                break
        while keyboard.is_pressed('right alt'):
            pass

