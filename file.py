import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
now=datetime.datetime.now()

content= '' #email content

# extract hacker news
def extract_news(url):
    print("extracting hacker news stories")
    cnt=''
    cnt+= ('<b>HN Top Stories:</b>\n '+'<br>'+'-'*50+'<br>')
    response=requests.get(url)
    content=response.content
    soup=BeautifulSoup(content,'html.parser')
    for i,tag in enumerate(soup.find_all('td',attrs={'class':'title','valign':''})) :
        cnt+=(( str(i+1)+' :: '+tag.text+"\n"+'<br>') if tag.text!= 'More' else '')
    return cnt
cnt= extract_news('https://news.ycombinator.com')
content+=cnt
content+= ('<br>----------<br>')
content+=('<br> End of Message <br>')

print("Composing email...")
# email details
SERVER='smtp.gmail.com'
PORT=587 #for gmail port number is 587
FROM='kavinnilamahendran@gmail.com'
TO='ppselvi1670@gmail.com'
PASS='k2V462Kn4L2'

msg=MIMEMultipart()

msg['Subject']='Top News Stories HN [Automated Email] '+ str(now.day)+','+str(now.month)+','+str(now.year)
msg['From']= FROM
msg['To']=TO

msg.attach(MIMEText(content,'html'))
print("Initiating server...")

server=smtplib.SMTP(SERVER,PORT)
server.set_debuglevel(0) # 1 to see error messages
server.ehlo()
server.starttls()
server.login(FROM,PASS)
server.sendmail(FROM,TO,msg.as_string())

print("Email sent...")
server.quit()
