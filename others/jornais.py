#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import bs4
import datetime
import os
import json
import sys

def getjournalnumber(nome):
    jornais = {
                "Correio da Manhã": ["1", "https://www.vercapas.com/capa/correio-da-manha.html"],
                "Jornal i":  ["2", "https://www.vercapas.com/capa/i.html"],
                "Jornal de Notícias":  ["3", "https://www.vercapas.com/capa/jornal-de-noticias.html"],
                "Público":  ["4", "https://www.vercapas.com/capa/publico.html"],
                "Diário de Notícias":  ["5", "https://www.vercapas.com/capa/diario-de-noticias.html"],
                "A Bola":  ["6", "https://www.vercapas.com/capa/a-bola.html"],
                "Record":  ["7", "https://www.vercapas.com/capa/record.html"],
                "O Jogo": ["8", "https://www.vercapas.com/capa/o-jogo.html"],
                "Expresso":  ["9", "https://www.vercapas.com/capa/expresso.html"],
                "Jornal de Negócios": ["10", "https://www.vercapas.com/capa/jornal-de-negocios.html"],
                "Jornal Económico": ["11", "https://www.vercapas.com/capa/jornal-economico.html"],
                "Visão": ["12", "https://www.vercapas.com/capa/visao.html"],
                "Sábado": ["13", "https://www.vercapas.com/capa/sabado.html"],
                "Cristina": ["14", "https://www.vercapas.com/capa/cristina.html"],
                "Exame": ["15", "https://www.vercapas.com/capa/exame.html"],
                "O Benfica": ["16", "https://www.vercapas.com/capa/o-benfica.html"],
                "Jornal Sporting": ["17", "https://www.vercapas.com/capa/jornal-sporting.html"],
                "Dragões": ["18", "https://www.vercapas.com/capa/dragoes.html"],
                "PC Guia": ["19", "https://www.vercapas.com/capa/pc-guia.html"],
                "Mundo da Fotografia Digital": ["20", "https://www.vercapas.com/capa/o-mundo-da-fotografia-digital.html"],
                "Programar": ["21", "https://www.vercapas.com/capa/programar.html"],
                "Motor": ["22", "https://www.vercapas.com/capa/motor.html"],
                "Autohoje": ["23", "https://www.vercapas.com/capa/autohoje.html"],
                "TopGear": ["24", "https://www.vercapas.com/capa/topgear.html"],
                "Teleculinária": ["25", "https://www.vercapas.com/capa/teleculinaria.html"],
                }
    return jornais[nome]


def showall_jornais():
    texto = "Os Jornais / revistas disponiveis são:\n" \
            "1. Correio da Manhã\n" \
            "2. Jornal i\n" \
            "3. Jornal de Notícias\n" \
            "4. Público\n" \
            "5. Diário de Notícias\n" \
            "6. A Bola\n" \
            "7. Record\n" \
            "8. O Jogo\n" \
            "9. Expresso\n" \
            "10. Jornal de Negócios\n" \
            "11. Jornal Económico\n" \
            "12. Visão\n" \
            "13. Sábado\n" \
            "14. Cristina\n" \
            "15. Exame\n" \
            "16. O Benfica\n" \
            "17. Jornal Sporting\n" \
            "18. Dragões\n" \
            "19. PC Guia\n" \
            "20. O Mundo da Fotografia Digital\n" \
            "21. Programar\n" \
            "22. Motor\n" \
            "23. Autohoje\n" \
            "24. TopGear\n" \
            "25. Teleculinária\n\n" \
            "***Para escolher os que quer receber diariamente, escreva os números separados por ',' , por exemplo " \
            "1, 2, 3, 5, 21***. Se pretender só 1 jornal, escreva o número do mesmo. \n\n" \
            "Existem muitos outros jornais. Se houver algum que queira e não esteja na lista, " \
            "por favor envie mensagem para @souocare."

    return texto

def download_jornais():
    information = requests.get("https://www.vercapas.com/")

    soup = bs4.BeautifulSoup(information.text, features="lxml")
    for a in soup.findAll('img'):
        title = a.get('title')
        try:
            numberofjornal = getjournalnumber(title)
            jornalespecificoimg_html = requests.get(numberofjornal[1])
            soupimgjornal = bs4.BeautifulSoup(jornalespecificoimg_html.text, features="lxml")
            spanimgjornal = soupimgjornal.find_all("span", {"class": "center_text"})
            images = spanimgjornal[0].findAll('img')
            linkimgjornal = images[0]['src']
            
            downloadimage = requests.get(linkimgjornal)
            file = open(os.getcwd() + "/others/jornais/" + str(numberofjornal[0]) + "." + linkimgjornal.split(".")[-1], "wb")
            file.write(downloadimage.content)
            file.close()
        except:
            pass