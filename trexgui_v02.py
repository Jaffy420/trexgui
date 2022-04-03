# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 15:28:23 2022

@author: Jaffy420
"""
import os
import configparser
import subprocess
#import GPUtil
#import psutil
from tkinter import END, Entry, Tk, Frame, Canvas, Label, PhotoImage, Text, WORD, Scale, Button, HORIZONTAL, IntVar
from tkinter import ttk

FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')
dual_mode = False

def create_config():
    if not os.path.isfile('trexgui.ini'):
        with open('trexgui.ini', 'w') as trex_config:
            trex_config.write("""[Rig_Info]
location = Enter Trex location and click Save Config
startup = Enter Windows Startup Location and click Save Config
rig_name = rig0
password = x
email = your_email@email.com

[ALPH_Config]
wallet = Enter Wallet ID and click Save Config
wallet2 = Enter Wallet ID and click Save Config
algo = blake3
pools = stratum+tcp://de.alephium.herominers.com:1199
	stratum+tcp://pool.woolypooly.com:3106
pl = 70
fan = 82
cclock =
mclock =
lock_core =
lhr_step =
lhr_mode =
lhr_tune =
lhr_interval =
intensity = 0
kernel = 0
gpu_init = 0
dag_build = 0
default_pool = 0
default_pool2 = 0
default_config2 = 0


[CFX_Config]
wallet = Enter Wallet ID and click Save Config
wallet2 = Enter Wallet ID and click Save Config
algo = octopus
pools = stratum+tcp://cfx-eu1.nanopool.org:17777
	stratum+tcp://pool.woolypooly.com:3094
pl = 70
fan = 82
cclock =
mclock =
lock_core =
lhr_step =
lhr_mode =
lhr_tune =
lhr_interval =
intensity = 0
kernel = 0
gpu_init = 0
dag_build = 0
default_pool = 0
default_pool2 = 0
default_config2 = 0

[ERGO_Config]
wallet = Enter Wallet ID and click Save Config
wallet2 = Enter Wallet ID and click Save Config
algo = autolykos2
pools = stratum+tcp://erg.2miners.com:8888
	stratum+tcp://de.ergo.herominers.com:1180
	stratum+tcp://ergo-eu1.nanopool.org:11111
	stratum+tcp://pool.woolypooly.com:3100
pl = 70
fan = 82
cclock =
mclock =
lock_core =
lhr_step =
lhr_mode =
lhr_tune =
lhr_interval =
intensity = 0
kernel = 0
gpu_init = 0
dag_build = 0
default_pool = 0
default_pool2 = 0
default_config2 = 0

[ETC_Config]
wallet = Enter Wallet ID and click Save Config
wallet2 = Enter Wallet ID and click Save Config
algo = etchash
pools = stratum+tcp://etc.2miners.com:1010
	stratum+tcp://pool.woolypooly.com:35000
pl = 70
fan = 82
cclock =
mclock =
lock_core =
lhr_step =
lhr_mode =
lhr_tune =
lhr_interval =
intensity = 0
kernel = 0
gpu_init = 0
dag_build = 0
default_pool = 0
default_pool2 = 0
default_config2 = 0

[ETH_Config]
wallet = Enter Wallet ID and click Save Config
wallet2 = Enter Wallet ID and click Save Config
algo = ethash
pools = stratum+tcp://eth.2miners.com:2020
	stratum+tcp://eu1.ethermine.org:4444
	stratum+ssl://eth-us-east.flexpool.io:5555
	stratum+http://127.0.0.1:8080
pl = 70
fan = 82
cclock =
mclock =
lock_core =
lhr_step =
lhr_mode =
lhr_tune =
lhr_interval =
intensity = 0
kernel = 0
gpu_init = 0
dag_build = 0
default_pool = 0
default_pool2 = 0
default_config2 = 0

[FIRO_Config]
wallet = Enter Wallet ID and click Save Config
wallet2 = Enter Wallet ID and click Save Config
algo = firopow
pools = stratum+tcp://firo.2miners.com:8181
	stratum+ssl://firo.mintpond.com:3005
	stratum+tcp://pool.woolypooly.com:3104
pl = 70
fan = 82
cclock =
mclock =
lock_core =
lhr_step =
lhr_mode =
lhr_tune =
lhr_interval =
intensity = 0
kernel = 0
gpu_init = 0
dag_build = 0
default_pool = 0
default_pool2 = 0
default_config2 = 0

[RVN_Config]
wallet = Enter Wallet ID and click Save Config
wallet2 = Enter Wallet ID and click Save Config
algo = kawpow
pools = stratum+tcp://rvn.2miners.com:6060
	stratum+tcp://stratum.ravenminer.com:3838
	stratum+tcp://pool.woolypooly.com:55555
pl = 70
fan = 82
cclock =
mclock =
lock_core =
lhr_step =
lhr_mode =
lhr_tune =
lhr_interval =
intensity = 0
kernel = 0
gpu_init = 0
dag_build = 0
default_pool = 0
default_pool2 = 0
default_config2 = 0

