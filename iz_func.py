#!/usr/bin/python
# -*- coding: utf-8

if 1==1:
    c0  =  "\033[0;37m"  ## Белый
    c1  =  "\033[1;30m"  ## Черный
    c2  =  "\033[0;31m"  ## Красный
    c3  =  "\033[0;32m"  ## Зеленый
    c4  =  "\033[1;35m"  ## Magenta like Mimosa\033[1;m
    c5  =  "\033[1;33m"  ## Yellow like Yolk\033[1;m'
    c7  =  "\033[1;37m"  ## White
    c8  =  "\033[1;33m"  ## Yellow
    c9  =  "\033[1;32m"  ## Green
    c10 =  "\033[1;34m"  ## Blue
    c11 =  "\033[1;36m"  ## Cyan
    c12 =  "\033[1;31m"  ## Red
    c13 =  "\033[1;35m"  ## Magenta
    c14 =  "\033[1;30m"  ## Black
    c15 =  "\033[0;37m"  ## Darkwhite
    c16 =  "\033[0;33m"  ## Darkyellow
    c17 =  "\033[0;32m"  ## Darkgreen
    c18 =  "\033[0;34m"  ## Darkblue
    c19 =  "\033[0;36m"  ## Darkcyan
    c20 =  "\033[0;31m"  ## Darkred
    c21 =  "\033[0;35m"  ## Darkmagenta
    c22 =  "\033[0;30m"  ## Darkblack
    c23 =  "\033[0;0m"   ## Off

def menu_command (menu01,menu02,menu03,menu11,menu12,menu13,menu21,menu22,menu23):
    if menu01.find ('_') == -1:
        menu01_com = menu01
    else:    
        nmc = menu01.find ('_')
        menu01_com = menu01
        menu01 = menu01[0:nmc]

    from telebot import types
    markup = types.InlineKeyboardMarkup(row_width=4)
    if menu01 != "":
        mn01 = ""
        mn02 = ""
        mn03 = ""
        mn01 = types.InlineKeyboardButton(text=menu01,callback_data=menu01_com)
        
        if menu02 != "":
            mn02 = types.InlineKeyboardButton(text=menu02,callback_data=menu02)
        if menu03 != "":
            mn03 = types.InlineKeyboardButton(text=menu03,callback_data=menu03)
            
        if mn01 != '' and mn02 == '' and mn03 == '':
            markup.add(mn01)
        if mn01 != '' and mn02 != '' and mn03 == '':
            markup.add(mn01,mn02)
        if mn01 != '' and mn02 != '' and mn03 != '':
            print ('[+] 3 меню')
            markup.add(mn01,mn02,mn03)
    if menu11 != "": 
        mn11 = ""
        mn12 = ""
        mn13 = ""
        mn11 = types.InlineKeyboardButton(text=menu11,callback_data=menu11)
        
        if menu12 != "":
            mn12 = types.InlineKeyboardButton(text=menu12,callback_data=menu12)
        if menu13 != "":
            mn13 = types.InlineKeyboardButton(text=menu13,callback_data=menu13)        
        
        if mn11 != '' and mn12 == '' and mn13 == '':
            print ('[+] 1 меню')
            markup.add(mn11)
            
        if mn11 != '' and mn12 != '' and mn13 == '':
            print ('[+] 2 меню')
            markup.add(mn11,mn12)

        if mn11 != '' and mn12 != '' and mn13 != '':
            print ('[+] 3 меню')
            markup.add(mn11,mn12,mn13)
    if menu21 != "": 
        mn21 = ""
        mn22 = ""
        mn23 = ""
        mn21 = types.InlineKeyboardButton(text=menu21,callback_data=menu21)
        
        if menu22 != "":
            mn22 = types.InlineKeyboardButton(text=menu22,callback_data=menu01)
        if menu23 != "":
            mn23 = types.InlineKeyboardButton(text=menu23,callback_data=menu01)        
        
        if mn21 != '' and mn22 == '' and mn23 == '':
            markup.add(mn21)
            
        if mn21 != '' and mn22 != '' and mn23 == '':
            markup.add(mn21,mn22)
    return markup    
          
