# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 15:28:23 2022

@author: Jaffy420
"""
import os
import configparser
from tkinter import *
from tkinter import ttk


def create_config():
    if not os.path.isfile('trexgui.ini'):
        with open('trexgui.ini', 'w') as trex_config:
            trex_config.write("""[Rig_Info]
location = Enter Trex location and click Set Path ------>
startup = Enter Windows Startup Location and click Set Startup -->
rig_name = rig0
password = x

[ALPH_Config]
wallet = Enter Wallet ID and click Set Wallet ------>
algo = blake3
pools = stratum+tcp://de.alephium.herominers.com:1199
	stratum+tcp://pool.woolypooly.com:3106
pl = 70
fan = 82

[CFX_Config]
wallet = Enter Wallet ID and click Set Wallet ------>
algo = octopus
pools = stratum+tcp://cfx-eu1.nanopool.org:17777
	stratum+tcp://pool.woolypooly.com:3094
pl = 70
fan = 82

[ERGO_Config]
wallet = Enter Wallet ID and click Set Wallet ------>
algo = autolykos2
pools = stratum+tcp://erg.2miners.com:8888
	stratum+tcp://de.ergo.herominers.com:1180
	stratum+tcp://ergo-eu1.nanopool.org:11111
	stratum+tcp://pool.woolypooly.com:3100
pl = 70
fan = 82

[ETC_Config]
wallet = Enter Wallet ID and click Set Wallet ------>
algo = etchash
pools = stratum+tcp://etc.2miners.com:1010
	stratum+tcp://pool.woolypooly.com:35000
pl = 70
fan = 82

[ETH_Config]
wallet = Enter Wallet ID and click Set Wallet ------>
algo = ethash
pools = stratum+tcp://eth.2miners.com:2020
	stratum+tcp://eu1.ethermine.org:4444
	stratum+ssl://eth-us-east.flexpool.io:5555
	stratum+http://127.0.0.1:8080
pl = 70
fan = 82

[FIRO_Config]
wallet = Enter Wallet ID and click Set Wallet ------>
algo = firopow
pools = stratum+tcp://firo.2miners.com:8181
	stratum+ssl://firo.mintpond.com:3005
	stratum+tcp://pool.woolypooly.com:3104
pl = 70
fan = 82

[RVN_Config]
wallet = Enter Wallet ID and click Set Wallet ------>
algo = kawpow
pools = stratum+tcp://rvn.2miners.com:6060
	stratum+tcp://stratum.ravenminer.com:3838
	stratum+tcp://pool.woolypooly.com:55555
pl = 70
fan = 82

[SERO_Config]
wallet = Enter Wallet ID and click Set Wallet ------>
algo = progpow --coin sero
pools = stratum+tcp://gongpool.com:8008
pl = 70
fan = 82

[VBK_Config]
wallet = Enter Wallet ID and click Set Wallet ------>
algo = progpow-veriblock
pools = stratum+tcp://vbk.luckypool.io:9501
pl = 70
fan = 82

[VEIL_Config]
wallet = Enter Wallet ID and click Set Wallet ------>
algo = progpow-veil
pools = stratum+tcp://pool.woolypooly.com:3098
pl = 70
fan = 82

[ZANO_Config]
wallet = Enter Wallet ID and click Set Wallet ------>
algo = progpowz
pools = stratum+tcp://zano.luckypool.io:8877
pl = 70
fan = 82

