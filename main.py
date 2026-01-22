'''
Docstring for main
'''

import datetime
from src import *
import src.utils as utils
from src.login import login_interface

PRODUCTKEYS = [ # 10 Product Keys 

	'2030-GITH-UBGC-AKKI-DIST-FIRS-TPRJ-INDI-AUSA-2026',
	'2030-AKKI-FIRS-TPRJ-HAPP-YGIT-DIST-USAI-NDIA-2026',
	'2030-DEV0-FIRS-TPRJ-INDI-AUSA-AKKI-AT18-0022-2026',
	'2030-GITH-UBAT-AKKI-USAI-NDIA-FIRS-TPRJ-2008-2026',
	'2030-AKKI-ATUS-AGOO-GLEA-ISSE-100M-USAI-NDIA-2026',
	'2030-USAI-NDIA-GOOG-LEAI-WITH-AKKI-WITH-$10T-2026',
	'2030-ALLR-IGHT-SREC-IVED-WITH-AKKI-INDI-AUSA-2026',
	'2030-USAI-NDIA-2008-VSCO-DEPY-THON-AIAT-AKKI-2026',
	'USAI-NDIA-VIRA-TIAK-IRAN-ANDH-ANRE-DDY1-2008-2030',
	'LAST-PROD-UCTK-EYAT-AKKI-PROG-RAM1-USAI-NDIA-2030'

]

def PRODUCT_ACTIVATION() -> None:

    def is_Product_Key_Valid() -> None:
        
        if product_key_to_be_verified.get() in PRODUCTKEYS:

            ACTIVATEBUTTON.configure(fg_color = '#A9C5E8', state = 'disabled', text_color_disabled = 'Black')
            product_key_to_be_verified.configure(state = 'disabled')
            STATUS.configure(text = 'STATUS : ACTIVATED', text_color = 'lime')
            CONTINUE.configure(fg_color = '#4CAF50', state = 'normal')
            CONFIGURATION_JSON['isActivated'] = True

    WINDOW = customtkinter.CTk()
    WINDOW.title('PRODUCT ACTIVATION - BANK WITH HIGH FUNCTIONALITIES')
    WINDOW.geometry('800x400')
    WINDOW.resizable(False, False)
    WINDOW.protocol('WM_DELETE_WINDOW', lambda: WINDOW.destroy() if CONFIGURATION_JSON.get('isActivated') else exit())
    customtkinter.CTkLabel(WINDOW, text = 'ENTER A VALID PRODUCT KEY', font=('Arial', 28), text_color='#378F9C', justify = 'left').place(x=20,y=17)
    customtkinter.CTkLabel(WINDOW, text = 'Product keys will be available on our official GitHub page. Please visit the repository to access the keys & stay updated.\nWe recommend ' \
    'checking the repository regularly for new updates, instructions, or important notices regarding this software.\n\nWe truly appreciate your patience & support as we work to provide the best ' \
    'experience possible. Thank you for being with us.',
                    font=('Roboto', 13), justify = 'left').place(x=20,y=67)
    customtkinter.CTkLabel(WINDOW, text = 'PRODUCT KEY', font = ('Roboto', 16), justify = 'left').place(x = 20, y = 170)
    product_key_to_be_verified = customtkinter.CTkEntry(WINDOW, placeholder_text = 'XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX-XXXX', font=('Consolas', 14), width = 407) ; product_key_to_be_verified.place(x = 20, y = 201)
    customtkinter.CTkButton(WINDOW, text = 'CLICK HERE TO VISIT REPOSITORY', fg_color='transparent', hover = False, text_color = '#21968B', command = lambda: utils.Open_Browser_For_Specified_URL(CONSTANTS['WEBSITES']['GITHUB_REPOSITORY'])).place(x = 5, y = 367)
    
    STATUS = customtkinter.CTkLabel(WINDOW, text = 'STATUS : NOT ACTIVATED', text_color = 'Red' ,font = ('Roboto', 18, 'bold')) ; STATUS.place(x = 505 , y = 240 )
    ACTIVATEBUTTON = customtkinter.CTkButton(WINDOW, text = 'ACTIVATE', text_color = 'Black', corner_radius=4, width=100, fg_color = '#007ACC', hover_color = '#3399FF', command = is_Product_Key_Valid) ; ACTIVATEBUTTON.place(x = 156, y = 290)
    customtkinter.CTkButton(WINDOW, text = 'Cancel', corner_radius = 4, fg_color = '#7BC47F', text_color = 'Black', hover_color = '#6BBF59', width = 100, command = lambda: [WINDOW.destroy(), exit()]).place(x = 580, y = 357)
    CONTINUE = customtkinter.CTkButton(WINDOW, text = 'Continue', corner_radius=4, fg_color = '#B0B0B0', text_color = 'Black', text_color_disabled = 'Black', hover_color='#45A049',
                    state = 'disabled', width = 100, command = WINDOW.destroy) ; CONTINUE.place(x = 685, y = 357)

    WINDOW.mainloop()

if not CONFIGURATION_JSON.get('isActivated', False):
    PRODUCT_ACTIVATION()

print('program started')
CONFIGURATION_JSON["Recently Used On"] = datetime.datetime.now().strftime('%d-%b-%Y -- %A @ %I:%M:%S %p')
login_interface().login()