[SERO_Config]
wallet = Enter Wallet ID and click Save Config
wallet2 = Enter Wallet ID and click Save Config
algo = progpow --coin sero
pools = stratum+tcp://gongpool.com:8008
pl = 70
fan = 82
cclock =
mclock =
lock_core =
lhr_step =
lhr_mode =
lhr_tune =
lhr_interval =
intensity = 0
kernel = 0
gpu_init = 0
dag_build = 0
default_pool = 0
default_pool2 = 0
default_config2 = 0

[VBK_Config]
wallet = Enter Wallet ID and click Save Config
wallet2 = Enter Wallet ID and click Save Config
algo = progpow-veriblock
pools = stratum+tcp://vbk.luckypool.io:9501
pl = 70
fan = 82
cclock =
mclock =
lock_core =
lhr_step =
lhr_mode =
lhr_tune =
lhr_interval =
intensity = 0
kernel = 0
gpu_init = 0
dag_build = 0
default_pool = 0
default_pool2 = 0
default_config2 = 0

[VEIL_Config]
wallet = Enter Wallet ID and click Save Config
wallet2 = Enter Wallet ID and click Save Config
algo = progpow-veil
pools = stratum+tcp://pool.woolypooly.com:3098
pl = 70
fan = 82
cclock =
mclock =
lock_core =
lhr_step =
lhr_mode =
lhr_tune =
lhr_interval =
intensity = 0
kernel = 0
gpu_init = 0
dag_build = 0
default_pool = 0
default_pool2 = 0
default_config2 = 0

