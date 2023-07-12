from bs4 import BeautifulSoup
import requests
import json

def setup():
    
    """Get all Data of universities here and return the data as an html file"""
    
    webUniNames=requests.get("https://businesstech.co.za/news/trending/101412/here-are-south-africas-26-universities/").text
    soup=BeautifulSoup(webUniNames,'lxml')
    content=soup.find_all('tr')
    return content

def Data(content):
    """This writes data into a text file which will be later used to access data recieved"""
    
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
    """This function just saves names of varsities nothing much! and filters everything else"""
    
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
    value={"Varsities":listToDict}
    return value

def AllData(filename):
    """All Data which will be needed by the application """
    gk=[]
    final_list=[]
    sm=[]
    with open(filename,'r') as fn: 
        gk= fn.readlines()
        for i in range(len(gk)):
            sm.append(gk[i])
            if len(sm)==2:
                kl={"Name":sm[0]}
                kl2={"Location":sm[1]}
                yu={"University":[kl,kl2]}
                final_list.append(yu)
                sm=[]
            
    return final_list



if "__main__"==__name__:
    value=createJsonFile(AllData("VarsityNames"))
    with open("Varsities.json", "w") as outfile:
        outfile.write(json.dumps(value))
    
    