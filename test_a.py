

# -*- coding: utf-8 -*-
from telethon import utils
import socks
import time
from telethon import TelegramClient, events, sync
import json
### --------------------------------------------------------------------------

from telethon.sync import TelegramClient
from telethon import functions, types
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest

ip          = '196.18.3.55'
port        = 8000
password    = 'Fkv7JY'
userproxy   = 'YHB8GP'
api_hash    = '1b40d1d01f8922b384d44e29d32f6acf'
api_id      = 192804
phone_number = '+79031279070'
client = TelegramClient('session_'+str(phone_number),api_id=api_id,api_hash=api_hash,proxy=(socks.HTTP,ip,port,'',password,userproxy))
client.connect()        
if not client.is_user_authorized():
    print ('[+] Нет клиента')
else:
    print ('[+] Версия 3.8')


if 1==2:
    channel_username='Psyhologram Bid'
    channel_entity=client.get_entity(channel_username)
    posts = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
    print ('----------------------------------------------')
    print (posts)
    messageId = posts.messages[0].id
    print (messageId)
    print ('--------------------------------------------------------')
    try: 
        print (posts.messages[0].reply_markup.rows[0].buttons[0].data)
        #client(GetBotCallbackAnswerRequest(channel_username,messageId,data=b'press'))
    except Exception as e: 
        pass  
        print (e)  

@client.on(events.NewMessage)
async def my_event_handler(event):
    print ('-----------------------------------------------------------------------------------------')
    print (event)
    print ('-----------------------------------------------------------------------------------------')
    import iz_func
    user_id  = '590719271'
    variable = 'Статус бота'
    namebot  = '@client_to_314_bot'
    status_o = iz_func.load_variable (user_id,variable,namebot) 
    print ('[status_o]',status_o)
    timestamp = int(time.time())
    status_t = iz_func.load_variable (user_id,'Время сделки',namebot)
    if status_t == '':
        status_t = 0
    utime =  (timestamp - int(status_t))//60
    print ('[+] Время последней сделки',utime,'мин.')

    #if 1==1:
    if status_o == 'ON' and utime > 15:
        try: 
            channel_username = 'Psyhologram Bid'
            channel_entity=await client.get_entity(channel_username)
        except Exception as e: 
            pass    
            print ('    =',e)    

        posts = await client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))        
        find_post = str(posts)

        nof = 'no'
        if find_post.find('Неизвестная проблема') != -1:
            nof = 'yes'
            print ('1')


        if find_post.find('Депрессия и депрессивность') != -1:
            nof = 'yes'
            print ('2')

        if find_post.find('Личностный рост') != -1:
            nof = 'yes'
            print ('3')

        if find_post.find('Проблемы в сексе') != -1:
            nof = 'yes'
            print ('4') 

        if find_post.find('Проблемы общения') != -1:
            nof = 'yes'
            print ('5') 


        if find_post.find('Проблемы в отношениях') != -1:
            nof = 'yes'
            print ('6')

        if find_post.find('Самоопределение в жизни') != -1:
            nof = 'yes'
            print ('7')


        if find_post.find('Самооценка и увереность') != -1:
            nof = 'yes'
            print ('8')


        if find_post.find('Семейные проблемыye') != -1:
            nof = 'yes'
            print ('9') 


        if find_post.find('Страх и фобия') != -1:
            nof = 'yes'
            print ('10') 

        if find_post.find('Тревожность') != -1:
            nof = 'yes'
            print ('11')

        if nof == 'yes':
            messageId = posts.messages[0].id
            print ('    [messageId]',messageId)
            try: 
                datal = posts.messages[0].reply_markup.rows[0].buttons[0].data
                print ('    [+]',datal)
                iz_func.save_variable (user_id,"Время сделки",str(timestamp),namebot)
                await client(GetBotCallbackAnswerRequest(channel_username,messageId,data=datal))                
            except Exception as e: 
                pass    
                print ('    ',e)
                print ('    [+] нет кнопки')
        else:
            print ('[-] Нет входящего слова')        


    else:
        print ('[-] Отменен по условию')



client.start()
client.run_until_disconnected()













