## Fireflies Camp Site Reminder
   - Send the email as a reminder when there is a camp site available during synchronous fireflies week. 

### Getting Started
#### Prerequisites
The following pakages need to be installed before implenting this code:
* BeautifulSoup
* smtplib
* email.mime.multipart
* email.mime.text
* apscheduler.schedulers.blocking

### Deployment
#### Set up the following parameters in the code:
* res : the address for webpate to be scraped
* from_add : the sender's email
* password : the passowrd of sender's email
* to_add : the lists of receivers' emails
* msg\[From] : the sender's email

### Example
#### Take Aug.3 (Friday) for example as target weekends
1. res = \"https://www.recreation.gov/campsiteCalendar.do?page=matrix&calarvdate=08/03/2018&contractCode=NRSO&parkId=70968"
2. Type in the sender's and receivers' email addresses.
3. Implement code in the terminal. 
   - This code will check available site every 10 min
4. When there is space avalible on Aug. 3rd or Aug. 4th, all the receivers would get the email reminder's automatically. 
   - For more options in various days, edit 'if i%14 == 0:' in line 31 and 33
   - If target date is Aug.3, when i = 0 is Aug. 3, i = 5 is Aug. 7 


