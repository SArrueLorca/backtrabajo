from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import os
from pymongo import MongoClient

# read by default 1st sheet of an excel file


class User(BaseModel):
    id: int
     
users= [User(id=1), User(id=2) ]

jsonconsultas= [
    {"Fecha":"2018-02-01","Total consultas":502},{"Fecha":"2018-02-02","Total consultas":532},
    {"Fecha":"2018-02-03","Total consultas":525},{"Fecha":"2018-02-04","Total consultas":398},
    {"Fecha":"2018-02-05","Total consultas":389},{"Fecha":"2018-02-06","Total consultas":442},
    {"Fecha":"2018-02-07","Total consultas":539},{"Fecha":"2018-02-08","Total consultas":396},
    {"Fecha":"2018-02-09","Total consultas":451},{"Fecha":"2018-02-10","Total consultas":397},
    {"Fecha":"2018-02-11","Total consultas":395},{"Fecha":"2018-02-12","Total consultas":423},
    {"Fecha":"2018-02-13","Total consultas":424},{"Fecha":"2018-02-14","Total consultas":515},
    {"Fecha":"2018-02-15","Total consultas":528},{"Fecha":"2018-02-16","Total consultas":491},
    {"Fecha":"2018-02-17","Total consultas":528},{"Fecha":"2018-02-18","Total consultas":499},
    {"Fecha":"2018-02-19","Total consultas":473},{"Fecha":"2018-02-20","Total consultas":496},
    {"Fecha":"2018-02-21","Total consultas":518},{"Fecha":"2018-02-22","Total consultas":384},
    {"Fecha":"2018-02-23","Total consultas":397},{"Fecha":"2018-02-24","Total consultas":535},
    {"Fecha":"2018-02-25","Total consultas":433},{"Fecha":"2018-02-26","Total consultas":518},
    {"Fecha":"2018-02-27","Total consultas":489},{"Fecha":"2018-02-28","Total consultas":454},
    {"Fecha":"2019-02-01","Total consultas":524},{"Fecha":"2019-02-02","Total consultas":493},
    {"Fecha":"2019-02-03","Total consultas":440},{"Fecha":"2019-02-04","Total consultas":385},
    {"Fecha":"2019-02-05","Total consultas":428},{"Fecha":"2019-02-06","Total consultas":478},
    {"Fecha":"2019-02-07","Total consultas":466},{"Fecha":"2019-02-08","Total consultas":504},
    {"Fecha":"2019-02-09","Total consultas":436},{"Fecha":"2019-02-10","Total consultas":407},
    {"Fecha":"2019-02-11","Total consultas":531},{"Fecha":"2019-02-12","Total consultas":440},
    {"Fecha":"2019-02-13","Total consultas":500},{"Fecha":"2019-02-14","Total consultas":509},
    {"Fecha":"2019-02-15","Total consultas":391},{"Fecha":"2019-02-16","Total consultas":466},
    {"Fecha":"2019-02-17","Total consultas":398},{"Fecha":"2019-02-18","Total consultas":420},
    {"Fecha":"2019-02-19","Total consultas":386},{"Fecha":"2019-02-20","Total consultas":389},
    {"Fecha":"2019-02-21","Total consultas":449},{"Fecha":"2019-02-22","Total consultas":498},
    {"Fecha":"2019-02-23","Total consultas":461},{"Fecha":"2019-02-24","Total consultas":437},
    {"Fecha":"2019-02-25","Total consultas":376},{"Fecha":"2019-02-26","Total consultas":385},
    {"Fecha":"2019-02-27","Total consultas":396},{"Fecha":"2019-02-28","Total consultas":465},
    {"Fecha":"2020-02-01","Total consultas":375},{"Fecha":"2020-02-02","Total consultas":398},
    {"Fecha":"2020-02-03","Total consultas":396},{"Fecha":"2020-02-04","Total consultas":443},
    {"Fecha":"2020-02-05","Total consultas":513},{"Fecha":"2020-02-06","Total consultas":380},
    {"Fecha":"2020-02-07","Total consultas":492},{"Fecha":"2020-02-08","Total consultas":436},
    {"Fecha":"2020-02-09","Total consultas":415},{"Fecha":"2020-02-10","Total consultas":470},
    {"Fecha":"2020-02-11","Total consultas":492},{"Fecha":"2020-02-12","Total consultas":528},
    {"Fecha":"2020-02-13","Total consultas":455},{"Fecha":"2020-02-14","Total consultas":428},
    {"Fecha":"2020-02-15","Total consultas":475},{"Fecha":"2020-02-16","Total consultas":414},
    {"Fecha":"2020-02-17","Total consultas":539},{"Fecha":"2020-02-18","Total consultas":395},
    {"Fecha":"2020-02-19","Total consultas":446},{"Fecha":"2020-02-20","Total consultas":449},
    {"Fecha":"2020-02-21","Total consultas":526},{"Fecha":"2020-02-22","Total consultas":484},
    {"Fecha":"2020-02-23","Total consultas":475},{"Fecha":"2020-02-24","Total consultas":384},
    {"Fecha":"2020-02-25","Total consultas":468},{"Fecha":"2020-02-26","Total consultas":443},
    {"Fecha":"2020-02-27","Total consultas":480},{"Fecha":"2020-02-28","Total consultas":431},
    {"Fecha":"2020-02-29","Total consultas":511},{"Fecha":"2021-02-01","Total consultas":534},
    {"Fecha":"2021-02-02","Total consultas":532},{"Fecha":"2021-02-03","Total consultas":464},
    {"Fecha":"2021-02-04","Total consultas":505},{"Fecha":"2021-02-05","Total consultas":408},
    {"Fecha":"2021-02-06","Total consultas":409},{"Fecha":"2021-02-07","Total consultas":407},
    {"Fecha":"2021-02-08","Total consultas":425},{"Fecha":"2021-02-09","Total consultas":381},
    {"Fecha":"2021-02-10","Total consultas":510},{"Fecha":"2021-02-11","Total consultas":444},
    {"Fecha":"2021-02-12","Total consultas":444},{"Fecha":"2021-02-13","Total consultas":533},
    {"Fecha":"2021-02-14","Total consultas":438},{"Fecha":"2021-02-15","Total consultas":469},
    {"Fecha":"2021-02-16","Total consultas":424},{"Fecha":"2021-02-17","Total consultas":432},
    {"Fecha":"2021-02-18","Total consultas":412},{"Fecha":"2021-02-19","Total consultas":507},
    {"Fecha":"2021-02-20","Total consultas":451},{"Fecha":"2021-02-21","Total consultas":378},
    {"Fecha":"2021-02-22","Total consultas":402},{"Fecha":"2021-02-23","Total consultas":477},
    {"Fecha":"2021-02-24","Total consultas":400},{"Fecha":"2021-02-25","Total consultas":494},
    {"Fecha":"2021-02-26","Total consultas":539},{"Fecha":"2021-02-27","Total consultas":425},
    {"Fecha":"2021-02-28","Total consultas":527},{"Fecha":"2022-02-01","Total consultas":533},
    {"Fecha":"2022-02-02","Total consultas":416},{"Fecha":"2022-02-03","Total consultas":533},
    {"Fecha":"2022-02-04","Total consultas":381},{"Fecha":"2022-02-05","Total consultas":388},
    {"Fecha":"2022-02-06","Total consultas":490},{"Fecha":"2022-02-07","Total consultas":522},
    {"Fecha":"2022-02-08","Total consultas":437},{"Fecha":"2022-02-09","Total consultas":416},
    {"Fecha":"2022-02-10","Total consultas":429},{"Fecha":"2022-02-11","Total consultas":406},
    {"Fecha":"2022-02-12","Total consultas":536},{"Fecha":"2022-02-13","Total consultas":404},
    {"Fecha":"2022-02-14","Total consultas":455},{"Fecha":"2022-02-15","Total consultas":471},
    {"Fecha":"2022-02-16","Total consultas":404},{"Fecha":"2022-02-17","Total consultas":538},
    {"Fecha":"2022-02-18","Total consultas":537},{"Fecha":"2022-02-19","Total consultas":479},
    {"Fecha":"2022-02-20","Total consultas":484},{"Fecha":"2022-02-21","Total consultas":383},
    {"Fecha":"2022-02-22","Total consultas":430},{"Fecha":"2022-02-23","Total consultas":456},
    {"Fecha":"2022-02-24","Total consultas":423},{"Fecha":"2022-02-25","Total consultas":376},
    {"Fecha":"2022-02-26","Total consultas":525},{"Fecha":"2022-02-27","Total consultas":528},
    {"Fecha":"2022-02-28","Total consultas":401},{"Fecha":"2023-02-01","Total consultas":453},
    {"Fecha":"2023-02-02","Total consultas":408},{"Fecha":"2023-02-03","Total consultas":442},
    {"Fecha":"2023-02-04","Total consultas":498},{"Fecha":"2023-02-05","Total consultas":515},
    {"Fecha":"2023-02-06","Total consultas":494},{"Fecha":"2023-02-07","Total consultas":465},
    {"Fecha":"2023-02-08","Total consultas":382},{"Fecha":"2023-02-09","Total consultas":384},
    {"Fecha":"2023-02-10","Total consultas":396},{"Fecha":"2023-02-11","Total consultas":530},
    {"Fecha":"2023-02-12","Total consultas":439},{"Fecha":"2023-02-13","Total consultas":518},
    {"Fecha":"2023-02-14","Total consultas":454},{"Fecha":"2023-02-15","Total consultas":504},
    {"Fecha":"2023-02-16","Total consultas":376},{"Fecha":"2023-02-17","Total consultas":413},
    {"Fecha":"2023-02-18","Total consultas":447},{"Fecha":"2023-02-19","Total consultas":455},
    {"Fecha":"2023-02-20","Total consultas":515},{"Fecha":"2023-02-21","Total consultas":385},
    {"Fecha":"2023-02-22","Total consultas":402},{"Fecha":"2023-02-23","Total consultas":533},
    {"Fecha":"2023-02-24","Total consultas":468},{"Fecha":"2023-02-25","Total consultas":450},
    {"Fecha":"2023-02-26","Total consultas":413},{"Fecha":"2023-02-27","Total consultas":419},
    {"Fecha":"2023-02-28","Total consultas":508}]

