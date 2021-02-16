#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import bs4
import datetime
import os
import json
import sys

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
        if 'alt="Correio da Manhã" data-original' in str(a):
            link = a["data-original"]
            response = requests.get(link)

            file = open(os.getcwd() + "/jornais/" + "1." + link.split(".")[-1], "wb")
            file.write(response.content)
            file.close()
        elif 'alt="Jornal de Notícias" data-original' in str(a):
            link = a["data-original"]
            response = requests.get(link)

            file = open(os.getcwd() + "/jornais/" + "3." + link.split(".")[-1], "wb")
            file.write(response.content)
            file.close()
        elif 'alt="Público" data-original' in str(a):
            link = a["data-original"]
            response = requests.get(link)

            file = open(os.getcwd() + "/jornais/" + "4." + link.split(".")[-1], "wb")
            file.write(response.content)
            file.close()
        elif 'alt="Diário de Notícias" data-original' in str(a):
            link = a["data-original"]
            response = requests.get(link)

            file = open(os.getcwd() + "/jornais/" + "5." + link.split(".")[-1], "wb")
            file.write(response.content)
            file.close()
        elif 'alt="A Bola" data-original' in str(a):
            link = a["data-original"]
            response = requests.get(link)

            file = open(os.getcwd() + "/jornais/" + "6." + link.split(".")[-1], "wb")
            file.write(response.content)
            file.close()
        elif 'alt="Record" data-original' in str(a):
            link = a["data-original"]
            response = requests.get(link)

            file = open(os.getcwd() + "/jornais/" + "7." + link.split(".")[-1], "wb")
            file.write(response.content)
            file.close()
        elif 'alt="O Jogo" data-original' in str(a):
            link = a["data-original"]
            response = requests.get(link)

            file = open(os.getcwd() + "/jornais/" + "8." + link.split(".")[-1], "wb")
            file.write(response.content)
            file.close()
        elif 'alt="Expresso" data-original' in str(a):
            link = a["data-original"]
            response = requests.get(link)

            file = open(os.getcwd() + "/jornais/" + "9." + link.split(".")[-1], "wb")
            file.write(response.content)
            file.close()
        else:
            pass

