import threading,requests,time,curses,json
from lxml import html
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


def checkpxer(self,proxy,urlx):
    proxiex = {'http': ('http://'+proxy),'https': ('https://'+proxy), 'ftp': ('ftp://'+proxy)}
    try:
        reb = self.session.get(urlx,timeout=int(self.opx["t_request"]),proxies =proxiex)
        checkdiff = html.fromstring(reb.content)
        bancheck = checkdiff.xpath('//*[@id="ban-alert-box"]/span/text()')
        
        if bancheck == ['IPของคุณถูกแบน']:
            with open('proxydict/p_blist.txt','r') as fp:
                vp = fp.read().splitlines()
                if proxy not in vp:
                    with open('proxydict/p_blist.txt','a') as wf:
                        self.dlestatus["b"] += 1
                        wf.write(proxy+"\n")
                        if self.opx["s_dlefail"] == 1:
                            self.w.addstr("[ "+proxy+" ] this proxy get banned  \n",self.redcolor)
                            self.w.refresh()
                        self.spx -= 1
        else:
            with open('proxydict/p_wlist.txt','r') as fp:
                vp = fp.read().splitlines()
                if proxy not in vp:
                    self.dlestatus["t"] += 1
                    with open('proxydict/p_wlist.txt','a') as wf:
                        wf.write(proxy+"\n")
                        self.w.addstr(proxy+" This proxy  connected \n",self.greencolor)
                        self.w.refresh()
                        self.spx -= 1
    except:
        self.dlestatus["f"] += 1
        if self.opx["s_dlefail"] == 1:
            self.w.addstr("[ "+proxy+" ] This proxy fail to Connect server\n",self.redcolor)
            self.w.refresh()
        self.spx -= 1


def dlepx_nx(self):
    self.dlestatus = {
            "t" : 0,
            "f" : 0,
            "b" : 0
        }
    self.spx = 0
    urlx = (self.psv["u_vote"]+str(self.opx["server"]))
    self.w.addstr("dlepx (0.2) - auto check proxy playserver.in.th \n",self.greencolor)
    self.w.addstr("check from server - "+urlx+"\n",self.greencolor)
    self.w.refresh()
    xa = 0
    threadsx = []
    try:
        with open('proxydict/p_list.txt','r') as fp:
            vp = fp.read().splitlines()
            for p in vp:
                xa += 1
                tx = threading.Thread(target = checkpxer, args = (self,p,urlx))
                threadsx.append(tx)
            self.w.addstr("You have ("+str(xa)+") proxy in p_list.txt\n")
            self.w.refresh()
            for x in threadsx:
                self.spx += 1
                x.start()
                while(self.spx >= int(self.opx["max_thread"])):
                    time.sleep(1)
            for x in threadsx:
                x.join()
            self.w.addstr(("Proxy checking success * WORK  [ {0} ]  |  BAN [ {1} ]  | FAIL [ {2} ]\n").format(str(self.dlestatus ["t"]),str(self.dlestatus ["b"]),str(self.dlestatus ["f"])),self.cyancolor)
            self.w.refresh()
            self.ppx = False

    except:
        self.w.addstr("Please check p_list.txt !! \n",self.redcolor)
        self.w.refresh()

def fate0(self,lud):
    ft = False
    tsp = ((16*60)-(int(lud)*60))
    urlx = (self.psv["u_vote"]+str(self.opx["server"]))
    while True:
        self.w.addstr(("fate0  - - - - runing \n"),self.cyancolor)
        self.w.refresh()
        pn = 0
        self.spx = 0
        threadsx = []
        try:
            px = requests.get('https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list').text
            cp = px.splitlines()
            for snif in cp:
                jpx = json.loads(snif)
                if jpx['country'] == "TH" and jpx['type'] == "http" or jpx['country'] == "TH" and jpx['type'] == "https":
                    proxy = (str(jpx['host'])+':'+ str(jpx['port']))
                    with open('proxydict/p_list.txt','r') as fp:
                        vp = fp.read().splitlines()
                        if proxy not in vp:
                            with open('proxydict/p_list.txt','a') as wf:
                                wf.write(proxy+"\n")
                                tx = threading.Thread(target = checkpxer, args = (self,proxy,urlx))
                                threadsx.append(tx)
                
            for x in threadsx:
                x.start()
                pn += 1
                self.spx += 1
                while(self.spx >= int(self.opx["max_thread"])):
                    time.sleep(1)
            for x in threadsx:
                x.join()
            self.w.addstr(("succes fate0 get proxy new ({0})  \n").format(str(pn)),self.cyancolor)
            self.w.refresh()
            if ft == False:
                time.sleep(tsp)
                ft = True
            elif ft == True:
                time.sleep((16*60))
        except:
            self.w.addstr("Check your internet connection !! \n",self.redcolor)
            self.w.refresh()


