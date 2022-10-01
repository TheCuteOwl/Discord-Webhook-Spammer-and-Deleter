
import requests
import time
from pystyle import * 


message = ''
def delete():
    webhook = input(Colorate.Horizontal(Colors.blue_to_green, 'Webhook URL : '))
    requests.delete(webhook)
    print(Colorate.Horizontal(Colors.blue_to_green, 'Successfully Deleted'))
    input(Colorate.Horizontal(Colors.blue_to_green, 'Press Enter to quit'))
    quit()


def Spamming():
    url = input(Colorate.Horizontal(Colors.blue_to_green, 'Webhook URL : '))
    message = "@everyone | Spam Moment " + str("⛓️" * 1000)
    data = {
    "content" : message,
    "username" : "custom username"
}


    while True:
        result = requests.post(url, json = data)
        time.sleep(0.2)
        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)
        else:
          print(Colorate.Horizontal(Colors.blue_to_green, "Send successfully, code {}.".format(result.status_code)))


def SpammingCustom():
    url = input('Webhook URL : ')
    message = messages
    data = {
    "content" : message,
    "username" : "custom username"
}


    while True:
        result = requests.post(url, json = data)
        time.sleep(0.2)
        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)
        else:
          print("Send successfully, code {}.".format(result.status_code))


choice = input(Colorate.Horizontal(Colors.blue_to_green, '''What do you want ?
[1]Spamming (Without Custom Message)
[2]Spamming (With Custom Message)
[1]Delete Webhook (Without Custom Message)'''))

if choice == '1':
    
    Spamming()

elif choice == '2':
    messages = input(Colorate.Horizontal(Colors.blue_to_green,'Message To Spam : '))
    SpammingCustom()

elif choice == '3':
    delete()







