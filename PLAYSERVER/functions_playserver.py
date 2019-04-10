import requests,json,base64,sys,time, hashlib, binascii
sys.path.insert(0, "PLAYSERVER/")
from data_playserver import*
sys.path.insert(0, "ANTICAPTCHA/")
from functions_anticaptcha import *
from colorama import init, Fore, Back, Style
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
session = requests.Session()
retry = Retry(connect=50, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

init(convert=True)
def GETIMAGE(proxies):
    try:
        time.sleep(0.5)
        requestid = session.post(url_getpic,verify=False, timeout=200, headers=headerXtap,proxies=proxies).json()
        IMAGE_ID = requestid['checksum']
        time.sleep(0.5)
        IMAGECT = session.get(url_image + IMAGE_ID,verify=False, timeout=200,  headers=headerXtap,proxies=proxies)
        base64pic = base64.b64encode(IMAGECT.content).decode('utf-8')
        if base64pic.find('iVBORw0KGgoAAAANSUhE') > -1:
            IMAGE = {'id':IMAGE_ID,
            'base64':base64pic}
            return IMAGE
        else:
            return 0
    except :
        return 0


def POSTIMAGE(self,data_vote, proxies,taskid,proxy):
    for timeout in range(60):
        try:
            status_post = ('\n PROXY    : {0} \n IMAGE ID : {1}\n CAPTCHA  : {2} \n STATUS   : {3}   DELAY : {4}   REPORT : {5}')
            time.sleep(0.5)
            vote = session.post(url_submitpic,verify=False, timeout=200,headers=headerXtap,data=data_vote,proxies=proxies).json()
            if vote['success'] == True:
                self.true +=1
                status_end = status_post.format(proxy,data_vote['checksum'],data_vote['captcha'],vote['success'],vote['wait'],'0')
                print(Fore.GREEN+status_end, flush=True)
                print(Style.RESET_ALL, flush=True)
                return vote['wait']
            else:
                erro_message = vote['error_msg'].encode('utf8').hex()
                md5_error = hashlib.md5(binascii.unhexlify(erro_message)).hexdigest()
                if md5_error == 'b4ecb33fc4dd1515eae17c9afcf8b90d': #The image has expired or has been used.
                    self.fail += 1
                    status_end = status_post.format(proxy,data_vote['checksum'],data_vote['captcha'],vote['success'],vote['wait'],md5_error)
                    print(Fore.YELLOW+status_end, flush=True)
                    print(Style.RESET_ALL, flush=True)
                    self.proxywork -= 1
                    return -1
                if md5_error == '47b84f936cfa1a104fa5d44821639363': #The code in the image is incorrect.
                    self.fail += 1
                    status_end = status_post.format(proxy,data_vote['checksum'],data_vote['captcha'],vote['success'],vote['wait'],md5_error)
                    print(Fore.RED+status_end, flush=True)
                    print(Style.RESET_ALL, flush=True)
                    reportIncorrectImageCaptcha(self.key,taskid)
                    return vote['wait']
                else:
                    self.fail += 1
                    proxy_use = (' '+proxy+' has already been used to vote > vote next time '+ str(vote['wait']))
                    print(Fore.YELLOW+proxy_use, flush=True)
                    print(Style.RESET_ALL, flush=True)
                    return vote['wait']
        except:
            time.sleep(1)
    return 0
