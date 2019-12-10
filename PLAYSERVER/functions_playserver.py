import requests,json,base64,sys,time, hashlib, binascii
sys.path.insert(0, "ANTICAPTCHA/")
from functions_anticaptcha import *


def GETIMAGE(self,proxies):
    try:
        rid = self.session.post(self.psv["getimage"], timeout=int(self.opx["t_request"]), headers=self.psv["header"],proxies=proxies).json()
        IMAGE_ID = rid['checksum']

        IMAGECT = self.session.get(self.psv["u_image"] + IMAGE_ID, timeout=int(self.opx["t_request"]),  headers=self.psv["header"],proxies=proxies)
        base64pic = base64.b64encode(IMAGECT.content).decode('utf-8')
        if base64pic.find('/9j/4AAQSkZJRgABAQEAYABgAAD') > -1:
            IMAGE = {'id':IMAGE_ID,
            'base64':base64pic}
            return IMAGE
        else:
            return False
    except :
        return False


def POSTIMAGE(self,data_vote, proxies,taskid,proxy):
    for timeout in range(60):
        try:
            vote = self.session.post(self.psv["submit"],timeout=int(self.opx["t_request"]),headers=self.psv["header"],data=data_vote,proxies=proxies).json()
            self.w.refresh()
            if vote['success']:
                self.tss +=1
                self.w.addstr(f"{proxy} : SUCCESS  !! IMAGE ID : {data_vote['checksum']} -> {data_vote['captcha']}\n",self.greencolor)
                self.w.refresh()
                return vote['wait']
            else:
                erro_message = vote['error_msg'].encode('utf8').hex()
                md5_error = hashlib.md5(binascii.unhexlify(erro_message)).hexdigest()
                if md5_error == 'b4ecb33fc4dd1515eae17c9afcf8b90d': #The image has expired or has been used.
                    self.fss += 1
                    if self.opx["s_psnfail"] == 1:
                        self.w.addstr(f"{proxy} : FAIL image has been used.  !! IMAGE ID : {data_vote['checksum']} -> {data_vote['captcha']}\n",self.redcolor)
                        self.w.refresh()
                    return None
                elif md5_error == '47b84f936cfa1a104fa5d44821639363': #The code in the image is incorrect.
                    self.fss += 1
                    if self.opx["s_psnfail"] == 1:
                        self.w.addstr(f"{proxy} : FAIL The code in the image is incorrect.  !! IMAGE ID : {data_vote['checksum']} -> {data_vote['captcha']}\n",self.redcolor)
                        self.w.refresh()
                    reportIncorrectImageCaptcha(self.opx["key"],taskid)
                    return vote['wait']
                else:
                    self.fss += 1
                    if self.opx["s_psnw"] == 1:
                        self.w.addstr(f"{proxy} : FAIL Proxy Wait  !! IMAGE ID : {data_vote['checksum']} -> {data_vote['captcha']} Next Vote Time {vote['wait']}\n",self.yellowcolor)
                        self.w.refresh()
                    return vote['wait']
        except:
            time.sleep(1)
    return False
