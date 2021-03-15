#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import bs4
import datetime
import os
import json
import locale
import sys
from datetime import datetime, timedelta


def dados_covid():
    #locale.setlocale(locale.LC_ALL, 'pt_PT')
    text = ''
    try:
        hoje = datetime.now()
        ontem = hoje - timedelta(1)

        hoje_string = datetime.strftime(hoje, '%d-%m-%Y')
        ontem_string = datetime.strftime(ontem, '%d-%m-%Y')

        hojereq = requests.get("https://covid19-api.vost.pt/Requests/get_entry/" + hoje_string).json()
        ontemreq = requests.get("https://covid19-api.vost.pt/Requests/get_entry/" + ontem_string).json()

        confirmados_hoje = list((hojereq["confirmados"]).values())[0]
        confirmados_hoje_string = (locale.format_string("%d", int(confirmados_hoje), grouping=True)).replace(" ", ".")
        confirmados_ontem = list((ontemreq["confirmados"]).values())[0]
        diferencaconfirmados_string = f'{(confirmados_hoje - confirmados_ontem):+}'
        ###
        internados_hoje = list((hojereq["internados"]).values())[0]
        internados_hoje_string = (locale.format_string("%d", int(internados_hoje), grouping=True)).replace(" ", ".")
        internados_ontem = list((ontemreq["internados"]).values())[0]
        diferencainternados_string = f'{(int(internados_hoje - internados_ontem)):+}'
        ###
        internadosUCI_hoje = list((hojereq["internados_uci"]).values())[0]
        internadosUCI_hoje_string = (locale.format_string("%d", int(internadosUCI_hoje), grouping=True)).replace(" ", ".")
        internadosUCI_ontem = list((ontemreq["internados_uci"]).values())[0]
        diferencainternadosUCI_string = f'{(int(internadosUCI_hoje - internadosUCI_ontem)):+}'
        ###
        obitos_hoje = list((hojereq["obitos"]).values())[0]
        obitos_hoje_string = (locale.format_string("%d", int(obitos_hoje), grouping=True)).replace(" ", ".")
        obitos_ontem = list((ontemreq["obitos"]).values())[0]
        diferencaobitos_string = f'{(obitos_hoje - obitos_ontem):+}'

        ###
        recuperados_hoje = list((hojereq["recuperados"]).values())[0]
        recuperados_hoje_string = (locale.format_string("%d", int(recuperados_hoje), grouping=True)).replace(" ", ".")
        recuperados_ontem = list((ontemreq["recuperados"]).values())[0]
        diferencarecuperados_string = f'{(recuperados_hoje - recuperados_ontem):+}'

        text = "Boletim DGS {data} \n" \
               "Casos Confirmados: {confirmadoshoje} ({diffconfirmados})\n" \
               "Número de Internados: {internadoshoje} ({diffinternados})\n" \
               "Número de Internados em UCI: {internadosucihoje} ({diffinternadosuci}) \n" \
               "Óbitos: {obitoshoje} ({diffobitos}) \n" \
               "Recuperados: {recuperadoshoje} ({diffrecuperados})\n" \
               "Fonte: DGS/@VOSTPT".format(data=hoje_string,
                                           confirmadoshoje=confirmados_hoje_string.replace(" ", "."),
                                           diffconfirmados=diferencaconfirmados_string,
                                           internadoshoje=internados_hoje_string.replace(" ", "."),
                                           diffinternados=diferencainternados_string,
                                           internadosucihoje=internadosUCI_hoje_string.replace(" ", "."),
                                           diffinternadosuci=diferencainternadosUCI_string,
                                           obitoshoje=obitos_hoje_string.replace(" ", "."),
                                           diffobitos=diferencaobitos_string,
                                           recuperadoshoje=recuperados_hoje_string.replace(" ", "."),
                                           diffrecuperados=diferencarecuperados_string)
        
    except:
        hoje_hoje = datetime.now()
        hoje = datetime.now() - timedelta(1)
        ontem = hoje_hoje - timedelta(2)

        hoje_string = datetime.strftime(hoje, '%d-%m-%Y')
        ontem_string = datetime.strftime(ontem, '%d-%m-%Y')

        hojereq = requests.get("https://covid19-api.vost.pt/Requests/get_entry/" + hoje_string).json()
        ontemreq = requests.get("https://covid19-api.vost.pt/Requests/get_entry/" + ontem_string).json()

        confirmados_hoje = list((hojereq["confirmados"]).values())[0]
        confirmados_hoje_string = (locale.format_string("%d", int(confirmados_hoje), grouping=True)).replace(" ", ".")
        confirmados_ontem = list((ontemreq["confirmados"]).values())[0]
        diferencaconfirmados_string = f'{(confirmados_hoje - confirmados_ontem):+}'
        ###
        internados_hoje = list((hojereq["internados"]).values())[0]
        internados_hoje_string = (locale.format_string("%d", int(internados_hoje), grouping=True)).replace(" ", ".")
        internados_ontem = list((ontemreq["internados"]).values())[0]
        diferencainternados_string = f'{(int(internados_hoje - internados_ontem)):+}'
        ###
        internadosUCI_hoje = list((hojereq["internados_uci"]).values())[0]
        internadosUCI_hoje_string = (locale.format_string("%d", int(internadosUCI_hoje), grouping=True)).replace(" ", ".")
        internadosUCI_ontem = list((ontemreq["internados_uci"]).values())[0]
        diferencainternadosUCI_string = f'{(int(internadosUCI_hoje - internadosUCI_ontem)):+}'
        ###
        obitos_hoje = list((hojereq["obitos"]).values())[0]
        obitos_hoje_string = (locale.format_string("%d", int(obitos_hoje), grouping=True)).replace(" ", ".")
        obitos_ontem = list((ontemreq["obitos"]).values())[0]
        diferencaobitos_string = f'{(obitos_hoje - obitos_ontem):+}'

        ###
        recuperados_hoje = list((hojereq["recuperados"]).values())[0]
        recuperados_hoje_string = (locale.format_string("%d", int(recuperados_hoje), grouping=True)).replace(" ", ".")
        recuperados_ontem = list((ontemreq["recuperados"]).values())[0]
        diferencarecuperados_string = f'{(recuperados_hoje - recuperados_ontem):+}'

        text = "Boletim DGS {data} \n" \
               "Casos Confirmados: {confirmadoshoje} ({diffconfirmados})\n" \
               "Número de Internados: {internadoshoje} ({diffinternados})\n" \
               "Número de Internados em UCI: {internadosucihoje} ({diffinternadosuci}) \n" \
               "Óbitos: {obitoshoje} ({diffobitos}) \n" \
               "Recuperados: {recuperadoshoje} ({diffrecuperados})\n" \
               "Fonte: DGS/@VOSTPT".format(data=hoje_string,
                                           confirmadoshoje=confirmados_hoje_string.replace(" ", "."),
                                           diffconfirmados=diferencaconfirmados_string,
                                           internadoshoje=internados_hoje_string.replace(" ", "."),
                                           diffinternados=diferencainternados_string,
                                           internadosucihoje=internadosUCI_hoje_string.replace(" ", "."),
                                           diffinternadosuci=diferencainternadosUCI_string,
                                           obitoshoje=obitos_hoje_string.replace(" ", "."),
                                           diffobitos=diferencaobitos_string,
                                           recuperadoshoje=recuperados_hoje_string.replace(" ", "."),
                                           diffrecuperados=diferencarecuperados_string)

    return text



