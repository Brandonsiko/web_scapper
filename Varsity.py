from bs4 import BeautifulSoup
import requests
import json

def setup():
    webUniNames=requests.get("https://businesstech.co.za/news/trending/101412/here-are-south-africas-26-universities/").text
    soup=BeautifulSoup(webUniNames,'lxml')
    content=soup.find_all('tr')
    return content

def Data(content):
    filename="VarsityNames"
    with open(filename,'w') as uniNames:
        for item in content:
            uniNames.writelines(item.text)
        print(item)
        uniNames.close()
    return uniNames
    
def Initialize(filename):
    try:
        with open(filename,'r') as names:
            vales=names.readlines()
        return len(vales)
    except FileNotFoundError as e:
        print(e)
        return 0

def justNames(filename):
    myinfoFile=[]
    south_african_varsities=[]
    with open(filename,'r') as myfile:
        for item in myfile.readlines():
            if item=="\n":
                pass
            else:
                myinfoFile.append(item)
        myfile.close()
    for i in range(len(myinfoFile)):
        if i%2==0:
            south_african_varsities.append(myinfoFile[i])
        else:
            pass
    return south_african_varsities

def varistyData(list_of_names):
    with open("varsityData",'w') as data_info:
        for item in list_of_names:
            data_info.writelines(item)
        data_info.close()


def createJsonFile(myList):
    """make a dictionary of names of varsities"""
    listToDict={}
    value={}
    for i in range(len(myList)):
        listToDict[i]=myList[i]
    value[0]={"namesOfVarsities":listToDict}
    return value

mything=justNames("VarsityNames")
value=(createJsonFile(mything))
well=json.dumps(value)
with open("Vnames.json", "w") as outfile:
    outfile.write(well)