### Создаем реферальную ссылку
def referal (user_id,namebot,message_in):
    db,cursor = connect (namebot)
    sql = "select id,user_id,bot,input,output from referalka where bot = '"+namebot+"' and user_id = '"+str(user_id)+"' limit 10"
    cursor.execute(sql)
    label = False
    data = cursor.fetchall()
    for rec in data: 
        label = True
        id,user_id,botname,input,output = rec
    if label == False:
        print ('[+] Создаем реферальную ссылку')
        cursor = db.cursor()  
        sql = "INSERT INTO referalka (`user_id`,`bot`,`input`,`output`) VALUES ('{}','{}','{}','{}')".format (user_id,namebot,message_in,'')
        cursor.execute(sql)
        db.commit()        
        lastid = cursor.lastrowid
        ref = 'https://teleg.run/'+namebot+'?start='+str((lastid+1974)*28+3)
        sql = "UPDATE referalka SET output = '"+ref+"' WHERE `id` = '"+str(lastid)+"'"
        cursor.execute(sql)
        db.commit()
        sql = "UPDATE referalka SET `unique` = "+str((lastid+1974)*28+3)+" WHERE `id` = '"+str(lastid)+"'"
        cursor.execute(sql)
        db.commit()

def save_variable (user_id,variable,value,namebot):
    #import pymysql
    #db = pymysql.connect("127.0.0.1","izofen","podkjf4","main" ,use_unicode=True, charset="utf8mb4" )    
    #cursor = db.cursor()
    db,cursor = connect (namebot)
    sql = "select id,user_id,variable,bot_name,znachen,dateofbirth  from setting where user_id = '"+str(user_id)+"' and  variable = '"+variable+"' and bot_name = '"+namebot+"' limit 1"
    label = "новый"
    cursor.execute(sql)
    results = cursor.fetchall()    
    for row in results:
        label = "в базе"
        #print ("[+] В БАЗЕ")
    if label == "новый":
        #print ("[+] НЕТ В БАЗЕ")
        #cursor = db.cursor()  
        sql = "INSERT INTO setting (`user_id`,`variable`,`bot_name`,`znachen`) VALUES ('{}','{}','{}','{}')".format (user_id,variable,namebot,value)
        cursor.execute(sql)
        db.commit()
    else:
        #cursor = db.cursor()      
        sql = "UPDATE setting SET znachen = '"+value+"' WHERE (`user_id` = '"+str(user_id)+"' and variable = '"+variable+"' and bot_name = '"+namebot+"')"
        cursor.execute(sql)
        db.commit()

def load_variable (user_id,variable,namebot):
    #import pymysql
    db,cursor = connect (namebot)
    variable_out = ''
    #db = pymysql.connect("127.0.0.1","izofen","podkjf4","main" ,use_unicode=True, charset="utf8mb4" )    
    #cursor = db.cursor()
    sql = "select id,user_id,variable,bot_name,znachen,dateofbirth  from setting where user_id = '"+str(user_id)+"' and  variable = '"+variable+"' and bot_name = '"+namebot+"' limit 1"
    cursor.execute(sql)
    results = cursor.fetchall()    
    for row in results:
        id,user_id,variable,bot_name,znachen,dateofbirth = row
        variable_out = znachen;
    return variable_out

def save_FIO (user_id,username,namebot,first_name,last_name):
    #
    #import pymysql
    import time
    #db = pymysql.connect("127.0.0.1","izofen","podkjf4","main" ,use_unicode=True, charset="utf8mb4" )    
    #cursor = db.cursor()
    db,cursor = connect (namebot)
    sql = "select id,user_id,username,bot_name,firstname,lastname from user where user_id = '"+str(user_id)+"' and bot_name = '"+namebot+"'limit 1"
    cursor.execute(sql)
    results = cursor.fetchall()        
    label = "новый"    
    for row in results:    
        #id,user_id,username,bot_name,firstname,lastname = row
        label = "в базе"
    if label == "новый":
        timestamp = int(time.time())
        cursor = db.cursor()  
        sql = "INSERT INTO user (`user_id`,`username`,`bot_name`,`firstname`,`lastname`,`timestamp`) VALUES ('{}','{}','{}','{}','{}',{})".format (user_id,username,namebot,first_name,last_name,timestamp)
        cursor.execute(sql)
        db.commit()        
    
def load__FIO (user_id): 
    #import pymysql
    #db = pymysql.connect("127.0.0.1","izofen","podkjf4","main" ,use_unicode=True, charset="utf8mb4" )    
    #cursor = db.cursor()
    db,cursor = connect (namebot)
    sql = "select id,user_id,username,bot_name,firstname,lastname from user where user_id = '"+str(user_id)+"' limit 1"
    cursor.execute(sql)
    results = cursor.fetchall()        
    label = "новый"    
    for row in results:    
        id,user_id,username,bot_name,firstname,lastname = row
    return username,first_name,last_name