""")

def create_combos(canvas, config):
    """ Create the Combo Boxes """
    wallet_list = []
    for each_section in config.sections():
        if each_section.endswith('_Config'):
            wallet_list.append(each_section)
    combo = ttk.Combobox(canvas)
    combo['values'] = wallet_list
    combo.current(0)
    combo.place(x = 25, y = 225,
                width = 200,
                height = 50)
    combo_pools = ttk.Combobox(canvas)
    combo_pools['values'] = config['ALPH_Config']['pools'].split('\n')
    combo_pools.current(0)
    combo_pools.place(x = 25, y = 335,
                      width = 300,
                      height = 50)
    return combo, combo_pools


def create_window():
    root = Tk()
    root.title('T-Rex Gui v 0.2')
    root.geometry("1440x1024")

    my_notebook = ttk.Notebook(root)
    my_notebook.pack()

    my_frame1 = Frame(my_notebook, width=1440, height=1024)
    my_frame2 = Frame(my_notebook, width=1440, height=1024)

    my_frame1.pack(fill="both", expand=1)
    my_frame2.pack(fill="both", expand=1)

    my_notebook.add(my_frame1, text="Mining Config")
    my_notebook.add(my_frame2, text="Rig Config")
    
    canvas = Canvas(my_frame1,
                    bg = "#ffffff",
                    height = 1024,
                    width = 1440,
                    bd = 0,
                    highlightthickness = 0,
                    relief = "ridge")
    canvas.place(x = 0, y = 0)
    
    canvas2 = Canvas(my_frame2,
                     bg = "#ffffff",
                     height = 1024,
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
    progress_lbl = Label(canvas, text="")
    progress_lbl.place(x = 700, y = 125,
                       width = 200.0,
                       height = 57)
    return progress_lbl


def create_miner_tab_lbl(canvas2):
    """ Create Miner Tab Labels """
    progress_lbl2 = Label(canvas2, text="")
    progress_lbl2.place(x = 700, y = 125,
                        width = 200.0,
                        height = 57)
    return progress_lbl2


def create_miner_tab_txt(canvas, config, root, combo):
    """ Create Miner Tab Text """
    root.entry0_img = entry0_img = PhotoImage(file = f"img_textBox0.png")
    entry0_bg = canvas.create_image(547.5, 482.5,
                                    image = entry0_img)
    fan_txt = Entry(canvas,
                    bd = 0,
                    bg = "#dddddd",
                    highlightthickness = 0)
    
    fan_txt.place(x = 490.5, y = 453,
                  width = 114.0,
                  height = 57)
    fan_txt.insert(0, config[combo.get()]['fan'])
    
    root.entry1_img = entry1_img = PhotoImage(file = f"img_textBox1.png")
    entry1_bg = canvas.create_image(547.5, 362.5,
                                    image = entry1_img)
    pl_txt = Entry(canvas,
                   bd = 0,
                   bg = "#dddddd",
                   highlightthickness = 0)
    pl_txt.place(x = 490.5, y = 333, 
                 width = 114.0,
                 height = 57)
    pl_txt.insert(0, config[combo.get()]['pl'])
    
    root.entry2_img = entry2_img = PhotoImage(file = f"img_textBox2.png")
    entry2_bg = canvas.create_image(720.0, 251.5,
                                    image = entry2_img)
    
    wallet_txt = Entry(canvas,
                       bd = 0,
                       bg = "#dddddd",
                       highlightthickness = 0)
    wallet_txt.insert(0, config[combo.get()]['wallet'])
    
    wallet_txt.place(x = 490.5, y = 222,
                     width = 459.0,
                     height = 57)
    
    root.entry3_img = entry3_img = PhotoImage(file = f"img_textBox3.png")
    entry3_bg = canvas.create_image(718.5, 639.5,
                                    image = entry3_img)
    
    bat_txt = Entry(canvas,
                    bd = 0,
                    bg = "#dddddd",
                    highlightthickness = 0)
    
    bat_txt.place(x = 51.5, y = 610,
                  width = 1334.0,
                  height = 57)
    return fan_txt, pl_txt, wallet_txt, bat_txt


def create_miner_tab_buttons(canvas, root, config, mine_save_clicked, mine_clicked):
    """ Create Miner Tab Buttons """
    root.img0 = img0 = PhotoImage(file = f"img0.png")
    start_mine = Button(canvas,
                        image = img0,
                        borderwidth = 0,
                        highlightthickness = 0,
                        command = mine_clicked,
                        relief = "flat")
    
    start_mine.place(x = 595, y = 826,
                     width = 250,
                     height = 59)
    
    root.img1 = img1 = PhotoImage(file = f"img1.png")
    mine_config = Button(canvas,
                         image = img1,
                         borderwidth = 0,
                         highlightthickness = 0,
                         command = mine_save_clicked,
                         relief = "flat")
    
    mine_config.place(x = 595, y = 737,
                      width = 250,
                      height = 59)
    
    root.background_img = background_img = PhotoImage(file = f"background.png")
    background = canvas.create_image(734.0, 311.0,
                                     image=background_img)  
    return start_mine, mine_config
     

def create_rig_tab_text(canvas2, config, root):
    """ Create Rig Tab Text """
    root.entry02_img = entry02_img = PhotoImage(file = f"img_textBox1.png")
    entry02_bg = canvas2.create_image(550.0, 482.5,
                                      image = entry02_img)
    
    rigname_txt = Entry(canvas2,
        bd = 0,
        bg = "#dddddd",
        highlightthickness = 0)
    
    rigname_txt.place(x = 490.5, y = 453,
                      width = 100.0,
                      height = 57)
    rigname_txt.insert(0, config['Rig_Info']['rig_name'])
    
    root.entry12_img = entry12_img = PhotoImage(file = f"img_textBox1.png")
    entry12_bg = canvas2.create_image(550.0, 602.5,
                                      image = entry12_img)
    
    password_txt = Entry(canvas2,
                         bd = 0,
                         bg = "#dddddd",
                         highlightthickness = 0)
    
    password_txt.place(x = 490.5, y = 573,
                       width = 100.0,
                       height = 57)
    password_txt.insert(0, config['Rig_Info']['password'])
    
    
    root.entry22_img = entry22_img = PhotoImage(file = f"img_textBox2.png")
    entry22_bg = canvas2.create_image(720.0, 362.5,
                                      image = entry22_img)
    
    location_txt = Entry(canvas2,
                         bd = 0,
                         bg = "#dddddd",
                         highlightthickness = 0)
    
    location_txt.place(x = 490.5, y = 333,
                       width = 459.0,
                       height = 57)
    location_txt.insert(0, config['Rig_Info']['location'])   
    
    root.entry32_img = entry32_img = PhotoImage(file = f"img_textBox2.png")
    entry32_bg = canvas2.create_image(720.0, 251.5,    
                                      image = entry32_img)

    startup_txt = Entry(canvas2,
                  bd = 0,
                  bg = "#dddddd",
                  highlightthickness = 0)

    startup_txt.place(x = 490.5, y = 222,
                      width = 459.0,
                      height = 57)
    startup_txt.insert(0, config['Rig_Info']['startup'])
    
    return rigname_txt, password_txt, location_txt, startup_txt


def create_rig_tab_buttons(canvas2, root, rig_save_clicked):
    """ Create Rig Tab Buttons """
    root.img02 = img02 = PhotoImage(file = f"img1.png")
    rig_save = Button(canvas2,
                 image = img02,
                 borderwidth = 0,
                 highlightthickness = 0,
                 command = rig_save_clicked,
                 relief = "flat")

    rig_save.place(x = 595, y = 826,
              width = 250,
              height = 59)

    root.background_img2 = background_img2 = PhotoImage(file = f"background2.png")
    background2 = canvas2.create_image(960.0, 292.5,
                                       image=background_img2)
    return rig_save


def main():
    """ Main Routine """
    def rig_save_clicked():
        """ Save Rig Config """
        config.set('Rig_Info', 'startup', startup_txt.get())
        config.set('Rig_Info', 'location', location_txt.get())
        config.set('Rig_Info', 'rig_name', rigname_txt.get())
        config.set('Rig_Info', 'password', password_txt.get())
        with open(config_file, 'w') as configfile:
            config.write(configfile)    
        progress_lbl2.configure(text='Rig Config Updated')


    def mine_save_clicked():
        """ Save Mining Config """
        config.set(combo.get(), 'wallet', wallet_txt.get())
        config.set(combo.get(), 'fan', fan_txt.get())
        config.set(combo.get(), 'pl', pl_txt.get())
        with open(config_file, 'w') as configfile:
            config.write(configfile)
        progress_lbl.configure(text='{} Updated'.format(config[combo.get()]))

    def mine_clicked():
        os.chdir(location_txt.get())
        os.system('start cmd /k {}'.format(bat_txt.get()))


    def changed_combo():
        """ Update Combo Change """
        wallet_txt.delete(0, END)
        wallet_txt.insert(0, config[combo.get()]['wallet'])
        pl_txt.delete(0, END)
        pl_txt.insert(0, config[combo.get()]['pl'])
        fan_txt.delete(0, END)
        fan_txt.insert(0, config[combo.get()]['fan'])
        combo_pools['values'] = config[combo.get()]['pools'].split('\n')
        combo_pools.current(0)
        update_bat()


    def update_bat():
        """ Update Bat Text """
        bat_txt.delete(0, END)
        if (config[combo.get()]['algo'] == 'octopus' 
                or config[combo.get()]['algo'] == 'autolykos2' 
                or config[combo.get()]['algo'] == 'firopow' 
                or config[combo.get()]['algo'] == 'kawpow'):
            new_bat = '{}\\t-rex.exe -a {} -o {} -u {}.{} -p {}'.format(location_txt.get(),
                                                                        config[combo.get()]['algo'],
                                                                        combo_pools.get(),
                                                                        wallet_txt.get(),
                                                                        rigname_txt.get(),
                                                                        password_txt.get())
        else:
            new_bat = '{}\\t-rex.exe -a {} -o {} -u {} -p {} -w {}'.format(location_txt.get(),
                                                                           config[combo.get()]['algo'],
                                                                           combo_pools.get(),
                                                                           wallet_txt.get(),
                                                                           password_txt.get(),
                                                                           rigname_txt.get())
        if pl_txt.get() != '':
            new_bat = '{} --pl {}'.format(new_bat, pl_txt.get())
        if fan_txt.get() != '':
            new_bat = '{} --fan {}'.format(new_bat, fan_txt.get()) 
        bat_txt.insert(0, new_bat)


    root, my_frame1, my_frame2, canvas, canvas2 = create_window()
    config, config_file = read_config()
    combo, combo_pools = create_combos(canvas, config)
    progress_lbl = create_miner_tab_lbl(canvas)
    fan_txt, pl_txt, wallet_txt, bat_txt = create_miner_tab_txt(canvas, config, root, combo)
    start_mine, mine_config = create_miner_tab_buttons(canvas, root, config, mine_save_clicked, mine_clicked)
    
    progress_lbl2 = create_miner_tab_lbl(canvas2)
    rigname_txt, password_txt, location_txt, startup_txt = create_rig_tab_text(canvas2, config, root)
    rig_save = create_rig_tab_buttons(canvas2, root, rig_save_clicked)
    
    update_bat()
    combo.bind("<<ComboboxSelected>>", lambda _ : changed_combo())
    combo_pools.bind("<<ComboboxSelected>>", lambda _ : update_bat())
    rigname_txt.bind("<KeyRelease>", lambda _ : update_bat())
    password_txt.bind("<KeyRelease>", lambda _ : update_bat())
    location_txt.bind("<KeyRelease>", lambda _ : update_bat())
    wallet_txt.bind("<KeyRelease>", lambda _ : update_bat())
    pl_txt.bind("<KeyRelease>", lambda _ : update_bat())
    fan_txt.bind("<KeyRelease>", lambda _ : update_bat())
    root.mainloop()


main()