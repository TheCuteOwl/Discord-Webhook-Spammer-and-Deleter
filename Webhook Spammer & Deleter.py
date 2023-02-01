import subprocess
import time

try:
    import requests
except:
    print('Module not installed')
    print('Installing For you...')
    print('Press enter when download is done...')
    time.sleep(1)
    subprocess.Popen("pip install Pystyle", shell=True)
    subprocess.Popen("pip install requests", shell=True) 
    time.sleep(2)
    input('You can now press Enter')

import requests

message = ''

def deletemultiple():
    with open('webhook.txt', 'r') as f:
        while (webhook := f.readline().rstrip()):

            
            print(( 'deleting : ' + webhook))
            requests.delete(webhook)
            print(('Successfully deleted :' + webhook))
    input('Finished press Enter to quit')
    quit()


def delete():
    webhook = input(( 'Webhook URL : '))
    requests.delete(webhook)
    print(( 'Successfully Deleted'))
    input(( 'Press Enter to quit'))
    quit()


def Spamming():
    url = input(( 'Webhook URL : '))
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
          print(( "Send successfully, code {}.".format(result.status_code)))


def SpammingCustom():
    url = input('Webhook URL : ')
    messages = input(('Message To Spam : '))
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
    choice = input(( '''What do you want ?
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
        print(( 'Wrong Number'))
        time.sleep(0.5)
        print('\n' * 100)
        Start()

Start()




