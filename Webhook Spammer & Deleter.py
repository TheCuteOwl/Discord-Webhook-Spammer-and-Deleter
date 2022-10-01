import requests
import time
from pystyle import * 


message = ''

def deletemultiple():
    with open('webhook.txt', 'r') as f:
        while (webhook := f.readline().rstrip()):

            
            print(Colorate.Horizontal(Colors.blue_to_green, 'deleting : ' + webhook))
            requests.delete(webhook)
            print(Colorate.Horizontal(Colors.blue_to_green,'Successfully deleted :' + webhook))
    input('Finished press Enter to quit')
    quit()


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
    "username" : "Spam Moment"
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
    messages = input(Colorate.Horizontal(Colors.blue_to_green,'Message To Spam : '))
    message = messages
    data = {
    "content" : message,
    "username" : "Spam Moment"
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


def Start():    
    choice = input(Colorate.Horizontal(Colors.blue_to_green, '''What do you want ?
[1]Spamming (Without Custom Message)
[2]Spamming (With Custom Message)
[3]Delete Webhook 
[4]Delete Multiple Webhook
Choose : '''))

    if choice == '1':
    
        Spamming()

    elif choice == '2':
      SpammingCustom()

    elif choice == '3':
        delete()
    elif choice == '4':
        deletemultiple()

    else:
        print(Colorate.Horizontal(Colors.blue_to_green, 'Wrong Number'))
        time.sleep(0.5)
        print('\n' * 100)
        Start()

Start()
