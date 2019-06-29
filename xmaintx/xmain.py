import curses,os,curses.panel,threading,sys,time,ctypes
import curses.textpad as textpad
import configparser,urllib.parse,requests,re, webbrowser
from msvcrt import getch
sys.path.insert(0, "ANTICAPTCHA/")
from data_anticaptcha import*
from functions_anticaptcha import *
sys.path.insert(0, "PLAYSERVER/")
from functions_playserver import *
sys.path.insert(0, "dlepx/")
from DLetajx import*
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry



class ThreadWithReturnValue(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        threading.Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None
    def run(self):
        print(type(self._target))
        if self._target is not None:
            self._return = self._target(*self._args,
                                                **self._kwargs)
    def join(self, *args):
        threading.Thread.join(self, *args)
        return self._return



def updates_col(self):
    if self.tss != 0 or self.fss != 0:
            fianl = self.tss+self.fss
            self.pss = self.tss/fianl*100
    j = (' {0} :  server: {1} - proxy: [ {2} ]  ,true ({3}) ,false ({4}) ,success({5}%), - PserverNX').format(self.opx["userid"],self.opx["server"],self.pw,self.tss,self.fss,"%.2f"%self.pss)
    ctypes.windll.kernel32.SetConsoleTitleW(j)

def psnx_f(self,proxies,proxy):
    self.pw += 1
    ft = False
    sd = 0
    dl = 0
    fv = 0
    ftx = 0
    while (int(self.tss)< int(self.opx["maxvote"]) and self.rpx == True ):
        updates_col(self)
        threadsx = []
        threadcap = []
        IMAG = []
        for i in range(int(self.opx["maximage"])):
            tg = ThreadWithReturnValue(target = GETIMAGE, args = (self,proxies))
            threadsx.append(tg)
        for x in threadsx:
            x.start()
            time.sleep(0.5)
        for x in threadsx:
            c = x.join()
            IMAG.append(c)
        for p in IMAG:
            if p != 0:
                cp = ThreadWithReturnValue(target = GETCAPCHA, args = (self,p))
                threadcap.append(cp)
            else:
                fv += 1
                if fv >= int(self.opx["f_request"]):
                    self.pw -= 1
                    sys.exit()

        for x in threadcap:
            x.start()
            time.sleep(0.5)
        for x in threadcap:
            h = x.join()
            if h != 0:
                if h['status'] != False:
                    if ft == True:
                        msp = time.time()
                        gs =  msp - sd
                        pd = dl - gs
                        if pd >= 0:
                                time.sleep(pd)
                    dl = 0
                    dtv = {'server_id':self.opx["server"],'captcha': h['text'], 'gameid': self.opx["userid"], 'checksum': h['id']}
                    vt = POSTIMAGE(self,dtv,proxies,h['taskId'],proxy)
                    updates_col(self)
                    if vt != False:
                        if vt == -1:
                            self.pw -= 1
                            sys.exit()
                        else:
                            if ft == False :
                                ft = True
                            if vt > 100:
                                ftx += 1
                                if ftx >= int(self.opx["f_request"]):
                                    self.pw -= 1
                                    sys.exit()
                                vt = vt-100
                            sd = time.time()
                            dl = int(vt)
                            
                else:
                    self.w.addstr("error"+str(h['errorDescription'])+"\n",self.redcolor)
                    self.w.refresh()
            else:
                self.w.addstr("take a long time from https://anti-captcha.com \n",self.redcolor)
                self.w.refresh()


    if self.rpx == False:
        self.w.addstr(proxy+" this proxy  exit | Psnx turn off   . . . \n",self.redcolor)
        self.w.refresh()
    else:
        self.w.addstr(proxy+" this proxy  exit | maxvote turn off   . . . \n",self.greencolor)
        self.w.refresh()

def updateseesion(self):
    self.session = requests.Session()
    self.retry = Retry(connect=self.opx["m_request"], backoff_factor=0.5)
    self.adapter = HTTPAdapter(max_retries=self.retry)
    self.session.mount('http://', self.adapter)
    self.session.mount('https://', self.adapter)



def autovote(self):
    if self.rpx == True:
        #setsen
        foo = []
        updateseesion(self)
        self.tss = 0
        self.fss = 0
        self.w.clear()
        self.w.addstr("PSNX Autovote turn on  . . . \n",self.greencolor)
        self.w.refresh()
        hh = threading.Thread(target = psnx_f, args = (self,0,0))
        foo.append(hh)
        with open('proxydict/p_wlist.txt','r') as fp:
            px = fp.read().splitlines()
            for proxy in px:
                try:
                    if '@'  in proxy:
                        spinpx = proxy.split("@")
                        xproxy, port = spinpx[2].split(':')
                    else:
                        xproxy, port = proxy.split(':')
                    if xproxy not in self.dicx_proxy:
                        self.dicx_proxy[xproxy] = port
                        proxies = {'http': ('http://'+proxy),'https': ('https://'+proxy), 'ftp': ('ftp://'+proxy)}
                        j = threading.Thread(target = psnx_f, args = (self,proxies,proxy))
                        foo.append(j)
                    elif port not in self.dicx_proxy[xproxy]:
                        proxies = {'http': ('http://'+proxy),'https': ('https://'+proxy), 'ftp': ('ftp://'+proxy)}
                        j = threading.Thread(target = psnx_f, args = (self,proxies,proxy))
                        foo.append(j)
                except:
                    self.w.addstr("fail to get proxy in p_wlist.txt \n",self.redcolor)
                    self.w.refresh()

        for x in foo:
            x.start()
            time.sleep(0.5)
        for x in foo:
            x.join()
        self.w.addstr(("PserverNX success True ({0}) False ({1}) \n").format(self.tss,self.fss),self.cyancolor)
        self.w.refresh()



def updatesv(self):
    try:
        unpack1 = requests.get(self.psv["u_server"]+self.opx["server"])
        unpack2 = re.search(self.psv["u_vote"]+'(.+?)"',unpack1.text)
        unpack_unicode = (unpack2.group(1))
        unpack_fn = urllib.parse.quote(unpack_unicode)
        self.psv["getimage"] =  ("http://playserver.co/index.php/Vote/ajax_getpic/"+unpack_fn)
        self.psv["submit"] = ("http://playserver.co/index.php/Vote/ajax_submitpic/"+unpack_fn)
        self.psv["header"] = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
            "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
            "Connection": "keep-alive",
            "Accept-Encoding": "gzip, deflate",
            "Referer": (self.psv["cb_vote"]+unpack_fn)
        }
        for i in self.psv: 
            self.w.addstr(i+"  : "+ str(self.psv[i]) + "\n",self.greencolor)
        self.w.refresh()

    except:
        self.w.addstr("fail update server Please check server id \n",self.redcolor)
        self.w.refresh()




