#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import telepot
import telepot.namedtuple
from others.weather import get_weatherinicialcity, get_weatheriniciallatlon, get_forecast_city, get_weather_city
from others.jornais import showall_jornais, download_jornais
from others.covid_dados import dados_covid, dados_covidinfodiaria
######
import traceback
import datetime
import os
import sqlite3
from dotenv import load_dotenv

load_dotenv()

def start_menu(chatid):
    markup = telepot.namedtuple.ReplyKeyboardMarkup(
        keyboard=[["Informação de utilização"], ['Guardar/Modificar Localização'], ["Modificar Jornais"], ["Obter Meteorologia"], ["Obter Dados Covid"], ["Obter Jornais"]])

    bot.sendMessage(chat_id=chatid,
                    text="Bem-vindo ao Bot das informações diárias. As informações diárias são enviadas diáriamente, "
                        "de várias informações.\n"
                        "Caso queira guardar/modificar a sua localização para a metereologia diária, clique nessa opção.\n"
                        "Caso queira modificar os jornais/revistas apresentadas, clique nessa opção. \n\n"
                        "Alguma informação mais, contacte-me @souocare. ", reply_markup=markup, parse_mode='Markdown',
                        disable_web_page_preview=True)


def save_locationweather(chat_id):
    try:
        lat = response[0]['message']["chat"]["location"]["latitude"]
        lon = response[0]['message']["chat"]["location"]["longitude"]

        info = get_weatheriniciallatlon(lat, lon)
        if str(info["cod"]) == "200":
            cursor.execute("Update Users "
                           "set [Loc_Meterologia] = '{loc}' "
                           "where [user_id] = {iduser} ;".format(iduser=chat_id,
                                                                loc=info["name"]))
            connection.commit()

            bot.sendMessage(chat_id=chat_id,
                            text="A localização foi guardada com sucesso! Foi guardada com a localidade "
                                 "***{cidade}***. Se não achar que é o "
                                 "mais correto, indique o nome. Abaixo, vai-lhe aparecer a metereologia para a localização dada.".format(cidade=info["name"]), parse_mode='Markdown')
        else:
            bot.sendMessage(chat_id=chat_id,
                            text="Não foi possivel guardar a localização. Por favor, tente "
                                 "novamente, ou indique o nome da localidade.",
                            parse_mode='Markdown')

    except:
        try:
            cidade = response[0]['message']['text']
            info = get_weatherinicialcity(cidade)
            if str(info["cod"]) == "200":
                cursor.execute("Update Users "
                               "set [Loc_Meterologia] = '{loc}' "
                               "where [user_id] = {iduser} ;".format(iduser=chat_id,
                                                                    loc=info["name"]))
                connection.commit()
                bot.sendMessage(chat_id=chat_id,
                                text="A localização foi guardada com sucesso! Foi guardada com a localidade "
                                     "***{cidade}***. Se não achar que é o "
                                     "mais correto, indique o nome. Abaixo, vai-lhe aparecer a metereologia para a localização dada.".format(cidade=info["name"]), parse_mode='Markdown')
            else:
                bot.sendMessage(chat_id=chat_id,
                                text="Não foi possivel guardar a localização. Por favor, tente "
                                     "novamente, ou indique o nome da localidade.",
                                parse_mode='Markdown')
        except:
            bot.sendMessage(chat_id=chat_id,
                            text="Não foi possivel guardar a localização. Por favor, tente "
                                 "novamente, ou indique o nome da localidade. \n\n"
                                 "Se receber esta mensagem várias vezes, por faovr contacte @souocare .",
                            parse_mode='Markdown')

def save_jornais(chat_id):
    jornais = response[0]['message']['text']
    lista_idsjornais = []
    for idjornal in jornais.split(","):
        lista_idsjornais.append(str(idjornal).replace(" ","") + " ")

    cursor.execute("Update Users "
                   "set [Ids_jornais] = '{idsjornais}' "
                   "where [user_id] = {iduser} ;".format(iduser=chat_id,
                                                        idsjornais=str(lista_idsjornais).replace("'", "")))
    connection.commit()
    bot.sendMessage(chat_id=chat_id,
                    text="As suas opções forem guardadas! Caso queira alterar, é só fazer o comando /modificar_jornais.\n"
                         "Caso queira adicionar outro jornal que não esteja na lista, por favor envie mensagem para @souocare.",
                    parse_mode='Markdown')



load_dotenv()

connection = sqlite3.connect('Users.db')
cursor = connection.cursor()

bot = telepot.Bot(token=os.getenv('Telegram_Token')) #normal

covidtoday = 0
downloadjornaisverificacao = 0
envioinfodiaria = 0


