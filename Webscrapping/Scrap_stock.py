# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 00:07:52 2021

@author: mkostner
"""

#elite center
from colorama import init,Fore,Back,Style
init(convert=True)

print(Style.RESET_ALL)
#request

import pandas as pd

#import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

import urllib3
urllib3.disable_warnings()
import time
salida=pd.DataFrame()

        
urls=['https://www.Pagína_Scrapping.cl/equipos/componentes-informaticos/tarjetas-de-video.html'] # lista con los url
tienda='Tienda XX'
for url in urls: #loop url

    req = urllib3.PoolManager()
    r = req.request('GET', url)#generamos el request
    soup = BeautifulSoup(r.data,'html.parser')#con transformamos el HTML a Soup             
    mydivs = soup.find_all("div", {"class": "product-item-info"}) #buscamos la galeria de productos
    
    for i in range(len(mydivs)): #iteramos por cada uno de los productos
        try:
            link=mydivs[i].a['href'] #sacamos el link 
            var=mydivs[i].findAll('a',{'class':'product-item-link'})[0].text.strip().upper() #nombre del producto
            if ("RTX" in var.upper())|("GTX" in var.upper())|("RADEON" in var.upper()): #nos quedamos solo con los productos que nos interesa
                stock='En Stock' #como todos los productos que estan visibles están disponibles no buscamos el stock sino que le ponemos un string "En Stock"
                
                precio_efect=int(mydivs[i].findAll('span',{'class':'price'})[0].text.strip().replace('$','').replace('.','')) #precio
  
                salida=salida.append([[tienda,var,precio_efect,"En stock",link]]) #guardamos el resultado
                                  
        except:
            pass          

    try:
        salida.columns=["Tienda","Descripcion","Efectivo","stock",'link'] #una vez que tenemos todos los resultados le cambiamos los nombres a las columndas
    except:
        pass
    
    
    