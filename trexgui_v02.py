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
location = Enter Trex location and click Save Config
startup = Enter Windows Startup Location and click Save Config
rig_name = rig0
password = x
email = your_email@email.com

[ALPH_Config]
wallet = Enter Wallet ID and click Save Config
algo = blake3
pools = stratum+tcp://de.alephium.herominers.com:1199
	stratum+tcp://pool.woolypooly.com:3106
pl = 70
fan = 82
cclock =
mclock =

[CFX_Config]
wallet = Enter Wallet ID and click Save Config
algo = octopus
pools = stratum+tcp://cfx-eu1.nanopool.org:17777
	stratum+tcp://pool.woolypooly.com:3094
pl = 70
fan = 82
cclock =
mclock =

[ERGO_Config]
wallet = Enter Wallet ID and click Save Config
algo = autolykos2
pools = stratum+tcp://erg.2miners.com:8888
	stratum+tcp://de.ergo.herominers.com:1180
	stratum+tcp://ergo-eu1.nanopool.org:11111
	stratum+tcp://pool.woolypooly.com:3100
pl = 70
fan = 82
cclock =
mclock =

[ETC_Config]
wallet = Enter Wallet ID and click Save Config
algo = etchash
pools = stratum+tcp://etc.2miners.com:1010
	stratum+tcp://pool.woolypooly.com:35000
pl = 70
fan = 82
cclock =
mclock =

[ETH_Config]
wallet = Enter Wallet ID and click Save Config
algo = ethash
pools = stratum+tcp://eth.2miners.com:2020
	stratum+tcp://eu1.ethermine.org:4444
	stratum+ssl://eth-us-east.flexpool.io:5555
	stratum+http://127.0.0.1:8080
pl = 70
fan = 82
cclock =
mclock =

[FIRO_Config]
wallet = Enter Wallet ID and click Save Config
algo = firopow
pools = stratum+tcp://firo.2miners.com:8181
	stratum+ssl://firo.mintpond.com:3005
	stratum+tcp://pool.woolypooly.com:3104
pl = 70
fan = 82
cclock =
mclock =

[RVN_Config]
wallet = Enter Wallet ID and click Save Config
algo = kawpow
pools = stratum+tcp://rvn.2miners.com:6060
	stratum+tcp://stratum.ravenminer.com:3838
	stratum+tcp://pool.woolypooly.com:55555
pl = 70
fan = 82
cclock =
mclock =

[SERO_Config]
wallet = Enter Wallet ID and click Save Config
algo = progpow --coin sero
pools = stratum+tcp://gongpool.com:8008
pl = 70
fan = 82
cclock =
mclock =

[VBK_Config]
wallet = Enter Wallet ID and click Save Config
algo = progpow-veriblock
pools = stratum+tcp://vbk.luckypool.io:9501
pl = 70
fan = 82
cclock =
mclock =

[VEIL_Config]
wallet = Enter Wallet ID and click Save Config
algo = progpow-veil
pools = stratum+tcp://pool.woolypooly.com:3098
pl = 70
fan = 82
cclock =
mclock =

[ZANO_Config]
wallet = Enter Wallet ID and click Save Config
algo = progpowz
pools = stratum+tcp://zano.luckypool.io:8877
pl = 70
fan = 82
cclock =
mclock =
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
    combo.place(x = 50, y = 55,
                width = 200,
                height = 35)
    combo_pools = ttk.Combobox(canvas)
    combo_pools['values'] = config['ALPH_Config']['pools'].split('\n')
    combo_pools.current(0)
    combo_pools.place(x = 25, y = 152,
                      width = 250,
                      height = 35)
    return combo, combo_pools


def create_window():
    root = Tk()
    root.title('T-Rex Gui v 0.2')
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
    progress_lbl = Label(canvas, text="")
    progress_lbl.place(x = 850, y = 125,
                       width = 200.0,
                       height = 40)
    return progress_lbl