[ZANO_Config]
wallet = Enter Wallet ID and click Save Config
wallet2 = Enter Wallet ID and click Save Config
algo = progpowz
pools = stratum+tcp://zano.luckypool.io:8877
pl = 70
fan = 82
cclock =
mclock =
lock_core =
lhr_step =
lhr_mode =
lhr_tune =
lhr_interval =
intensity = 0
kernel = 0
gpu_init = 0
dag_build = 0
default_pool = 0
default_pool2 = 0
default_config2 = 0
""")

def create_combos(canvas, config):
    """ Create the Combo Boxes """
    wallet_list = []
    for each_section in config.sections():
        if each_section.endswith('_Config'):
            wallet_list.append(each_section)
    combo = ttk.Combobox(canvas, font=('Helvatical bold',12))
    combo['values'] = wallet_list
    combo.current(0)
    combo.place(x = 50, y = 54,
                width = 200,
                height = 35)
    combo_pools = ttk.Combobox(canvas, font=('Helvatical bold',12))
    combo_pools['values'] = config['ALPH_Config']['pools'].split('\n')
    combo_pools.current(config[combo.get()]['default_pool'])
    combo_pools.place(x = 25, y = 208,
                      width = 250,
                      height = 35)
    
    combo2 = ttk.Combobox(canvas, font=('Helvatical bold',12))
    combo2['values'] = wallet_list
    combo2.current(0)
    combo2.place(x = 600, y = 54,
                width = 200,
                height = 35)
    combo_pools2 = ttk.Combobox(canvas, font=('Helvatical bold',12))
    combo_pools2['values'] = config['ALPH_Config']['pools'].split('\n')
    combo_pools2.current(config[combo.get()]['default_pool'])
    combo_pools2.place(x = 567, y = 208,
                      width = 250,
                      height = 35)
    
    combo_pools2.configure(state='disabled')
    combo2.configure(state='disabled')
    combo_lhr = ttk.Combobox(canvas, font=('Helvatical bold',12))
    combo_lhr['values'] = ['default', 'full', 'off', 'down']
    if config[combo.get()]['lhr_mode']:
        combo_lhr.current(config[combo.get()]['lhr_mode'])
    else:
        combo_lhr.current(0)
    combo_lhr.place(x = 35, y = 285,
                      width = 75,
                      height = 35)
    return combo, combo_pools, combo_lhr, combo2, combo_pools2


def create_window():
    root = Tk()
    root.title('T-Rex Configurator v0.3')
    root.geometry("1440x600")

    my_notebook = ttk.Notebook(root)
    my_notebook.pack()

    my_frame1 = Frame(my_notebook, width=1440, height=600)
    my_frame2 = Frame(my_notebook, width=1440, height=600)

    my_frame1.pack(fill="both", expand=1)
    my_frame2.pack(fill="both", expand=1)

    my_notebook.add(my_frame1, text="Mining Config")
    my_notebook.add(my_frame2, text="Rig Config")
    
    canvas = Canvas(my_frame1,
                    bg = "#ffffff",
                    height = 600,
                    width = 1440,
                    bd = 0,
                    highlightthickness = 0,
                    relief = "ridge")
    canvas.place(x = 0, y = 0)
    
    canvas2 = Canvas(my_frame2,
                     bg = "#ffffff",
                     height = 600,
                     width = 1440,
                     bd = 0,
                     highlightthickness = 0,
                     relief = "ridge")
    canvas2.place(x = 0, y = 0)
    return root, my_frame1, my_frame2, canvas, canvas2


def read_config():
    """ Read Config """
    create_config()
    config = configparser.ConfigParser()
    config_file = 'trexgui.ini'
    config.read(config_file)
    return config, config_file


                                     
    
def create_miner_tab_lbl(canvas):
    """ Create Miner Tab Labels """
    
    progress_lbl = Label(canvas, text="", font=('Helvatical bold',12))
    progress_lbl.place(x = 930, y = 75,
                       width = 200.0,
                       height = 40) 
    return progress_lbl


def create_miner_tab_txt(canvas, config, root, combo):
    """ Create Miner Tab Text """
    root.entry0_img = entry0_img = PhotoImage(file = "img_textBox0.png")
    _ = canvas.create_image(390, 375,
                                    image = entry0_img)
    fan_txt = Entry(canvas,
                    bd = 0,
                    bg = "#dddddd",
                    highlightthickness = 0,
                    font=('Helvatical bold',12))
    
    fan_txt.place(x = 345, y = 354,
                  width = 85,
                  height = 40)
    fan_txt.insert(0, config[combo.get()]['fan'])
    
    
    
    root.entry06_img = entry06_img = PhotoImage(file = "img_textBox0.png")
    _ = canvas.create_image(570, 375,
                                    image = entry06_img)
    mclock_txt = Entry(canvas,
                    bd = 0,
                    bg = "#dddddd",
                    highlightthickness = 0,
                    font=('Helvatical bold',12))
    
    mclock_txt.place(x = 530, y = 354,
                  width = 85,
                  height = 40)
    mclock_txt.insert(0, config[combo.get()]['mclock'])
    
    root.entry1_img = entry1_img = PhotoImage(file = "img_textBox0.png")
    _ = canvas.create_image(390, 300,
                                    image = entry1_img)
    pl_txt = Entry(canvas,
                   bd = 0,
                   bg = "#dddddd",
                   highlightthickness = 0,
                   font=('Helvatical bold',12))
    
    pl_txt.place(x = 345, y = 280, 
                 width = 85,
                 height = 40)
    pl_txt.insert(0, config[combo.get()]['pl'])
    
    root.entry15_img = entry15_img = PhotoImage(file = "img_textBox0.png")
    _ = canvas.create_image(570, 300,
                                     image = entry15_img)
    cclock_txt = Entry(canvas,
                       bd = 0,
                       bg = "#dddddd",
                       highlightthickness = 0,
                       font=('Helvatical bold',12))
    
    cclock_txt.place(x = 530, y = 280, 
                     width = 85,
                     height = 40)
    cclock_txt.insert(0, config[combo.get()]['cclock'])
    
    root.entry2_img = entry2_img = PhotoImage(file = "img_textBox4.png")
    _ = canvas.create_image(278, 150,
                                    image = entry2_img)
    
    wallet_txt = Entry(canvas,
                       bd = 0,
                       bg = "#dddddd",
                       highlightthickness = 0,
                       font=('Helvatical bold',12))
    
    wallet_txt.insert(0, config[combo.get()]['wallet'])
    
    wallet_txt.place(x = 25, y = 130,
                     width = 469.0,
                     height = 40)
    
    root.entry99_img = entry99_img = PhotoImage(file = "img_textBox4.png")
    wallet2 = canvas.create_image(830, 150,
                                    image = entry99_img)
    
    wallet_txt2 = Entry(canvas,
                       bd = 0,
                       bg = "#dddddd",
                       highlightthickness = 0,
                       font=('Helvatical bold',12))
    
    wallet_txt2.insert(0, config[combo.get()]['wallet'])
    
    wallet_txt2.place(x = 570, y = 130,
                     width = 469.0,
                     height = 40)
    
    root.entry3_img = entry3_img = PhotoImage(file = "img_textBox5.png")
    _ = canvas.create_image(718.5, 480,
                                    image = entry3_img)
    bat_txt = Text(canvas,
                   bd = 0,
                   bg = "#dddddd",
                   highlightthickness = 0,
                   font=('Helvatical bold',12),
                   wrap=WORD)
    
    bat_txt.place(x = 51.5, y = 460,
                  width = 1334.0,
                  height = 40)
    wallet_txt2.configure(state='disabled')
    return fan_txt, pl_txt, wallet_txt, bat_txt, cclock_txt, mclock_txt, wallet2, wallet_txt2


def create_miner_tab_txt2(canvas, config, root, combo):    
    root.entry21_img = entry21_img = PhotoImage(file = "img_textBox0.png")
    _ = canvas.create_image(730, 300,
                                    image = entry21_img)
    lock_core_txt = Entry(canvas,
                   bd = 0,
                   bg = "#dddddd",
                   highlightthickness = 0,
                   font=('Helvatical bold',12))
    
    lock_core_txt.place(x = 690, y = 280, 
                 width = 85,
                 height = 40)
    lock_core_txt.insert(0, config[combo.get()]['lock_core'])
    
    root.entry200_img = entry200_img = PhotoImage(file = "img_textBox0.png")
    _ = canvas.create_image(230, 302,
                                      image = entry200_img)
    lhr_step_txt = Entry(canvas,
                    bd = 0,
                    bg = "#dddddd",
                    highlightthickness = 0,
                    font=('Helvatical bold',12))
    
    lhr_step_txt.place(x = 190, y = 280,
                  width = 85,
                  height = 40)
    lhr_step_txt.insert(0, config[combo.get()]['lhr_step'])
    
    root.entry202_img = entry202_img = PhotoImage(file = "img_textBox0.png")
    _ = canvas.create_image(75, 375,
                                      image = entry202_img)
    lhr_interval_txt = Entry(canvas,
                    bd = 0,
                    bg = "#dddddd",
                    highlightthickness = 0,
                    font=('Helvatical bold',12))
    
    lhr_interval_txt.place(x = 35, y = 354,
                  width = 85,
                  height = 40)
    lhr_interval_txt.insert(0, config[combo.get()]['lhr_interval'])
    
    root.entry201_img = entry201_img = PhotoImage(file = "img_textBox0.png")
    _ = canvas.create_image(230, 375,
                                      image = entry201_img)
    lhr_tune_txt = Entry(canvas,
                    bd = 0,
                    bg = "#dddddd",
                    highlightthickness = 0,
                    font=('Helvatical bold',12))
    
    lhr_tune_txt.place(x = 190, y = 354,
                  width = 85,
                  height = 40)
    lhr_tune_txt.insert(0, config[combo.get()]['lhr_tune'])
    
    return lock_core_txt, lhr_step_txt, lhr_interval_txt, lhr_tune_txt


def help_box(canvas, config, root, combo):
    """ Create Help Box """
    help_txt = Text(canvas,
                   bd = 0,
                   bg = "#dddddd",
                   highlightthickness = 0,
                   font=('Helvatical bold',12),
                   wrap=WORD)
    
    help_txt.place(x = 850, y = 200,
                  width = 250,
                  height = 200)
    return help_txt


def create_miner_tab_buttons(canvas, root, config, mine_save_clicked, mine_clicked, bat_clicked):
    """ Create Miner Tab Buttons """
    root.img0 = img0 = PhotoImage(file = "img0.png")
    start_mine = Button(canvas,
                        image = img0,
                        borderwidth = 0,
                        highlightthickness = 0,
                        command = mine_clicked,
                        relief = "flat")
    
    start_mine.place(x = 850, y = 510,
                     width = 250,
                     height = 59)
    
    root.img1 = img1 = PhotoImage(file = "img1.png")
    mine_config = Button(canvas,
                         image = img1,
                         borderwidth = 0,
                         highlightthickness = 0,
                         command = mine_save_clicked,
                         relief = "flat")
    
    mine_config.place(x = 550, y = 510,
                      width = 250,
                      height = 59)
    
    root.img2 = img2 = PhotoImage(file = "img2.png")
    create_bat = Button(canvas,
                         image = img2,
                         borderwidth = 0,
                         highlightthickness = 0,
                         command = bat_clicked,
                         relief = "flat")
    
    create_bat.place(x = 250, y = 510,
                      width = 250,
                      height = 59)
    
    root.stuff = stuff = PhotoImage(file = "background_nodual.png")
    background_nodual = canvas.create_image(714.0, 230.0,
                                     image=stuff) 
    root.img234 = img234 = PhotoImage(file = "background.png")
    background = canvas.create_image(714.0, 230.0,
                                     image=img234) 
    
    
    #canvas.itemconfig(background_nodual, state='hidden')
    canvas.itemconfig(background_nodual, state='hidden')
    
    return start_mine, mine_config, create_bat, background_nodual, background
    

def create_miner_tab_slides(canvas):
    """ Create Miner Tab Sliders """
    intensity = Scale(canvas, from_=0, to=25, orient=HORIZONTAL)
    intensity.place(x = 1205, y = 390)
    
    kernel = Scale(canvas, from_=0, to=5, orient=HORIZONTAL)
    kernel.place(x = 1325, y = 390)
    
    gpu_init_mode = Scale(canvas, from_=0, to=2, orient=HORIZONTAL)
    gpu_init_mode.place(x = 1205, y = 310)
    
    dag_build_mode = Scale(canvas, from_=0, to=2, orient=HORIZONTAL)
    dag_build_mode.place(x = 1325, y = 310)
    return intensity, kernel, gpu_init_mode, dag_build_mode
    

def set_default_sliders(config, combo, intensity, kernel, gpu_init_mode, dag_build_mode):
    """ Set Defulat Sliders """
    intensity.set(config[combo.get()]['intensity'])
    kernel.set(config[combo.get()]['kernel'])
    gpu_init_mode.set(config[combo.get()]['gpu_init'])
    dag_build_mode.set(config[combo.get()]['dag_build'])
    
    
def create_rig_tab_text(canvas2, config, root):
    """ Create Rig Tab Text """
    root.entry02_img = entry02_img = PhotoImage(file = "img_textBox0.png")
    _ = canvas2.create_image(75, 257,
                                      image = entry02_img)
    
    rigname_txt = Entry(canvas2,
        bd = 0,
        bg = "#dddddd",
        highlightthickness = 0)
    
    rigname_txt.place(x = 28, y = 237,
                      width = 100.0,
                      height = 40)
    rigname_txt.insert(0, config['Rig_Info']['rig_name'])
    
    root.entry12_img = entry12_img = PhotoImage(file = "img_textBox0.png")
    _ = canvas2.create_image(220, 257,
                                      image = entry12_img)
    
    password_txt = Entry(canvas2,
                         bd = 0,
                         bg = "#dddddd",
                         highlightthickness = 0)
    
    password_txt.place(x = 178, y = 237,
                       width = 100.0,
                       height = 40)
    password_txt.insert(0, config['Rig_Info']['password'])
    
    root.entry122_img = entry122_img = PhotoImage(file = "img_textBox2.png")
    _ = canvas2.create_image(175, 357,
                                      image = entry122_img)
    
    email_txt = Entry(canvas2,
                      bd = 0,
                      bg = "#dddddd",
                      highlightthickness = 0)
    
    email_txt.place(x = 25, y = 337,
                    width = 300,
                    height = 40)
    email_txt.insert(0, config['Rig_Info']['email'])
    
    root.entry22_img = entry22_img = PhotoImage(file = "img_textBox4.png")
    _ = canvas2.create_image(280, 168,
                                      image = entry22_img)
    
    location_txt = Entry(canvas2,
                         bd = 0,
                         bg = "#dddddd",
                         highlightthickness = 0)
    
    location_txt.place(x = 25, y = 147,
                       width = 480,
                       height = 40)
    location_txt.insert(0, config['Rig_Info']['location'])   
    
    root.entry32_img = entry32_img = PhotoImage(file = "img_textBox4.png")
    _ = canvas2.create_image(280, 73,
                                      image = entry32_img)

    startup_txt = Entry(canvas2,
                        bd = 0,
                        bg = "#dddddd",
                        highlightthickness = 0)

    startup_txt.place(x = 25, y = 53,
                      width = 480,
                      height = 40)
    startup_txt.insert(0, config['Rig_Info']['startup'])
    
    return rigname_txt, password_txt, location_txt, startup_txt, email_txt


def create_rig_tab_buttons(canvas2, root, rig_save_clicked):
    """ Create Rig Tab Buttons """
    root.img02 = img02 = PhotoImage(file = "img1.png")
    rig_save = Button(canvas2,
                      image = img02,
                      borderwidth = 0,
                      highlightthickness = 0,
                      command = rig_save_clicked,
                      relief = "flat")

    rig_save.place(x = 595, y = 430,
                   width = 250,
                   height = 59)

    root.background_img2 = background_img2 = PhotoImage(file = "background2.png")
    _ = canvas2.create_image(720, 175,
                             image=background_img2)


def main():
    """ Main Routine """
    def check_changed():
        """ Enable Dual Mining Mode """
        global dual_mode
        if checkbox_var.get() == 1:
            wallet_txt2.configure(state='normal')
            combo2.configure(state='normal')
            combo_pools2.configure(state='normal')
            dual_mode = True
        elif checkbox_var.get() == 0:
            wallet_txt2.configure(state='disabled')
            combo2.configure(state='disabled')
            combo_pools2.configure(state='disabled')
            dual_mode = False
        update_bat()

            
    def on_start_hover(text):
    #What you do when the mouse hovers
        help_txt.insert(1.0, text)
    
    
    def on_end_hover():
    #What to do when the mouse stops hovering
        help_txt.delete(1.0, END)
        
        
    def bat_clicked():
        
        print('{}\\trexgui.bat'.format(startup_txt.get()))
        try:
            with open('{}\\{}'.format(startup_txt.get(), 'trexgui.bat'), 'w') as bat_file:
                file_text = "{}pause".format(bat_txt.get("1.0", END))
                bat_file.write(file_text)
            explore(startup_txt.get())
        except:
            print('Unable to Open File')


    def explore(path):
        # explorer would choke on forward slashes
        path = os.path.normpath(path)
    
        if os.path.isdir(path):
            subprocess.run([FILEBROWSER_PATH, path])
        elif os.path.isfile(path):
            subprocess.run([FILEBROWSER_PATH, '/select,', os.path.normpath(path)])


    def rig_save_clicked():
        """ Save Rig Config """
        config.set('Rig_Info', 'startup', startup_txt.get())
        config.set('Rig_Info', 'location', location_txt.get())
        config.set('Rig_Info', 'rig_name', rigname_txt.get())
        config.set('Rig_Info', 'password', password_txt.get())
        config.set('Rig_Info', 'email', email_txt.get())
        with open(config_file, 'w') as configfile:
            config.write(configfile)    
        progress_lbl2.configure(text='Rig Config Updated')


    def mine_save_clicked():
        """ Save Mining Config """
        config.set(combo.get(), 'wallet', wallet_txt.get())
        config.set(combo.get(), 'fan', fan_txt.get())
        config.set(combo.get(), 'pl', pl_txt.get())
        config.set(combo.get(), 'cclock', cclock_txt.get())
        config.set(combo.get(), 'mclock', mclock_txt.get())
        config.set(combo.get(), 'lock_core', lock_core_txt.get())
        config.set(combo.get(), 'lhr_step', lhr_step_txt.get())
        config.set(combo.get(), 'lhr_interval', lhr_interval_txt.get())
        config.set(combo.get(), 'lhr_tune', lhr_tune_txt.get())
        config.set(combo.get(), 'lhr_mode', '{}'.format(combo_lhr.current()))
        config.set(combo.get(), 'intensity', '{}'.format(intensity.get()))
        config.set(combo.get(), 'kernel', '{}'.format(kernel.get()))
        config.set(combo.get(), 'gpu_init', '{}'.format(gpu_init_mode.get()))
        config.set(combo.get(), 'dag_build', '{}'.format(dag_build_mode.get()))
        config.set(combo.get(), 'default_pool', '{}'.format(combo_pools.current()))
        
        config.set(combo2.get(), 'wallet', wallet_txt2.get())
        config.set(combo2.get(), 'default_pool', '{}'.format(combo_pools2.current()))
        config.set(combo.get(), 'default_config2', '{}'.format(combo2.current()))
        with open(config_file, 'w') as configfile:
            config.write(configfile)
        progress_lbl.configure(text='{} Updated'.format(combo.get()))


    def mine_clicked():
        os.chdir(location_txt.get())
        os.system('start cmd /k {}'.format(bat_txt.get("1.0", END)))


    def changed_combo():
        """ Update Combo Change """
        wallet_txt.delete(0, END)
        wallet_txt.insert(0, config[combo.get()]['wallet'])
        wallet_txt2.delete(0, END)
        wallet_txt2.insert(0, config[combo2.get()]['wallet'])
        pl_txt.delete(0, END)
        pl_txt.insert(0, config[combo.get()]['pl'])
        fan_txt.delete(0, END) 
        fan_txt.insert(0, config[combo.get()]['fan'])
        cclock_txt.delete(0, END)
        cclock_txt.insert(0, config[combo.get()]['cclock'])
        mclock_txt.delete(0, END)
        mclock_txt.insert(0, config[combo.get()]['mclock'])
        lock_core_txt.delete(0, END)
        lock_core_txt.insert(0, config[combo.get()]['lock_core'])
        lhr_step_txt.delete(0, END)
        lhr_step_txt.insert(0, config[combo.get()]['lhr_step'])
        lhr_tune_txt.delete(0, END)
        lhr_tune_txt.insert(0, config[combo.get()]['lhr_tune'])
        lhr_interval_txt.delete(0, END)
        lhr_interval_txt.insert(0, config[combo.get()]['lhr_interval'])
        intensity.set(config[combo.get()]['intensity'])
        kernel.set(config[combo.get()]['kernel'])
        gpu_init_mode.set(config[combo.get()]['gpu_init'])
        dag_build_mode.set(config[combo.get()]['dag_build'])
        #combo2.current(config[combo.get()]['default_config2'])
        combo_pools['values'] = config[combo.get()]['pools'].split('\n')
        combo_pools.current(config[combo.get()]['default_pool'])
        combo_pools2['values'] = config[combo2.get()]['pools'].split('\n')
        combo_pools2.current(config[combo2.get()]['default_pool'])
        
        if config[combo.get()]['lhr_mode']:
            combo_lhr.current(config[combo.get()]['lhr_mode'])
        else:
            combo_lhr.current(0)
        update_bat()


    def create_binds():
        """ Create Bind Events """
        combo.bind("<<ComboboxSelected>>", lambda _ : changed_combo())
        combo_pools.bind("<<ComboboxSelected>>", lambda _ : update_bat())
        combo2.bind("<<ComboboxSelected>>", lambda _ : changed_combo())
        combo_pools2.bind("<<ComboboxSelected>>", lambda _ : update_bat())
        combo_lhr.bind("<<ComboboxSelected>>", lambda _ : update_bat())
        rigname_txt.bind("<KeyRelease>", lambda _ : update_bat())
        password_txt.bind("<KeyRelease>", lambda _ : update_bat())
        location_txt.bind("<KeyRelease>", lambda _ : update_bat())
        wallet_txt.bind("<KeyRelease>", lambda _ : update_bat())
        wallet_txt2.bind("<KeyRelease>", lambda _ : update_bat())
        pl_txt.bind("<KeyRelease>", lambda _ : update_bat())
        fan_txt.bind("<KeyRelease>", lambda _ : update_bat())
        cclock_txt.bind("<KeyRelease>", lambda _ : update_bat())
        mclock_txt.bind("<KeyRelease>", lambda _ : update_bat())
        lock_core_txt.bind("<KeyRelease>", lambda _ : update_bat())
        lhr_step_txt.bind("<KeyRelease>", lambda _ : update_bat())
        lhr_tune_txt.bind("<KeyRelease>", lambda _ : update_bat())
        lhr_interval_txt.bind("<KeyRelease>", lambda _ : update_bat())
        intensity.bind("<ButtonRelease-1>", lambda _ : update_bat())
        kernel.bind("<ButtonRelease-1>", lambda _ : update_bat())
        gpu_init_mode.bind("<ButtonRelease-1>", lambda _ : update_bat())
        dag_build_mode.bind("<ButtonRelease-1>", lambda _ : update_bat())

        #Create Help
        dag_build_mode.bind('<Enter>', lambda _ : on_start_hover('// DAG build mode.\n0 - auto,\n1 - default,\n2 - recommended for 30xx cards\n'))
        dag_build_mode.bind('<Leave>', lambda _ : on_end_hover())
        intensity.bind('<Enter>', lambda _ : on_start_hover('// Intensity used with your GPUs.\nIt can be different for each GPU,\ne.g. "intensity": "20,21.4,23"'))
        intensity.bind('<Leave>', lambda _ : on_end_hover())
        gpu_init_mode.bind('<Enter>', lambda _ : on_start_hover('// Enables DAG sequential initialization.'))
        gpu_init_mode.bind('<Leave>', lambda _ : on_end_hover())
        kernel.bind('<Enter>', lambda _ : on_start_hover('// Choose kernel for Ethash. Range from 0 to 5.'))
        kernel.bind('<Leave>', lambda _ : on_end_hover())
        fan_txt.bind('<Enter>', lambda _ : on_start_hover('// GPU fan speed % (100),\ntarget core temperature (t:65),\nor target memory temperature (tm:90).\n(Windows only)\n// "fan": "t:65",'))
        fan_txt.bind('<Leave>', lambda _ : on_end_hover())
        lhr_interval_txt.bind('<Enter>', lambda _ : on_start_hover('// LHR auto-tune time interval in minutes (default: 20).\n// Amount of time the GPU must be mining without hitting LHR locks before the miner\n// increases LHR tune value.\n"lhr-autotune-interval": 20,'))
        lhr_interval_txt.bind('<Leave>', lambda _ : on_end_hover())
        lhr_tune_txt.bind('<Enter>', lambda _ : on_start_hover('// [Ethash, Autolykos2] LHR tuning value that indicates the percentage of the full speed the miner\n// tries to achieve for LHR cards (default: -1). Range from -1 to 100.\n// -1 - auto-mode (LHR tune is set to 74 (or 68 in low power mode) for LHR cards and 0 for non-LHR)\n//  0 - disabled (use for non-LHR cards)\n// 68 - recommended starting value for most LHR cards in low power mode (see lhr-low-power)\n// 74 - recommended starting value for most LHR cards\n// Can be set for each GPU separately, e.g.\n// "lhr-tune": "0,0,74.5,0" - this will set LHR tuning value to 74.5 for the third GPU.\n"lhr-tune": -1,'))
        lhr_tune_txt.bind('<Leave>', lambda _ : on_end_hover())
        lhr_step_txt.bind('<Enter>', lambda _ : on_start_hover('// LHR auto-tune step size\n"lhr-autotune-step-size": 0.5,'))
        lhr_step_txt.bind('<Leave>', lambda _ : on_end_hover())
        lock_core_txt.bind('<Enter>', lambda _ : on_start_hover('// Specifies desired locked GPU core clock speed in MHz.\n// "lock-cclock": 1000,'))
        lock_core_txt.bind('<Leave>', lambda _ : on_end_hover())
        mclock_txt.bind('<Enter>', lambda _ : on_start_hover('// Set memory clock offset in MHz. (Windows only)\n// "mclock": 100,'))
        mclock_txt.bind('<Leave>', lambda _ : on_end_hover())
        cclock_txt.bind('<Enter>', lambda _ : on_start_hover('// Set core clock offset in MHz. (Windows only)\n// "cclock": 50,'))
        cclock_txt.bind('<Leave>', lambda _ : on_end_hover())
        pl_txt.bind('<Enter>', lambda _ : on_start_hover('// Set power limit. (Windows - in percent, Linux - in Watts)\n// "pl": 100,'))
        pl_txt.bind('<Leave>', lambda _ : on_end_hover())
        combo_lhr.bind('<Enter>', lambda _ : on_start_hover('// [Ethash, Autolykos2] LHR auto-tune mode (default: full). Valid values:\n// off  - auto-tune is disabled. LHR tune value is fixed during mining, and will not change\n//        no matter how often LHR lock is detected\n// down - LHR tune value will decrease if the miner detects LHR lock\n// full - same as "down" but additionally miner will be trying to increase LHR tune\n//        value if its stable on the current LHR tune level\n"lhr-autotune-mode": "full",'))
        combo_lhr.bind('<Leave>', lambda _ : on_end_hover())
        
        
    def update_bat():
        """ Update Bat Text """
        bat_txt.delete(1.0, END)
        if 'nanopool' in combo_pools.get():
            rigname_fix = '{}/{}'.format(rigname_txt.get(), email_txt.get())
        else:
            rigname_fix = rigname_txt.get()
        if dual_mode == True:
            if (config[combo.get()]['algo'] == 'octopus' 
                    or config[combo.get()]['algo'] == 'autolykos2' 
                    or config[combo.get()]['algo'] == 'firopow' 
                    or config[combo.get()]['algo'] == 'kawpow'):
                new_bat = '{}\\t-rex.exe -a {} --dual-algo {} -o {} -u {}.{} -p {} --url2 {} --user2 {}.{} --pass2 {}'.format(location_txt.get(),
                                                                            config[combo.get()]['algo'],
                                                                            config[combo2.get()]['algo'],
                                                                            combo_pools.get(),
                                                                            wallet_txt.get(),
                                                                            rigname_fix,
                                                                            password_txt.get(),
                                                                            combo_pools2.get(),
                                                                            wallet_txt2.get(),
                                                                            rigname_fix,
                                                                            password_txt.get())
            else:
                new_bat = '{}\\t-rex.exe -a {} --dual-algo {} -o {} -u {} -p {} -w {} --url2 {} --user2 {}.{} --pass2 {}'.format(location_txt.get(),
                                                                            config[combo.get()]['algo'],
                                                                            config[combo2.get()]['algo'],
                                                                            combo_pools.get(),
                                                                            wallet_txt.get(),
                                                                            password_txt.get(),
                                                                            rigname_fix,
                                                                            combo_pools2.get(),
                                                                            wallet_txt2.get(),
                                                                            rigname_fix,
                                                                            password_txt.get())
        else:
            if (config[combo.get()]['algo'] == 'octopus' 
                    or config[combo.get()]['algo'] == 'autolykos2' 
                    or config[combo.get()]['algo'] == 'firopow' 
                    or config[combo.get()]['algo'] == 'kawpow'):
                new_bat = '{}\\t-rex.exe -a {} -o {} -u {}.{} -p {}'.format(location_txt.get(),
                                                                            config[combo.get()]['algo'],
                                                                            combo_pools.get(),
                                                                            wallet_txt.get(),
                                                                            rigname_fix,
                                                                            password_txt.get())
            else:
                new_bat = '{}\\t-rex.exe -a {} -o {} -u {} -p {} -w {}'.format(location_txt.get(),
                                                                               config[combo.get()]['algo'],
                                                                               combo_pools.get(),
                                                                               wallet_txt.get(),
                                                                               password_txt.get(),
                                                                               rigname_fix)
        if pl_txt.get() != '' and pl_txt.get() != '0':
            new_bat = '{} --pl {}'.format(new_bat, pl_txt.get())
        if fan_txt.get() != '' and fan_txt.get() != '0':
            new_bat = '{} --fan {}'.format(new_bat, fan_txt.get())
        if intensity.get() != 0:
            new_bat = '{} -i {}'.format(new_bat, intensity.get())
        if kernel.get() != 0:
            new_bat = '{} --kernel {}'.format(new_bat, kernel.get())
        if gpu_init_mode.get() != 0:
            new_bat = '{} --gpu_init_mode {}'.format(new_bat, gpu_init_mode.get())
        if dag_build_mode.get() != 0:
            new_bat = '{} --dag_build_mode {}'.format(new_bat, dag_build_mode.get())
        if cclock_txt.get() != '' and cclock_txt.get() != '0':
            new_bat = '{} --cclock {}'.format(new_bat, cclock_txt.get())
        if mclock_txt.get() != '' and mclock_txt.get() != '0':
            new_bat = '{} --mclock {}'.format(new_bat, mclock_txt.get())
        if lock_core_txt.get() != '' and lock_core_txt.get() != '0':
            new_bat = '{} --lock-cclock {}'.format(new_bat, lock_core_txt.get())
        if lhr_step_txt.get() != '' and lhr_step_txt.get() != '0':
            new_bat = '{} --lhr-autotune-step-size {}'.format(new_bat, lhr_step_txt.get())
        if lhr_interval_txt.get() != '' and lhr_interval_txt.get() != '0':
            new_bat = '{} --lhr-autotune-interval {}'.format(new_bat, lhr_interval_txt.get())
        if lhr_tune_txt.get() != '' and lhr_tune_txt.get() != '0':
            new_bat = '{} --lhr-tune {}'.format(new_bat, lhr_tune_txt.get())
        if combo_lhr.get() != 'default':
            new_bat = '{} --lhr-autotune-mode {}'.format(new_bat, combo_lhr.get())
        bat_txt.insert(1.0, new_bat)
    
    
    
    root, my_frame1, my_frame2, canvas, canvas2 = create_window()
    config, config_file = read_config()
    combo, combo_pools, combo_lhr, combo2, combo_pools2 = create_combos(canvas, config)
    progress_lbl = create_miner_tab_lbl(canvas)
    
    
    
    
    
    fan_txt, pl_txt, wallet_txt, bat_txt, cclock_txt, mclock_txt, wallet2, wallet_txt2  = create_miner_tab_txt(canvas, config, root, combo)
    lock_core_txt, lhr_step_txt, lhr_interval_txt, lhr_tune_txt = create_miner_tab_txt2(canvas, config, root, combo)
    start_mine, mine_config, create_bat, background_nodual, background = create_miner_tab_buttons(canvas, root, config, mine_save_clicked, mine_clicked, bat_clicked)
    intensity, kernel, gpu_init_mode, dag_build_mode = create_miner_tab_slides(canvas)
    set_default_sliders(config, combo, intensity, kernel, gpu_init_mode, dag_build_mode)
    
    help_txt = help_box(canvas, config, root, combo)
    
    
    checkbox_var= IntVar()
    checkbox =ttk.Checkbutton(canvas,
                #text='',
                variable=checkbox_var,
                command=check_changed)
    
    checkbox.place(x = 400, y = 50)
    progress_lbl2 = create_miner_tab_lbl(canvas2)
    rigname_txt, password_txt, location_txt, startup_txt, email_txt = create_rig_tab_text(canvas2, config, root)
    create_rig_tab_buttons(canvas2, root, rig_save_clicked)
    
    update_bat()
    create_binds()
    
    #GPUs = GPUtil.getGPUs()
    #for GPU in GPUs:
    #    print('{} {}'.format(GPU.name, GPU.memoryTotal))
    #print(psutil.virtual_memory()[0]/1024/1024/1024)
    root.mainloop()


main()