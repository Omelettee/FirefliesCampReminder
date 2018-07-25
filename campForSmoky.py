import pandas as pd
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime

def check():
    print datetime.datetime.now().time()
    #change the following address,especially the target date, which is 06/08/2018
    #Target date should be a Friday, for the original code is specific for camp sites on weekends 
    #If not, edit "== 0" in line 31 && "== 1" in line 33 
    res = requests.get("https://www.recreation.gov/campsiteCalendar.do?page=matrix&calarvdate=06/08/2018&contractCode=NRSO&parkId=70968")
    soup = BeautifulSoup(res.content,'lxml')
    table = soup.find_all('table')[0]
    temp = str(table).split("\n")
    reserve = []
    for line in temp:
            if "td" in line and "div" not in line and "status" in line:
                if "status r" in line:
                    reserve.append("r")
                elif "status a" in line : 
                    reserve.append("a")
                else :
                    reserve.append("unknown")
    Fri = []
    Sat = []
    for i in range(350):
        if i%14 == 0:
            Fri.append(reserve[i])
        if i%14 == 1: 
            Sat.append(reserve[i])
            
    flag =  'a' in Fri or 'a' in Sat
    s = smtplib.SMTP(host='smtp.gmail.com',port=587)
    s.starttls()
    from_add = '' #The sender's email 
    password = '' #The password of sender's email
    to_add = ['',''] #Add all receivers' email in this list
    s.login(from_add,password)

    if flag:
        for email in to_add:
            msg = MIMEMultipart()
            msg['From'] = '' #The sender's email
            msg['To'] = email
            msg['Subject'] = 'There is space for camping right now'
            msg.attach(MIMEText("If you are available, please sign up right now!\nhttps://www.recreation.gov/campsiteCalendar.do?page=matrix&calarvdate=06/08/2018&contractCode=NRSO&parkId=70968", 'Plain'))
            s.sendmail(from_add,email,msg.as_string())
    s.quit

scheduler = BlockingScheduler()
scheduler.add_job(check, 'interval', minutes=10)
scheduler.start()
     
