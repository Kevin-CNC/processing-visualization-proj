import requests, json
from requests import Response

urls:list = [
    "https://yc-oss.github.io/api/batches/spring-2025.json",
    "https://yc-oss.github.io/api/batches/summer-2025.json",
    "https://yc-oss.github.io/api/batches/fall-2025.json",
    "https://yc-oss.github.io/api/batches/winter-2025.json"
]


def fetch_company_batch(targetUrl:str) -> list:
    """
    Fetch data straight from the publicly available Y-Combinator API.
    
    Inputs:
    targetUrl 'str' : The target endpoint of the api
    
    
    Returns:
    
    """
    
    reply:Response = requests.get(url=targetUrl)
    data = reply.json()
    
    comps = list()
    for point in data:
        frame:dict = {
            "uniqueId" : point['id'],
            "logo" : point['small_logo_thumb_url'],
            "description": point['one_liner'],
            "industry": point["industry"],
            "batch": point['batch']        
        }
        
        dataString:str = json.dumps(frame) # Serialises the dictionary into a string.
        comps.append(dataString+"\n")


    with open('data.txt',"w") as recordingFile:
        recordingFile.writelines(comps)
            
                
for url in urls:
    fetch_company_batch(targetUrl=url)