jsonconsultas2=[]

def search_user(id:int):
    algosfiltrados = filter(lambda user: user.id==id,users)
    try:
        return list(algosfiltrados)[0]
    except:
        return {"error":"sin elementos"}

app = FastAPI();

@app.get("/getconsultas/")
async def getconsultas():
        aniosarray=[                    
             {"Anio":2018,"Total":0},
             {"Anio":2019,"Total":0},
             {"Anio":2020,"Total":0},
             {"Anio":2021,"Total":0},
             {"Anio":2022,"Total":0},
             {"Anio":2023,"Total":0},
             {"Anio":2024,"Total":0},
        ]

        client = MongoClient()
        db = client['local']

        collection = db['clinicaconsultas']
        for document in collection.find():
            # iterate the cursor
            jsonconsultas2.append(document)

        #print(jsonconsultas2) 
        client.close()

        for x in jsonconsultas2:
            #print(f"CASO {x['Fecha']}")
           
            for anio in aniosarray:
                
                valor= x['Fecha']
                #print(f"Comparando {valor.split('-')[0]} con {anio['Anio']}")
                if int(valor.split('-')[0])==anio['Anio']:
                    #print("SI")
                 
                    anio['Total']=anio['Total']+x['Total consultas'] 
                    break

        try:
            dataframe1 = pd.read_excel('consultas_febrero_2024.xlsx')

            #print(dataframe1)  
            #Formato Columnas/Filas
            i = 1
            j=0
            contador=0
            while i <= 29:
                
                j=0
                while j <= 4:
                    #print(f"Viendo columna {i} y fila {j}" )
                    #print(f"CASO {dataframe1[i][j]}" )
                    contador=contador+dataframe1[i][j]
                    j+=1
                i += 1               
            aniosarray[6]['Total']=int(contador)

            return list(aniosarray)
        except Exception as e: 
            print(e)
            return {"error":"sin elementos"}


@app.get("/prueba/{id}")
async def prueba(id:int):
    return search_user(id)
    
@app.get("/prueba1/")
async def prueba(id:int):

    return search_user(id)

@app.get("/adduser/")
async def adduser(user:User):

        if type(search_user(user.id))==User:
            return {"error": "Usuario ya existe"}
        else:
            users.append(user)

    

    