def create_miner_tab_txt(canvas, config, root, combo):
    """ Create Miner Tab Text """
    root.entry0_img = entry0_img = PhotoImage(file = f"img_textBox0.png")
    entry0_bg = canvas.create_image(390, 265,
                                    image = entry0_img)
    fan_txt = Entry(canvas,
                    bd = 0,
                    bg = "#dddddd",
                    highlightthickness = 0)
    
    fan_txt.place(x = 345, y = 247,
                  width = 85,
                  height = 40)
    fan_txt.insert(0, config[combo.get()]['fan'])
    
    root.entry06_img = entry06_img = PhotoImage(file = f"img_textBox0.png")
    entry06_bg = canvas.create_image(570, 265,
                                    image = entry06_img)
    mclock_txt = Entry(canvas,
                    bd = 0,
                    bg = "#dddddd",
                    highlightthickness = 0)
    
    mclock_txt.place(x = 530, y = 247,
                  width = 85,
                  height = 40)
    mclock_txt.insert(0, config[combo.get()]['mclock'])
    
    root.entry1_img = entry1_img = PhotoImage(file = f"img_textBox0.png")
    entry1_bg = canvas.create_image(390, 170,
                                    image = entry1_img)
    pl_txt = Entry(canvas,
                   bd = 0,
                   bg = "#dddddd",
                   highlightthickness = 0)
    pl_txt.place(x = 345, y = 152, 
                 width = 85,
                 height = 40)
    pl_txt.insert(0, config[combo.get()]['pl'])
    
    root.entry15_img = entry15_img = PhotoImage(file = f"img_textBox0.png")
    entry15_bg = canvas.create_image(570, 170,
                                     image = entry15_img)
    cclock_txt = Entry(canvas,
                       bd = 0,
                       bg = "#dddddd",
                       highlightthickness = 0)
    cclock_txt.place(x = 530, y = 152, 
                     width = 85,
                     height = 40)
    cclock_txt.insert(0, config[combo.get()]['cclock'])
    
    root.entry2_img = entry2_img = PhotoImage(file = f"img_textBox4.png")
    entry2_bg = canvas.create_image(590.0, 73,
                                    image = entry2_img)
    
    wallet_txt = Entry(canvas,
                       bd = 0,
                       bg = "#dddddd",
                       highlightthickness = 0)
    wallet_txt.insert(0, config[combo.get()]['wallet'])
    
    wallet_txt.place(x = 345, y = 53,
                     width = 469.0,
                     height = 40)
    
    root.entry3_img = entry3_img = PhotoImage(file = f"img_textBox5.png")
    entry3_bg = canvas.create_image(718.5, 380,
                                    image = entry3_img)
    
    bat_txt = Entry(canvas,
                    bd = 0,
                    bg = "#dddddd",
                    highlightthickness = 0)
    
    bat_txt.place(x = 51.5, y = 362,
                  width = 1334.0,
                  height = 40)
    return fan_txt, pl_txt, wallet_txt, bat_txt, cclock_txt, mclock_txt


def create_miner_tab_buttons(canvas, root, config, mine_save_clicked, mine_clicked):
    """ Create Miner Tab Buttons """
    root.img0 = img0 = PhotoImage(file = f"img0.png")
    start_mine = Button(canvas,
                        image = img0,
                        borderwidth = 0,
                        highlightthickness = 0,
                        command = mine_clicked,
                        relief = "flat")
    
    start_mine.place(x = 595, y = 510,
                     width = 250,
                     height = 59)
    
    root.img1 = img1 = PhotoImage(file = f"img1.png")
    mine_config = Button(canvas,
                         image = img1,
                         borderwidth = 0,
                         highlightthickness = 0,
                         command = mine_save_clicked,
                         relief = "flat")
    
    mine_config.place(x = 595, y = 430,
                      width = 250,
                      height = 59)
    intensity = Scale(canvas, from_=0, to=27, orient=HORIZONTAL)
    intensity.place(x = 442, y = 300)
    root.background_img = background_img = PhotoImage(file = f"background.png")
    background = canvas.create_image(714.0, 185.0,
                                     image=background_img)  
    return start_mine, mine_config, intensity
     