def menu_key (db,name,namebot):
    from telebot import types
    keyboard = types.InlineKeyboardMarkup(row_width=4)
    #import pymysql
    #db = pymysql.connect("127.0.0.1","izofen","podkjf4","main" ,use_unicode=True, charset="utf8mb4" )    
    #cursor = db.cursor()
    cursor = connect (namebot)
    sql = "select id,name,bot,vid,menu01,menu02,menu03 from menu where line=1 and vid = 'пипка' "
    cursor.execute(sql)
    data = cursor.fetchall()
    for rec in data:  
        id,name,bot,vid,menu01,menu02,menu03 = rec
        if menu01 != "" and menu02 == "" and menu03 == "":
            #markup.row(menu01,menu02,menu03)
            key01 = types.InlineKeyboardButton(text=menu01, callback_data = menu01)
            keyboard.add(key01)
    return keyboard
    
def menu_stat (menu01,menu02,menu03,menu11,menu12,menu13,menu21,menu22,menu23):
    from telebot import types
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if menu01 != "":
        markup.row(menu01,menu02,menu03)
    if menu11 != "": 
        markup.row(menu11,menu12,menu13)
    if menu21 != "": 
        markup.row(menu21,menu22,menu23)
    return markup
    
def connect (namebot):
    import pymysql
    db = pymysql.connect("192.168.0.85","izofen","podkjf4","main" ,use_unicode=True, charset="utf8mb4" )
    cursor = db.cursor()
    return db,cursor

def proxy (namebot):
    db,cursor = connect (namebot)
    sql = "select id,ip,login,password,port,tip from proxy where tip = '{}' limit 1".format('telegram')
    cursor.execute(sql)
    data = cursor.fetchall()
    id = 0
    for rec in data: 
        id,ip,login,password,port,tip = rec
    if id != 0:
        proxy = {'https':'http://{}:{}@{}:{}'.format(password,login,ip,port)}
        print ('[+]',proxy)
        return proxy
    else:
        return 'error'
    
def get_token (namebot):
    db,cursor = connect (namebot)
    sql = "select id,name,id_comment,token,about from bots where name = '{}' limit 1;".format(namebot)
    cursor.execute(sql)
    data = cursor.fetchall()
    id = 0
    for rec in data: 
        id,name,id_comment,token,about = rec
    if id != 0:
        return token,about
    else:
        return 'error',''

def save_log (namebot,user_id,message,tip,status,command):
    import time
    timestamp = int(time.time())
    db,cursor = connect (namebot)
    sql = "INSERT INTO log_message (`namebot`,`user_id`,`message`,`tip`,`status`,`command`,`timestamp`,`send`) VALUES ('{}','{}','{}','{}','{}','{}','{}',0)".format (namebot,user_id,message,tip,status,command,timestamp)
    cursor.execute(sql)
    db.commit()

def send_message (user_id,message_in,status,namebot,bot):
    ## Поиск входящего сообщения
    db,cursor   = connect (namebot)
    message_out = message_in
    menu        = ''
    sql = "SELECT id,tekegram,text,input,menu,status FROM message where tekegram = '"+str(namebot)+"' and input = '"+str(message_in)+"'"
    met_find = 0
    cursor.execute(sql)
    data = cursor.fetchall()
    for rec in data: 
        id_s,tekegram_s,text_s,input_s,menu_s,status_s = rec
        message_out = text_s
        menu  = menu_s
        met_find = met_find + 1        
    answer = 'не отправлено'
    if met_find == 0:
        if status == 'S':
            pass
            sql = "INSERT INTO message (`tekegram`,`text`,`input`,`menu`,`status`) VALUES ('{}','{}','{}','{}','{}')".format (namebot,message_in,message_in,'','')
            cursor.execute(sql)
            db.commit()
        #   bot.send_message(user_id,message_out,parse_mode='HTML')
            bot_send (user_id,message_out,"",bot,namebot)
            answer = 'отправлено'
    else:
        message_out = fill_message (user_id,message_out,namebot)
        print ('[+] Ответ: {}, меню: {}'.format(message_out,menu))            
        if menu == '':
            # Сообщение без меню
            #bot.send_message(user_id,message_out,parse_mode='HTML')
            bot_send (user_id,message_out,"",bot,namebot)
            answer = 'отправлено'
        else:
            cursor = db.cursor()
            sql = "select id,name,bot,vid,menu01,menu02,menu03,menu11,menu12,menu13,menu21,menu22,menu23,line from menu where name = '"+str(menu)+"' and bot = '"+namebot+"'"
            cursor.execute(sql)
            data = cursor.fetchall()
            name_m = ""
            for rec in data: 
                id_m,name_m,bot_m,vid_m,menu01_m,menu02_m,menu03_m,menu11_m,menu12_m,menu13_m,menu21_m,menu22_m,menu23_m,line_m = rec
            if name_m != "":  
                if vid_m == "select":
                    markup = menu_stat (menu01_m,menu02_m,menu03_m,menu11_m,menu12_m,menu13_m,menu21_m,menu22_m,menu23_m)
                if vid_m == "command": 
                    menu01_m = fill_menu (user_id,menu01_m)
                    markup = menu_command (menu01_m,menu02_m,menu03_m,menu11_m,menu12_m,menu13_m,menu21_m,menu22_m,menu23_m)
                bot_send (user_id,message_out,markup,bot,namebot)
                answer = 'отправлено'
            else:
                pass
                ## Меню не найдено    
    return answer

