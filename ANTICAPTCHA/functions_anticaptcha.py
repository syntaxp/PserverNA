import requests,json,time,sys
sys.path.insert(0, "ANTICAPTCHA/")
from data_anticaptcha import *


def GETCAPCHA(self,base64):
    try:
        Taskdata = {
        "clientKey":self.opx["key"],
        "task":
        {
        "type":"ImageToTextTask",
        "body":base64["base64"],
        "phrase":False,
        "case":False,
        "numeric":False,
        "math":0,
        "minLength":6,
        "maxLength":6,
        "comment":"This application has been report to anticapcha If your answer is wrong according to anticapcha policy from https://anti-captcha.com/clients/reports/refunds"
        },
        "softId":appid,
        "languagePool":"en"
        }
        createTask  = requests.post(create_task_url,timeout=100,json=Taskdata).json()
        if createTask['errorId'] == 0:
            TaskID = {
                "clientKey":self.opx["key"],
                "taskId": createTask['taskId']
                    }
            for timeout in range(60):
                captcha_id = requests.post(get_result_url,timeout=100, json = TaskID).json()
                if captcha_id['status'] != 'processing':
                    captcha = {'status':True,'text':captcha_id['solution']['text'],'cost':captcha_id['cost'],'taskId':createTask['taskId'],'id':base64['id']}
                    return captcha
                else:
                    time.sleep(5)
        else:
            captcha = {'status':False,'errorDescription':createTask['errorDescription']}
            return captcha
    except:
        return False

def GETbalance(key):
    try:
        data = {'clientKey':key}
        p = requests.post(get_balance_url,timeout=5,headers=header,json=data).json()
        if p['errorId'] == 0:
            return p['balance']
        else:
            return None
    except:
        return None

def reportIncorrectImageCaptcha(key,taskid):
    data = {
    "clientKey":key,
    "taskId": taskid
    }
    reprot = requests.post(incorrect_captcha_url,timeout=500,headers=header,json=data).json()
    return reprot