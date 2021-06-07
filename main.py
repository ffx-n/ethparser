import requests
import telebot


token = "1817923374:AAG-gGXRvC98ukdhyfO-CClAku4c65t-cqY"
tb = telebot.TeleBot(token)
def read_add():
    with open("addresses.txt", "r", encoding="utf-8") as f:
        r = f.read().split("\n")
    return r


def check_balance(address):
    url = f'https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey=WIEVI3F6D88WMB3SM77WUDE9MYFAIU3M3S'
    r = requests.get(url)
    balance = r.json()['result']
    if len(balance) < 18:
        need_zeros = f"{'0' * (18 - len(balance))}"
        balance = '0.' + need_zeros + balance
    elif len(balance) == 18:
        balance = "0." + balance
    else:
        balance = balance[:-18] + '.' + balance[-17:]
    return balance


while True:
    try:
        data = read_add()
        for i in data:
            try:
                balance = float(check_balance(i))
                if balance >= 0.0050:
                    tb.send_message(1757275340, f'balance: {balance}\naddress:{i}')
            except Exception as err:
                tb.send_message(1757275340, f'error {err}')
                print(err)
                continue
    except Exception as err:
        tb.send_message(1757275340, f'critical error {err}')


#print(check_balance("0xdb54fee4796db6db094ce40509582b0e92c44dae"))