def commands_psnx(self,b):
    c = 0
    #unbug
    for i in b:
        c += 1
    cmx = str(b[0:(c-1)])
    #call commands
    try:
        co,ca = cmx.split(' ')
        if co == "fate0":
            if type(int(ca)) == int:
                if int(ca) > 14:
                    self.w.addstr("max value fate0 14 !!  \n",self.redcolor)
                    self.w.refresh()
                else:
                    threading.Thread(target = fate0, args = (self,int(ca))).start()
        elif co in self.opx:
            if co == "balance":
                self.w.addstr("You can't fix balance !!  \n",self.redcolor)
                self.w.refresh()
            else:
                self.opx[co] = ca
                self.w.addstr("Chang value "+co+" > "+self.opx[co]+"\n",self.cyancolor)
                self.w.refresh()
            cf = configparser.RawConfigParser()
            cf.read('control/config.ini')
            if co in cf["default"]:
                cf.set('default', co, ca)
                with open('control/config.ini', 'w') as configfile:
                    cf.write(configfile)
                if co == "server":
                    updatesv(self)
                elif co == "key":
                    check_ca(self)
            elif co in cf["option"]:
                cf.set('option', co, ca)
                with open('control/config.ini', 'w') as configfile:
                    cf.write(configfile)          
        elif co == "get":
            if ca in self.opx:
                self.w.addstr(ca+" : "+self.opx[ca]+"\n",self.greencolor)
                self.w.refresh()
            elif ca == "config":
                self.w.addstr("---------------------- All config -----------------------\n",self.greencolor)
                for i in self.opx: 
                    self.w.addstr(i+"  : "+ str(self.opx[i]) + "\n",self.greencolor)
                self.w.addstr("---------------------------------------------------------\n",self.greencolor)
                self.w.refresh()
            else:
                self.w.addstr('"'+cmx+'"'+" command not found\n",self.redcolor)
                self.w.refresh()
        else:
            self.w.addstr('"'+cmx+'"'+" command not found\n",self.redcolor)
            self.w.refresh()
    except:
        if cmx == "ca":
            threading.Thread(target = check_ca, args = (self,)).start()
        elif cmx == "fate2":
            webbrowser.open("FateX.exe")
        elif cmx == "dle":
            if self.ppx == False:
                self.ppx =True
                updateseesion(self)
                threading.Thread(target = dlepx_nx, args = (self,)).start()
            else:
                self.w.addstr("dlepx is runing can stop Please wait \n",self.redcolor)
                self.w.refresh()
        elif cmx == "psn":
            if self.rpx == False:
                self.rpx =True
                threading.Thread(target = autovote, args = (self,)).start()
            else:
                self.rpx = False
                self.w.addstr("PSNX is  turn off wait for loop exit !!! \n",self.redcolor)
                self.w.refresh()
        else:
            self.w.addstr('"'+cmx+'"'+" command not found\n",self.redcolor)
            self.w.refresh()