def create_rig_tab_text(canvas2, config, root):
    """ Create Rig Tab Text """
    root.entry02_img = entry02_img = PhotoImage(file = f"img_textBox0.png")
    entry02_bg = canvas2.create_image(75, 257,
                                      image = entry02_img)
    
    rigname_txt = Entry(canvas2,
        bd = 0,
        bg = "#dddddd",
        highlightthickness = 0)
    
    rigname_txt.place(x = 28, y = 237,
                      width = 100.0,
                      height = 40)
    rigname_txt.insert(0, config['Rig_Info']['rig_name'])
    
    root.entry12_img = entry12_img = PhotoImage(file = f"img_textBox0.png")
    entry12_bg = canvas2.create_image(220, 257,
                                      image = entry12_img)
    
    password_txt = Entry(canvas2,
                         bd = 0,
                         bg = "#dddddd",
                         highlightthickness = 0)
    
    password_txt.place(x = 178, y = 237,
                       width = 100.0,
                       height = 40)
    password_txt.insert(0, config['Rig_Info']['password'])
    
    root.entry122_img = entry122_img = PhotoImage(file = f"img_textBox2.png")
    entry122_bg = canvas2.create_image(175, 357,
                                      image = entry122_img)
    
    email_txt = Entry(canvas2,
                      bd = 0,
                      bg = "#dddddd",
                      highlightthickness = 0)
    
    email_txt.place(x = 25, y = 337,
                    width = 300,
                    height = 40)
    email_txt.insert(0, config['Rig_Info']['email'])
    
    root.entry22_img = entry22_img = PhotoImage(file = f"img_textBox4.png")
    entry22_bg = canvas2.create_image(280, 168,
                                      image = entry22_img)
    
    location_txt = Entry(canvas2,
                         bd = 0,
                         bg = "#dddddd",
                         highlightthickness = 0)
    
    location_txt.place(x = 25, y = 147,
                       width = 480,
                       height = 40)
    location_txt.insert(0, config['Rig_Info']['location'])   
    
    root.entry32_img = entry32_img = PhotoImage(file = f"img_textBox4.png")
    entry32_bg = canvas2.create_image(280, 73,
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
    root.img02 = img02 = PhotoImage(file = f"img1.png")
    rig_save = Button(canvas2,
                      image = img02,
                      borderwidth = 0,
                      highlightthickness = 0,
                      command = rig_save_clicked,
                      relief = "flat")

    rig_save.place(x = 595, y = 430,
                   width = 250,
                   height = 59)

    root.background_img2 = background_img2 = PhotoImage(file = f"background2.png")
    background2 = canvas2.create_image(720, 175,
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
        with open(config_file, 'w') as configfile:
            config.write(configfile)
        progress_lbl.configure(text='{} Updated'.format(combo.get()))


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
        cclock_txt.delete(0, END)
        cclock_txt.insert(0, config[combo.get()]['cclock'])
        mclock_txt.delete(0, END)
        mclock_txt.insert(0, config[combo.get()]['mclock'])
        combo_pools['values'] = config[combo.get()]['pools'].split('\n')
        combo_pools.current(0)
        update_bat()


    def update_bat():
        """ Update Bat Text """
        bat_txt.delete(0, END)
        if 'nanopool' in combo_pools.get():
            rigname_fix = '{}/{}'.format(rigname_txt.get(), email_txt.get())
        else:
            rigname_fix = rigname_txt.get()
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
        if pl_txt.get() != '':
            new_bat = '{} --pl {}'.format(new_bat, pl_txt.get())
        if fan_txt.get() != '':
            new_bat = '{} --fan {}'.format(new_bat, fan_txt.get())
        if intensity.get() != 0:
            new_bat = '{} --intensity {}'.format(new_bat, intensity.get())
        if cclock_txt.get() != '' and cclock_txt.get() != '0':
            new_bat = '{} --cclock {}'.format(new_bat, cclock_txt.get())
        if mclock_txt.get() != '' and mclock_txt.get() != '0':
            new_bat = '{} --mclock {}'.format(new_bat, mclock_txt.get())
        bat_txt.insert(0, new_bat)


    root, my_frame1, my_frame2, canvas, canvas2 = create_window()
    config, config_file = read_config()
    combo, combo_pools = create_combos(canvas, config)
    progress_lbl = create_miner_tab_lbl(canvas)
    fan_txt, pl_txt, wallet_txt, bat_txt, cclock_txt, mclock_txt = create_miner_tab_txt(canvas, config, root, combo)
    start_mine, mine_config, intensity = create_miner_tab_buttons(canvas, root, config, mine_save_clicked, mine_clicked)
    
    progress_lbl2 = create_miner_tab_lbl(canvas2)
    rigname_txt, password_txt, location_txt, startup_txt, email_txt = create_rig_tab_text(canvas2, config, root)
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
    cclock_txt.bind("<KeyRelease>", lambda _ : update_bat())
    mclock_txt.bind("<KeyRelease>", lambda _ : update_bat())
    intensity.bind("<ButtonRelease-1>", lambda _ : update_bat())
    root.mainloop()


main()