if __name__ == '__main__':
    offset = 0
    while True:
        now = datetime.datetime.now()
        
        if int(now.hour) == 6 and  int(now.minute) == 1:
            downloadjornaisverificacao = 0
            envioinfodiaria = 0

        if int(now.hour) == 7 and int(downloadjornaisverificacao) == 0:
            for file in os.listdir(os.getcwd() + "/others/jornais"):
                if file.endswith('.jpg'):
                    os.remove(os.getcwd() + "/others/jornais/" + file)
            download_jornais()
            downloadjornaisverificacao = 1

        if int(now.hour) == 9 and int(envioinfodiaria) == 0:
            print("Envio diário comecou")
            cursor.execute("select user_id, [Name] ,[Loc_Meterologia], [Ids_jornais]  from Users;")
            check_idbd = cursor.fetchall()
            if len(check_idbd) > 0:
                dadoscovid = dados_covid()
                for user in check_idbd:
                    jornais = user[3].strip('][').split(', ')
                    bot.sendMessage(chat_id=user[0],
                                    text="Bom dia, {nome}! Aqui vão todas as informações do dia.\nAbaixo estão "
                                         "as capas de hoje.".format(nome=user[1]),
                                    parse_mode='Markdown')

                    for jornal in jornais:
                        pf = open(os.getcwd() + "/others/jornais/" + str(jornal).replace(" ", "") + ".jpg", mode="rb")
                        bot.sendPhoto(chat_id=user[0], photo=pf)
                        
                    if user[2] == None:
                        pass
                    else:
                        try:
                            weather_now = get_weather_city(user[2])
                            meterologia = get_forecast_city(user[2])

                            bot.sendMessage(chat_id=user[0],
                                            text=weather_now,
                                            parse_mode='Markdown')

                            bot.sendMessage(chat_id=user[0],
                                            text=meterologia,
                                            parse_mode='Markdown')

                        except:
                            bot.sendMessage(chat_id=user[0],
                                            text="A metereologia não está disponivel de momento. Por favor, tente mais tarde.",
                                            parse_mode='Markdown')

                    bot.sendMessage(chat_id=user[0],
                                    text=dadoscovid,
                                    parse_mode='Markdown')
                print("Dados enviados!")

            else:
                pass
            
            envioinfodiaria = 1
        
        if (int(now.hour) == 15 and int(now.minute) == 0 and int(now.second) == 0) or (
                int(now.hour) == 15 and int(now.minute) == 15 and int(now.second) == 0) or (
                int(now.hour) == 15 and int(now.minute) == 30 and int(now.second) == 0) or (
                int(now.hour) == 15 and int(now.minute) == 45 and int(now.second) == 0) or (
                int(now.hour) == 16 and int(now.minute) == 0 and int(now.second) == 0) or (
                int(now.hour) == 16 and int(now.minute) == 15 and int(now.second) == 0) or (
                int(now.hour) == 16 and int(now.minute) == 30 and int(now.second) == 0) or (
                int(now.hour) == 16 and int(now.minute) == 45 and int(now.second) == 0) or (
                int(now.hour) == 17 and int(now.minute) == 45 and int(now.second) == 0):
            if covidtoday == 0:
                dadoscovid = dados_covidinfodiaria()
                if dadoscovid == 'Erro':
                    pass
                else:
                    cursor.execute("select user_id, [Name] ,[Loc_Meterologia], [Ids_jornais]  from Users;")
                    check_idbd = cursor.fetchall()
                    if len(check_idbd) > 0:
                        dadoscovid = dados_covid()
                        for user in check_idbd:
                            bot.sendMessage(chat_id=user[0],
                                                text=dadoscovid,
                                                parse_mode='Markdown')
                    covidtoday = 1
            else:
                pass
        

                
            

        try:
            response = bot.getUpdates(offset=offset)

            if len(response) == 0:
                pass
            else:
                chat_id = response[0]["message"]['from']['id']
                cursor.execute("select user_id from Users where [user_id] = {userid} ;".format(userid=chat_id))
                check_idbdsdada = cursor.fetchall()
                print(check_idbdsdada)
                if len(check_idbdsdada) > 0:
                    pass
                else:
                    nome = ""
                    try:
                        nome = nome + str(response[0]['message']["chat"]["first_name"]) + " " + \
                               response[0]['message']["chat"]["last_name"]
                    except:
                        nome = nome + str(response[0]['message']["chat"]["first_name"])

                    cursor.execute("insert into Users ([user_id], [Name], [Ids_jornais]) "
                                   "values ({iduser}, '{nome}', '[1, 3, 4, 7, 9]');".format(iduser=chat_id,
                                                                         nome=nome))
                    connection.commit()


                try:
                    if response[0]['message']['text'] == '/start' or \
                            response[0]['message']['text'] == '/ajuda' or \
                            response[0]['message']['text'] == '/comecar' or response[0]['message']['text'] == 'Informação de utilização':
                        start_menu(response[0]["message"]['from']['id'])

                    elif response[0]['message']['text'] == '/guardar_local_tempo' \
                            or response[0]['message']['text'] == 'Guardar/Modificar Localização':
                        cursor.execute("Update Users "
                                       "set [last_option] = 2 "
                                       "where [user_id] = {iduser} ;".format(iduser=chat_id))
                        connection.commit()

                        bot.sendMessage(chat_id=chat_id,
                                        text="Para colocar a sua localização, basta escrever o local que pretende.\n"
                                             "Se quiser, pode também enviar as suas coordenadas, clicando no "
                                             "botão inferior esquerdo, e clicando em 'Localização'. \n\n"
                                             "Caso queira mudar a sua localização, "
                                             "basta fazer ***/guardar_local_tempo***.", parse_mode='Markdown')

                    elif response[0]['message']['text'] == '/modificar_jornais' \
                            or response[0]['message']['text'] == 'Modificar Jornais':
                        cursor.execute("Update Users "
                                       "set [last_option] = 3 "
                                       "where [user_id] = {iduser} ;".format(iduser=chat_id))
                        connection.commit()

                        texto = showall_jornais()
                        bot.sendMessage(chat_id=chat_id,
                                        text=texto, parse_mode='Markdown')


                    elif response[0]['message']['text'] == '/obter_meteorologia' \
                            or response[0]['message']['text'] == 'Obter Meteorologia':
                        cursor.execute("select [Loc_Meterologia] from Users where [user_id] = {userid} ;".format(userid=chat_id))
                        check_local = cursor.fetchone()[0]
                        if check_local == None:
                            bot.sendMessage(chat_id=chat_id,
                                            text="Não tem nenhuma localização predifinida. Por favor, use o comando /guardar_local_tempo para configurar.",
                                            parse_mode='Markdown')
                        try:
                            weather_now = get_weather_city(check_local)
                            meterologia = get_forecast_city(check_local)

                            bot.sendMessage(chat_id=chat_id,
                                            text=weather_now,
                                            parse_mode='Markdown')

                            bot.sendMessage(chat_id=chat_id,
                                            text=meterologia,
                                            parse_mode='Markdown')

                        except:
                            bot.sendMessage(chat_id=chat_id,
                                            text="A metereologia não está disponivel de momento. Por favor, tente mais tarde.",
                                            parse_mode='Markdown')
                        
                            
                    elif response[0]['message']['text'] == '/obter_jornais' \
                            or response[0]['message']['text'] == 'Obter Jornais':
                        cursor.execute("select [Ids_jornais] from Users where [user_id] = {userid} ;".format(userid=chat_id))
                        check_jornais = cursor.fetchone()[0]
                        try:
                            jornais = check_jornais.strip('][').split(', ')
                            for jornal in jornais:
                                pf = open(os.getcwd() + "/others/jornais/" + str(jornal).replace(" ", "") + ".jpg", mode="rb")
                                bot.sendPhoto(chat_id=chat_id, photo=pf)
                        except:
                            download_jornais()
                            jornais = check_jornais.strip('][').split(', ')
                            for jornal in jornais:
                                pf = open(os.getcwd() + "/others/jornais/" + str(jornal).replace(" ", "") + ".jpg", mode="rb")
                                bot.sendPhoto(chat_id=chat_id, photo=pf)
                            
                            
                    elif response[0]['message']['text'] == '/obter_dadoscovid' \
                            or response[0]['message']['text'] == 'Obter Dados Covid':
                        dadoscovid = dados_covid()
                        bot.sendMessage(chat_id=chat_id,
                                        text=dadoscovid,
                                        parse_mode='Markdown')
                        


                    elif response[0]['message']['chat']['id'] == 519356699 and (response[0]['message']['text']).startswith(
                            "Aviso:\n"):
                        cursor.execute("select user_id from Users;")
                        check_idbd = cursor.fetchall()
                        for user in check_idbd:
                            bot.sendMessage(chat_id=user[0],
                                            text=((response[0]['message']['text'])[7:]).replace("*", "***"), parse_mode='Markdown')



                    else:
                        cursor.execute("select last_option from Users "
                                       "where [user_id] = {userid} ;".format(userid=chat_id))
                        check_idbd = cursor.fetchone()[0]
                        if check_idbd == None:
                            bot.sendMessage(chat_id=response[0]["message"]['from']['id'],
                                    text="De momento não é possivel obter a informação. Tente mais tarde",
                                    parse_mode='markdown')
                        else:
                            if int(check_idbd) == 2:
                                save_locationweather(chat_id)
                            elif int(check_idbd) == 3:
                                save_jornais(chat_id)
                            else:
                                pass

                except:
                    bot.sendMessage(chat_id=response[0]["message"]['from']['id'],
                                    text="De momento não é possivel obter a informação. Tente mais tarde",
                                    parse_mode='markdown')
                    error = str(traceback.format_exc())
                    f = open("log_file.txt", "w")
                    f.write(error + "\n\n\n")
                    f.close()

            if response:
                try:
                    offset = response[-1]["update_id"] + 1  # penso que isto é para não receber as mensagens antigas
                except IndexError:
                    pass
        except:
            pass
