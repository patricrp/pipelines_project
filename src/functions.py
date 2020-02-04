import requests
import os
from dotenv import load_dotenv
import matplotlib.pyplot as plt
from fpdf import FPDF 
import pandas as pd
import sys

#Function to get the video id from the url
load_dotenv()
def video_id(url):
    return url.split("=")[-1]

#Function to look if a country is mentioned on the description
def buscandoAWally(paises,descripcion):
    for pais in paises:
        try:
            if re.findall(f'{pais}', descripcion)[0] == pais:
                return pais
        except:
            pass
#Function to get video views

def requestYoutube(id_video, token):
    token = os.getenv("YOUTUBE_APIKEY")
    if not token:
        raise ValueError("You must set a YOUTUBE_APIKEY token")
    
    url = "https://www.googleapis.com/youtube/v3/videos"
    
    print(f"Requesting data from {url}")
    params = {"part":"statistics",
               "id":id_video,
               "key":token}
    res = requests.get(url,params=params)
    if res.status_code != 200:
        print(res.text)
        raise ValueError("Bad Response")
    return res.json()

#Function to get video date
def requestYoutubeYear(id_video, token):
    token = os.getenv("YOUTUBE_APIKEY")
    if not token:
        raise ValueError("You must set a YOUTUBE_APIKEY token")
    
    url = "https://www.googleapis.com/youtube/v3/videos"
    
    print(f"Requesting data from {url}")
    params = {"part":"snippet",
               "id":id_video,
               "key":token}
    res = requests.get(url,params=params)
    if res.status_code != 200:
        print(res.text)
        raise ValueError("Bad Response")
    return res.json()

#Get total views for a country, year
def totalViews(pais,year):
    df = pd.read_csv('output/data.csv', dtype = 'str') 
    Visualizaciones = df[(df['Pais'] == f'{pais}') & (df['Year'] == f'{str(year)}')]
    return Visualizaciones['Visualizaciones'].astype('int').sum()

#Get total views for a country group by year
'''def viewsPerYear(pais):
    df = pd.read_csv('output/data.csv', dtype = 'str')
    VisualizacionesPorYear = df[(df['Pais'] == f'{pais}')]
    visualizacionesYouTube = VisualizacionesPorYear.groupby('Year').agg({'Visualizaciones':'sum'}).astype('int').plot.bar()
    plt.savefig('visualizaciones.png')
    return VisualizacionesPorYear

#Create PDF
def createPDF():
    pdf = FPDF('P','mm','A4')
    pdf.add_page()
    pdf.image('visualizaciones.png')
    return pdf.output("visualizacionesYouTube.pdf",'F')'''