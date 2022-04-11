from urllib.request import urlopen as conn
import json
def bot(text):
    msg=text.replace(" ", "%20")
    url = "http://api.brainshop.ai/get?bid=164728&key=MKPsfkgXLZPGrWoH&uid=teamcloseup&msg="+msg
    response = conn(url)
    data= json.loads(response.read())
    output = data['cnt']
    
    return(output)
    