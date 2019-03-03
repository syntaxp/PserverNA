import requests,json,time,threading,sys
from data_anti import get_balance_url,header,create_task_url,get_result_url,Appid,incorrect_captcha_url


def GETbalance(key):
    data = {'clientKey':key}
    p = requests.post(get_balance_url,headers=header,json=data).json()
    return p['balance']

def GETCAPCHA(key,base64):
    Taskdata = {
    "clientKey":key,
    "task":
    {
    "type":"ImageToTextTask",
    "body":base64,
    "phrase":False,
    "case":False,
    "numeric":False,
    "math":0,
    "minLength":6,
    "maxLength":6
    },
    "softId":int(Appid),
    "languagePool":"en"
    }

    createTask  = requests.post(create_task_url,json=Taskdata).json()
    if createTask['errorId'] != 1:
        TaskID = {
            "clientKey":key,
            "taskId": createTask['taskId']
            }
        for timeout in range(60):
            captcha_id = requests.post(get_result_url, json = TaskID).json()
            if captcha_id['status'] != 'processing':
                captcha = {'status':True,'text':captcha_id['solution']['text'],'cost':captcha_id['cost'],'taskId':createTask['taskId']}
                return captcha
            else:
                e = threading.Event()
                e.wait(timeout=3)
    else:
        return captcha['status':False]

def reportIncorrectImageCaptcha(key,taskid):
    data = {
    "clientKey":key,
    "taskId": taskid
    }
    reprot = requests.post(incorrect_captcha_url,headers=header,json=data).json()
    return reprot