def dados_covidinfodiaria():
    texttoday = ''
    #locale.setlocale(locale.LC_ALL, 'pt_PT')
    try:
        hoje = datetime.now()
        ontem = hoje - timedelta(1)

        hoje_string = datetime.strftime(hoje, '%d-%m-%Y')
        ontem_string = datetime.strftime(ontem, '%d-%m-%Y')

        hojereq = requests.get("https://covid19-api.vost.pt/Requests/get_entry/" + hoje_string).json()
        ontemreq = requests.get("https://covid19-api.vost.pt/Requests/get_entry/" + ontem_string).json()

        confirmados_hoje = list((hojereq["confirmados"]).values())[0]
        confirmados_hoje_string = (locale.format_string("%d", int(confirmados_hoje), grouping=True)).replace(" ", ".")
        confirmados_ontem = list((ontemreq["confirmados"]).values())[0]
        diferencaconfirmados_string = f'{(confirmados_hoje - confirmados_ontem):+}'
        ###
        internados_hoje = list((hojereq["internados"]).values())[0]
        internados_hoje_string = (locale.format_string("%d", int(internados_hoje), grouping=True)).replace(" ", ".")
        internados_ontem = list((ontemreq["internados"]).values())[0]
        diferencainternados_string = f'{(int(internados_hoje - internados_ontem)):+}'
        ###
        internadosUCI_hoje = list((hojereq["internados_uci"]).values())[0]
        internadosUCI_hoje_string = (locale.format_string("%d", int(internadosUCI_hoje), grouping=True)).replace(" ", ".")
        internadosUCI_ontem = list((ontemreq["internados_uci"]).values())[0]
        diferencainternadosUCI_string = f'{(int(internadosUCI_hoje - internadosUCI_ontem)):+}'
        ###
        obitos_hoje = list((hojereq["obitos"]).values())[0]
        obitos_hoje_string = (locale.format_string("%d", int(obitos_hoje), grouping=True)).replace(" ", ".")
        obitos_ontem = list((ontemreq["obitos"]).values())[0]
        diferencaobitos_string = f'{(obitos_hoje - obitos_ontem):+}'

        ###
        recuperados_hoje = list((hojereq["recuperados"]).values())[0]
        recuperados_hoje_string = (locale.format_string("%d", int(recuperados_hoje), grouping=True)).replace(" ", ".")
        recuperados_ontem = list((ontemreq["recuperados"]).values())[0]
        diferencarecuperados_string = f'{(recuperados_hoje - recuperados_ontem):+}'

        texttoday = "Boletim DGS {data} \n" \
               "Casos Confirmados: {confirmadoshoje} ({diffconfirmados})\n" \
               "Número de Internados: {internadoshoje} ({diffinternados})\n" \
               "Número de Internados em UCI: {internadosucihoje} ({diffinternadosuci}) \n" \
               "Óbitos: {obitoshoje} ({diffobitos}) \n" \
               "Recuperados: {recuperadoshoje} ({diffrecuperados})\n" \
               "Fonte: DGS/@VOSTPT".format(data=hoje_string,
                                           confirmadoshoje=confirmados_hoje_string.replace(" ", "."),
                                           diffconfirmados=diferencaconfirmados_string,
                                           internadoshoje=internados_hoje_string.replace(" ", "."),
                                           diffinternados=diferencainternados_string,
                                           internadosucihoje=internadosUCI_hoje_string.replace(" ", "."),
                                           diffinternadosuci=diferencainternadosUCI_string,
                                           obitoshoje=obitos_hoje_string.replace(" ", "."),
                                           diffobitos=diferencaobitos_string,
                                           recuperadoshoje=recuperados_hoje_string.replace(" ", "."),
                                           diffrecuperados=diferencarecuperados_string)
        
    except:
        texttoday = "Erro"

    return texttoday

