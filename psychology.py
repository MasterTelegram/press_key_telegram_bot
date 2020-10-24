

# -*- coding: utf-8 -*-
from telethon import utils
import socks
import time
from telethon import TelegramClient, events, sync
import json
import iz_func
### --------------------------------------------------------------------------
from telethon.sync import TelegramClient
from telethon import functions, types
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
print ('[+] Версия 3.3')
namebot  = '@send314_bot'
api_hash    = 'XXXXXXXXXXXXXXXXXXXXXXXX'
api_id      = 192804
phone_number = 'XXXXXXXXXXXXXXXXXXXXXXXXX'
session = 'session_'+str(phone_number)+'_session'
client = TelegramClient(session,api_id=api_id,api_hash=api_hash) ### ,proxy=(socks.HTTP,ip ,int(port)
client.connect() 
if not client.is_user_authorized():
    print ('[+] Регистрация клиента',session)  
    client.send_code_request(phone_number)
    client.sign_in(phone_number, input('Enter the code: '))
    exit (0)

if not client.is_user_authorized():
    print ('[+] Нет клиента. Отправка сообшения в группу.')
else:
    channel_username = -XXXXXXXXXXXXXX
    channel_entity=client.get_entity(channel_username)
    posts = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
    print (posts)
    messageId = posts.messages[0].id
    message = posts.messages[0].message
    print ('[+] messageId',messageId)
    print ('[+]',message)
    yng = 0
    if message.find ('Возраст') != -1:
        nm = message.find ('Возраст')
        yng = int(message[nm+8:nm+11])
        print (yng)
        minvz = (iz_func.load_setting ('Минимальный возраст',namebot))
        maxvz = (iz_func.load_setting ('Максимальный возраст',namebot))      
        print ('minvz',minvz)
        print ('maxvz',maxvz)
    try: 
        print (posts.messages[0].reply_markup.rows[0].buttons[0].data)
        #client(GetBotCallbackAnswerRequest(channel_username,messageId,data=b'press'))
    except Exception as e: 
        pass  
        print (e)  
@client.on(events.NewMessage)
async def my_event_handler(event):
    import iz_func
    print (event)    
    user_id  = '590719271'
    variable = 'Статус бота'
    namebot  = '@send314_bot'
    status_o = iz_func.load_variable (user_id,variable,namebot) 
    message = ''
    message = event.original_update.message
    print ('[status_o]',status_o)
    print ('[+]',message)
    yng = 0
    minvz = 0
    maxvz = 0
    if str(message).find ('Возраст') != -1:
        minvz = int(iz_func.load_setting ('Минимальный возраст',namebot))
        maxvz = int(iz_func.load_setting ('Максимальный возраст',namebot))
        print ('[+] Минимальный возраст',minvz)
        print ('[+] Максимальный возраст',maxvz)
        nm  = str(message).find ('Возраст')
        yng = int(str(message)[nm+8:nm+10])
        print ('[+] Возраст в сообщении:',yng)
        timestamp = int(time.time())
        status_t = iz_func.load_variable (user_id,'Время сделки',namebot)
        if status_t == '':
            status_t = 0
        utime =  (timestamp - int(status_t))//60
        print ('[+] Время последней сделки',utime,'мин.')
        label = 'yes'
        if status_o == 'ON':
            pass
        else:    
            label = 'Нет команды включить'
            print ('[+]',label)
        twait = int(iz_func.load_setting ('Время ожидания бота',namebot))
        print ('[+] Время ожидания между сделками:',twait)
        if utime > twait:
            pass
        else:    
            label = 'Не прошло время'
            print ('[+]',label)
        print ('[+] Возраст:',yng,',а мин',minvz)
        if yng < minvz:
            label = 'Возраст не совпадает мин'
            print ('[+]',label)
        print ('[+] Возраст:',yng,',а мак',maxvz)
        if yng > maxvz:
            label = 'Возраст не совпадает мак'
            print ('[+]',label)
        if label == 'yes':
            try: 
                #channel_username = 'Psyhologram Bid'
                channel_username = 'Psyhologram.ru'
                channel_entity=await client.get_entity(channel_username)
            except Exception as e: 
                pass    
                print ('    =',e)    
            posts = await client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))        
            find_post = str(posts)
            nof = 'no'
            print ('[+] Текст для анализа')
            print (find_post)
            if find_post.find('Неизвестная проблема') != -1:
                nof = 'yes'
            if find_post.find('Депрессия и депрессивность') != -1:
                nof = 'yes'
            if find_post.find('Личностный рост') != -1:
                nof = 'yes'
            if find_post.find('Проблемы в сексе') != -1:
                nof = 'yes'
            if find_post.find('Проблемы общения') != -1:
                nof = 'yes'
            if find_post.find('Проблемы в отношениях') != -1:
                nof = 'yes'
            if find_post.find('Самоопределение в жизни') != -1:
                nof = 'yes'
            if find_post.find('Самооценка и увереность') != -1:
                nof = 'yes'
            if find_post.find('Семейные проблемы') != -1:
                nof = 'yes'
            if find_post.find('Страх и фобия') != -1:
                nof = 'yes'
            if find_post.find('Тревожность') != -1:
                nof = 'yes'
            if nof == 'yes':
                print ('[+] Для работы все есть. Нажимаем кнопку)')
                messageId = posts.messages[0].id
                print ('    [messageId]',messageId)
                try: 
                    datal = posts.messages[0].reply_markup.rows[0].buttons[0].data
                    iz_func.save_variable (user_id,"Время сделки",str(timestamp),namebot)
                    await client(GetBotCallbackAnswerRequest(channel_username,messageId,data=datal))                
                except Exception as e:  
                    print ('    ',e)
                    print ('    [+] нет кнопки')
            else:
                print ('[-] Нет входящего слова')        
        else:
            print ('[-] Отменен по условию фильтра',label )
    else:
        print ('[+] В сообщении нет возраста')
client.start()
client.run_until_disconnected()