def bot_send (user_id,message_out,markup,bot,namebot):
    if markup != '':
        try: 
            bot.send_message(user_id,message_out,parse_mode='HTML',reply_markup=markup)
            send = 'send'
        except:    
            send = 'no send'
    else:
        try:
            bot.send_message(user_id,message_out,parse_mode='HTML')
            send = 'send'
        except:
            send = 'no send'   
    save_log (namebot,user_id,message_out,'out message','',send)

def fill_message (user_id,message_out,namebot):
    message = message_out
    while message.find ('%%') != -1:
        nm = message.find ('%%')
        sl_begin = message [nm+2:]
        ng = sl_begin.find ('%%')
        sl_midel = sl_begin [0:ng]
        message =  sl_begin [ng:]
        print ('[+] sl_midel',sl_midel)
        answer  = load_variable (user_id,sl_midel,namebot) 
        print ('[+] answer',answer)
        zp = "%%"+str(sl_midel)+"%%"
        print ('[+] zp',zp)
        message_out = message_out.replace(zp,str(answer))

    #if message_out.find ('%%Ответ тестирования%%') != -1:
    #    summa_sell  = iz_func.load_variable (user_id,"Ответ тестирования",namebot)
    #    message_out = message_out.replace("%%Ответ тестирования%%", str(summa_sell)) 
              
    #if message_out.find ('%%Номер робота%%') != -1:
    #    total  = iz_func.load_variable (user_id,"Номер робота",namebot)
    #    message_out = message_out.replace("%%Номер робота%%", str(total))    
       
    #if message_out.find ('%%Установленная цена покупки%%') != -1:
    #    total  = iz_func.load_variable (user_id,"Установленная цена покупки",namebot)
    #    message_out = message_out.replace("%%Установленная цена покупки%%", str(total))    
       
    #if message_out.find ('%%Сумма Покупки%%') != -1:
    #    summa_sell  = iz_func.load_variable (user_id,"Сумма Покупки",namebot)
    #    message_out = message_out.replace("%%Сумма Покупки%%", str(summa_sell)+"BTC") 

    return message_out    

def get_message (user_id,message_in,namebot):
    db,cursor   = connect (namebot)
    message_out = message_in
    menu = ''
    sql = "SELECT id,tekegram,text,input,menu,status FROM message where tekegram = '"+str(namebot)+"' and input = '"+str(message_in)+"'"
    cursor.execute(sql)
    data = cursor.fetchall()
    for rec in data: 
        id_s,tekegram_s,text_s,input_s,menu_s,status_s = rec
        message_out = text_s
        menu  = menu_s
    return message_out,menu
    
def get_menu (user_id,menu,st,namebot):    
    db,cursor   = connect (namebot)
    sql = "select id,name,bot,vid,menu01,menu02,menu03,menu11,menu12,menu13,menu21,menu22,menu23,line from menu where name = '"+str(menu)+"' and bot = '"+namebot+"'"
    cursor.execute(sql)
    data = cursor.fetchall()
    name_m = ""
    markup = ''
    for rec in data: 
        id_m,name_m,bot_m,vid_m,menu01_m,menu02_m,menu03_m,menu11_m,menu12_m,menu13_m,menu21_m,menu22_m,menu23_m,line_m = rec
    if name_m != "":  
        if vid_m == "select":
            markup = iz_func.menu_stat (menu01_m,menu02_m,menu03_m,menu11_m,menu12_m,menu13_m,menu21_m,menu22_m,menu23_m)
        if vid_m == "command": 
            menu01_m = fill_menu (user_id,menu01_m)
            markup = iz_func.menu_command (menu01_m,menu02_m,menu03_m,menu11_m,menu12_m,menu13_m,menu21_m,menu22_m,menu23_m)
    return markup        