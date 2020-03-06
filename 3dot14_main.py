from telethon import TelegramClient, events
from telebot import apihelper
from telebot import types

import socks
import telebot
import time

### --------------------------------------------------------------------------
import optparse
parser =  optparse.OptionParser(version='1.0',description='Шаблон')
parser.add_option('-t','--telefon', type='string', dest='telefon', help='Телефон исходящий')
parser.add_option('-i','--input  ', type='string', dest='input'  , help='Телефон входящий ')
parser.add_option('-m','--message', type='string', dest='message', help='Сообщение')
(options, args) = parser.parse_args()
print ("[+] Текст сообщения "  ,options.message)
print ("[+] Телефон исходящий ",options.telefon)
print ("[+] Телефон входящий  ",options.input)


#ip   = '196.18.15.10'
#port = '8000'
#password  = 'ExejJZ'
#userproxy = 'J22FvE'
#proxy = {'https':'http://{}:{}@{}:{}'.format(password,userproxy,ip,port)}
#print ('[+]',proxy)
#apihelper.proxy = proxy 

ip   = '196.18.3.55'
port = '8000'
password  = 'Fkv7JY'
userproxy = 'YHB8GP'
proxy = {'https':'http://{}:{}@{}:{}'.format(password,userproxy,ip,port)}
#proxy = {'https':'http://{}:{}@{}:{}'.format(password,userproxy,ip,port)}
print ('[+]',proxy)
apihelper.proxy = proxy 


namebot  = "@client_to_314_bot"
token    = '719993270:AAGXXlx74xaj9A5AFdI6YXVM8OdUkXfpQMk'
bot      = telebot.TeleBot(token)
#print (iz_func.c8+"[+]",namebot,iz_func.c0)
#print ('Ver 3.1.0, Аvtor: @Pi_3dot141 (https://t.me/Pi_3dot141)')
user_id  = '399838806'
#user_id  = '981876621'

message_out = 'Запуск бота сборшика информации'
bot.send_message(user_id,message_out,parse_mode='HTML')   ### ,reply_markup=markup
        
## +40773456128 (BitBaza Sale);
## +18295062766 (Kung-Fu Crypto);
## +79265192506 (Господин Энергосбыт);
## +79776524835 (Григорий);
## +18093576174 (Промышленный Майнер);
## +79315939641 (Эрик Кван);        
#phone_number = "+"+options.telefon
#print ("[phone_number]",phone_number)
#client = TelegramClient('session_'+str(phone_number),api_id=192804,api_hash='1b40d1d01f8922b384d44e29d32f6acf',proxy=(socks.HTTP,'196.18.15.10',8000,'','ExejJZ','J22FvE'))


##session_main = 'session_+79033671563.session'

session_main = 'session_+79031279070.session'
print (session_main)



client = TelegramClient(session_main,api_id=192804,api_hash='1b40d1d01f8922b384d44e29d32f6acf',proxy=(socks.HTTP,ip ,8000,port,'Fkv7JY','YHB8GP'))

client.connect() 
if not client.is_user_authorized():
    phone_number = '+79031279070'
    client.send_code_request(phone_number)
    client.sign_in(phone_number, input('Enter the code: '))



import requests
@client.on(events.NewMessage)
async def my_event_handler(event):
    print ('[event]',event)
    print ('')
    print ('[message]',event.message)
    print ('')
    print ('[message]',event.message.id)
    print ('')
    print ('[reply_markup]',event.message.reply_markup)

    #print ('[event]',event.sender())
    #print ('[+] event.to_id ',event.to_id) 
    #if str(event.to_id).find("PeerUser") != -1:
    #    print ('-----------------------------')
    #    sender = await event.get_sender()
    #    print ('[+]',sender.id) 
    #    print ('[+]',sender.first_name )
    #    print ('[+]',sender.last_name)
    #    print ('[+]',sender.username)
    #    print ('[+]',sender.phone)
    #    Conect02 = str(sender.phone) ###str(sender.first_name) + ' - ' + sender.last_name + ' - ' + sender.username + ' - ' + sender.phone
    #    print ("[+] tel",Conect02)
    #    print ('-----------------------------')
    #    URL = 'http://192.168.0.85/amo/amo.php'
    #    URL = URL + '?service=contact&level=apiAdd&subdomain=bitbaza.amocrm.ru&login=miner@bitbaza.ru&hash=9cb70cbae27023cb520d572ad67b8578375e3254'
    #    URL = URL + '&name='+Conect02+'&request_id=Conect03&responsible_user_id=Conect04&company_name=Conect01&tags1=Conect05&tags2=Conect06'
    #    response = requests.get(URL)
    #    userAMO = str(response.content)
    #    userAMO = userAMO.replace("b", "")
    #    userAMO = userAMO.replace("'", "")
    #    userAMO = userAMO.replace('"', "")
    #    print('[userAMO]',userAMO)  ## .encode('utf-8')
    #    lead02 = 'Лид из телеграм @'+str(sender.username) + ' - телефон: '+str(sender.phone) ##Conect02
    #    lead04 = '2259499' ##str(userAMO)
    #    URL = 'http://192.168.0.85/amo/amo.php/amo/amo.php'
    #    URL = URL + '?service=lead&level=apiAdd&subdomain=bitbaza.amocrm.ru&login=miner@bitbaza.ru&hash=9cb70cbae27023cb520d572ad67b8578375e3254'
    #    URL = URL + '&name='+lead02+'&date_create=''&responsible_user_id='+lead04+'&status_id=lead05&price=lead03&tags1=lead06&tags2=lead07&visitor_uid=lead08'
        
    #    print ('[+]',URL)
        
    #    response = requests.get(URL)
    #    leadAMO = str(response.content)
    #    leadAMO = leadAMO.replace("b", "")
    #    leadAMO = leadAMO.replace("'", "")
    #    leadAMO = leadAMO.replace('"', "")
    #    print('[leadAMO]',leadAMO)  ## .encode('utf-8')
    #    #message_out = '<b>'+phone_number+'</b>\n'
    #    #message_out = message_out + event.raw_text
    #    print ('[text] ',event.raw_text)
        #bot.send_message(user_id,message_out,parse_mode='HTML')   ### ,reply_markup=markup
        #print (user_id)
        #print (message_out)
        #if 'hello' in event.raw_text:
           #await event.reply('hi!')
            
            
client.start()
client.run_until_disconnected()













