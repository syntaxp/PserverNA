import configparser,sys
import threading,time,ctypes,re
from colorama import init, Fore, Back, Style
sys.path.insert(0, "PLAYSERVER/")
from data_playserver import *
from functions_playserver import *
sys.path.insert(0, "ANTICAPTCHA/")
from data_anticaptcha import*
from functions_anticaptcha import *
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
class PSERVERNA_PAYLOADS:

    def __init__(self):
        init(convert=True)
        cls()
        print('\n [-] Auto vote playserver runing checkproxy/vote . . . ')
        self.method_1()
    def method_1(self):
        def run(self):
            loadconfig = configparser.RawConfigParser()
            loadconfig.readfp(open(r"control/config.txt"))
            self.server = loadconfig.get("default", "server")
            self.key = loadconfig.get("default", "key")
            self.userid = loadconfig.get("default", "userid")
            self.maxvote = loadconfig.get("option", "maxvote")
            self.autoproxy = loadconfig.get("option", "autoproxy")
            self.true = 0
            self.fail = 0
            self.persen = 0
            self.proxywork = 0
            self.balance = 0
            self.dic_proxy = {'proxylist':'newproxy'}
            with open('control/proxy.txt','r') as loadproxy:
                proxylist = loadproxy.read().splitlines()
                for proxy in proxylist:
                    try:
                        if '@'  in proxy:
                            wgetproxy = proxy.split("@")[1]
                        else:
                            wgetproxy, port = proxy.split(':')
                        if wgetproxy not in self.dic_proxy:
                            self.dic_proxy.update({wgetproxy:wgetproxy})
                            proxies = {'http': ('http://'+proxy),'https': ('https://'+proxy), 'ftp': ('ftp://'+proxy)}
                            threading.Thread(target = PserverNA, args = (self,proxies,proxy)).start()
                    except:
                        time.sleep(1)
                        print('fail get proxy from proxy.txt')
            threading.Thread(target = getSBalance, args = (self,)).start()
            if int(self.autoproxy) == 1:
                threading.Thread(target = autogetproxy, args = (self,)).start()
            updatestatus(self)


        def autogetproxy(self):
            while True:
                proxylist = requests.get('https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list').text
                loadproxy = proxylist.splitlines()
                for nextporxy in loadproxy:
                    json_porxy = json.loads(nextporxy)
                    if json_porxy['country'] == "TH" and json_porxy['type'] == "http" :
                        proxy = (json_porxy['host']+':'+ str(json_porxy['port']))
                        wgetproxy = re.search('(.+?):',proxy).group(1)
                        if wgetproxy not in self.dic_proxy:
                            self.dic_proxy.update({wgetproxy:wgetproxy})
                            proxies = {'http': ('http://'+proxy),'https': ('https://'+proxy), 'ftp': ('ftp://'+proxy)}
                            threading.Thread(target = PserverNA, args = (self,proxies,proxy)).start()

                time.sleep(17)

        def getSBalance(self):
            while True:
                self.balance = GETbalance(self.key)
                time.sleep(10)
        def updatestatus(self):
            if self.true != 0 or self.fail != 0:
                fianl = self.true+self.fail
                self.persen = self.true/fianl*100
            j = (' {0} :  Serverid : {1} - Proxy: [ {2} ]  ,True_ ({3}) ,False_ ({4}) ,SUCCESS({5}%),  {6}$   - PserverNA').format(self.userid,self.server,self.proxywork,self.true,self.fail,"%.2f"%self.persen,self.balance)
            ctypes.windll.kernel32.SetConsoleTitleW(j)

        def PserverNA(self,proxies,proxy):
            self.proxywork += 1
            opentime = 0
            setdelay = 0
            delay = 0
            while (int(self.true) < int(self.maxvote)):
                IMAGE = GETIMAGE(proxies)
                if IMAGE != 0:
                    captcha = GETCAPCHA(self,IMAGE['base64'])
                    if captcha != 0:
                        if captcha['status'] != False:
                            if opentime == 1:
                                makesleep = time.time()
                                getsleep =  makesleep - setdelay
                                pooldelay = delay - getsleep
                                if pooldelay >= 0:
                                    time.sleep(pooldelay)
                                delay = 0
                            data_vote = {'server_id':self.server,'captcha': captcha['text'], 'gameid': self.userid, 'checksum': IMAGE['id']}
                            VOTE = POSTIMAGE(self,data_vote,proxies,captcha['taskId'],proxy)
                            if VOTE != 0:
                                if VOTE == -1:
                                    self.proxywork -= 1
                                    updatestatus(self)
                                    sys.exit()
                                else:
                                    if opentime == 0 :
                                        opentime = 1
                                    setdelay = time.time()
                                    delay = VOTE
                            updatestatus(self)
                        else:
                            print('error:'+captcha['errorDescription'],flush=True)
                    else:
                        print(' take a long time from https://anti-captcha.com',flush=True)
                else:
                    self.proxywork -= 1
                    updatestatus(self)
                    sys.exit()
            self.proxywork -=1
            updatestatus(self)
            print(' Maxvote : '+ self.maxvote +' this proxy (' + proxy + ')stop working but another proxy Will work until completion')
            sys.exit()

        run(self)



class GETPROXYAUTO:
    def __init__(self):
        cls()
        print('\n [-] Auto getproxy runing proxy working save to control/proxy.txt . . .')
        init(convert=True)
        self.method_1()
    def method_1(self):
        def run(self):
            print(' coming soon')
            time.sleep(5)
            sys.exit()



        run(self)
