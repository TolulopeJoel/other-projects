import time
import AtmMachine

banks = ['glitch', 'zone', 'winter', 'ringer', 'agents']


def available_banks():
    for bank in banks:
        print(bank)


class AtmCard:                                                                                          # atm card and card_validity
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def user_card(self, account_number):
        if len(account_number) == 11:
            card_validity = True
        else:
            card_validity = False
        if card_validity:
            print(f'\n\nwelcome {self.first_name} {self.last_name} 😃')
        else:
            print('\nsorry, this account account number is not recognized 🤧')


account_balance = {'s': 10000, 'c': 37000}                                                # s stands for savings and c stands for current account

print('available banks are; ')                                                                                                              # selecting banks
available_banks()
user_bank = input('\nYour Bank 👀 \n>> ').lower()
while user_bank not in banks:
    print('bank not available 😶\n')
    print('banks available are:')
    available_banks()
    user_bank = input('\nYour Bank👀>> ').lower()
else:
    print('verifying card.', end='')
    for i in range(5):
        time.sleep(1.0)
        print('.', end='')

atm_card = AtmCard('tolu', 'joel')                                                                                              # virtual atm card
atm_card.user_card('12345678900')

while True:
    print('what do you want to do??\nwithdraw money(w) \ndeposit money(d) \ncheck account balance(c)\n')
    atm_task = input('>>> ').lower()

    if atm_task == 'w':                                                                                                # withdrawing money
        for i in range(5):                                                                                                      # pin validation
            enter_pin = input('enter your four digit pin (why are my eyes closed😭) \n>> ')

            if (enter_pin.isnumeric() and len(str(enter_pin))) == 4:
                print('\naccess granted')
                pin_validation = True
                if pin_validation:
                    AtmMachine.account_selection()

            elif not enter_pin.isnumeric():                                                                             # pin not a number
                for j in range(5):
                    print('pin can\'t contain letters or symbols')
                    enter_pin = input('enter your four digit pin (why are my eyes closed😭) \n>> ')

                    if (enter_pin.isnumeric() and len(str(enter_pin))) == 4:
                        pin_validation = True
                        print('\naccess granted')
                        if pin_validation:
                            print('\n(S)avings or (C)urrent account')
                            AtmMachine.account_selection()
                        break
                    print('pin too short or long')
                    enter_pin = input('enter your four digit pin (why are my eyes closed😭) \n>> ')

            elif len(enter_pin) != 4:
                for v in range(5):
                    if len(enter_pin) == 4:
                        print('\naccess granted')
                        break
                    print('pin too short or long')
                    enter_pin = input('enter your four digit pin (why are my eyes closed😭) \n>> ')
            break

    elif atm_task == 'd':                                                                                         # depositing money
        print('please walk into the bank🤲, thank you\nThis operation can\'t be carried out here now\n')

    elif atm_task == 'c':                                                                                         # checking account balance
        print(f"savings account: ${account_balance['s']}")
        print(f"current account: ${account_balance['c']}\n")

    else:
        print('invalid input, try again')
        continue
