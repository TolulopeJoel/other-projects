import AtmFunctions

account_type = {'s': 'savings', 'c': 'current'}


def account_selection():  # choosing account type
    global account_type
    print('(S)avings or (C)urrent account ')
    withdrawal_account = input('>> ').lower()
    if withdrawal_account in account_type.keys():
        get_account_balance = AtmFunctions.account_balance.get(withdrawal_account)
        print(get_account_balance)
    else:
        print('unknown account type')
        account_selection()

    def withdrawal():
        try:
            withdrawal_amount = int(input('How much do you want to withdraw? \n>> '))
            if withdrawal_amount <= (get_account_balance - 10):
                AtmFunctions.account_balance[withdrawal_account] = AtmFunctions.account_balance[withdrawal_account] - withdrawal_amount
                print(f'\n${withdrawal_amount} was debited from your {account_type[withdrawal_account]} account')
                print(f"you have ${AtmFunctions.account_balance[withdrawal_account]} left in your {account_type[withdrawal_account]} account")
                while True:
                    new_withdrawal = input('do you want to continue this process? [y/n] \n>> ').lower()
                    if new_withdrawal == 'y':
                        withdrawal()
                    elif new_withdrawal == 'n':
                        exit()
                    else:
                        print('unknown input type\n')
                        continue
            else:
                print(f'Insufficient Funds ☹ glitch\ntry withdrawing from $10 to ${AtmFunctions.account_balance[withdrawal_account] - 10}')
                withdrawal()
        except ValueError:
            print('this is not an amount')
            withdrawal()

    withdrawal()