def check_ca(self):
    self.w.addstr(": Check key from anti-captcha.com . . .\n",self.yellowcolor)
    self.w.refresh()
    self.opx["balance"]  = str(GETbalance(self.opx["key"]))
    self.w.refresh()
    if self.opx["balance"] != "-10":
        self.w.addstr("Key     : "+ str(self.opx["key"]) +"\n",self.greencolor)
        self.w.addstr("Balance : "+ str(self.opx["balance"]) +"\n",self.greencolor)        
    else:
        self.w.addstr("Key     : "+ self.opx["key"] +"\n",self.redcolor)
        self.w.addstr("Balance :  error 0x0" +"\n",self.redcolor) 
        self.w.addstr("Please check your key . . .\n",self.redcolor)
    self.w.refresh()

def callpsnx():
    curses.wrapper(PserverNX) 


class PserverNX(object):                                                         
    def __init__(self, stdscreen):
        #value
        self.rpx = False
        self.ppx = False
        self.spx = 0
        self.tss = 0
        self.fss = 0
        self.pss = 0
        self.pw  = 0
        self.dlestatus = {
            "t" : 0,
            "f" : 0,
            "b" : 0
        }
        self.dicx_proxy = {'proxylist':'newproxy'}
        curses.curs_set(0) 
        ts = os.get_terminal_size()
        self.xline = (int(ts.lines)-1)
        self.w= curses.newwin(self.xline, int(ts.columns),0, 0)
        self.w.scrollok(1)
        self.w.nodelay(0)
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK) # error command
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK) # succes command
        curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK) # succes command
        curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK) # succes command
        self.redcolor = curses.color_pair(1)
        self.greencolor = curses.color_pair(2)
        self.yellowcolor = curses.color_pair(3)
        self.cyancolor = curses.color_pair(4)
        #hderheader
        self.w.addstr("PserverNX(5.0) is an custom client and intelligent automated assistant for Playservern.in.th \nSupport - https://discord.gg/Mgu73TN \n")
        self.w.addstr("Update  - @syntaxp \n")
        self.w.addstr(": Check key from anti-captcha.com . . .\n",self.yellowcolor)
        self.w.refresh()
        #load config
        cf = configparser.RawConfigParser()
        cf.readfp(open(r"control/config.ini"))
        self.opx = {
            "server" : cf.get("default", "server"),
            "key" : cf.get("default", "key"),
            "userid" : cf.get("default", "userid"),
            "maxvote" : cf.get("option", "maxvote"),
            "maximage" : cf.get("option", "maximage"),
            "max_thread" : cf.get("option", "max_thread"),
            "t_request" : cf.get("option", "t_request"),
            "m_request" : cf.get("option", "m_request"),
            "f_request" : cf.get("option", "f_request"),
            "s_dlefail" : int(cf.get("option", "s_dlefail")),
            "s_psnfail" : int(cf.get("option", "s_psnfail")),
            "s_psnw" : int(cf.get("option", "s_psnw")),
            "dl" : float(cf.get("option", "dl"))
        }
        self.opx["balance"]  = str(GETbalance(self.opx["key"]))
        #set url server
        self.psv = {
            "u_server" : "https://playserver.in.th/index.php/Server/",
            "u_vote" : "https://playserver.in.th/index.php/Vote/prokud/",
            "u_image" : "http://playserver.co/index.php/VoteGetImage/",
            "cb_vote" : "http://playserver.in.th/index.php/Vote/prokud/",
        }
       
        self.w.addstr("--------------------------- Config ---------------------------\n",self.greencolor)
        self.w.addstr("Server  : "+ self.opx["server"] +"\n",self.greencolor)
        self.w.addstr("Userid  : "+ self.opx["userid"] +"\n",self.greencolor)
        self.w.addstr("Maxvote : "+ self.opx["maxvote"] +"\n",self.greencolor)
        if str(self.opx["balance"]) != "-10":
            self.w.addstr("Key     : "+ self.opx["key"] +"\n",self.greencolor)
            self.w.addstr("Balance : "+ self.opx["balance"] +"\n",self.greencolor)
            self.w.addstr("--------------------------------------------------------------\n",self.greencolor)
        else:
            self.w.addstr("Key     : "+ self.opx["key"] +"\n",self.redcolor)
            self.w.addstr("Balance :  error 0x0" +"\n",self.redcolor) 
            self.w.addstr("--------------------------------------------------------------\n",self.greencolor)
            self.w.addstr("Please check your key . . .\n",self.redcolor)
        updatesv(self)
        #set session
        self.session = requests.Session()
        self.retry = Retry(connect=int(self.opx["m_request"]), backoff_factor=0.5)
        self.adapter = HTTPAdapter(max_retries=self.retry)
        self.session.mount('http://', self.adapter)
        self.session.mount('https://', self.adapter)
        #error 0x0 key 

        while True:
            win = curses.newwin(1, 0,self.xline, 0)
            win.scrollok(1)
            win.addstr(0, 0, "P$erverNX : ",self.redcolor)
            win.refresh()
            c = textpad.Textbox(curses.newwin(0,0,self.xline,12), insert_mode=True).edit()
            threading.Thread(target = commands_psnx, args = (self,c)).start()



