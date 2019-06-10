import threading,requests,time
from lxml import html

class Dleter:
    def __init__(self):
        print('\n [-] PLAYSERVER PROXY DLETER by Syntaxp *  ')
        self.method_1()
    def method_1(self):
        def run(self):
            print(" 1 CHECK PROXY \n 2 UNBAN PROXY")
            CALLFSS = int(input(" $ CALL FUNCTION ? : "))
            if CALLFSS == 1:
                print(' > CHECK PROXY PLAYSERVER DLETER ')
                with open('sniffproxy/proxy.txt','r') as fproxy:
                    vccproxy = fproxy.read().splitlines()
                    for proxyX in vccproxy:
                        threading.Thread(target = checkpxer, args = (self,proxyX)).start()
            elif CALLFSS == 2:
                print("wait for dev update this funtion")
                time.sleep(5)
            else:
                print(" Don't have functions")
        def checkpxer(self,proxy):
            proxiex = {'http': ('http://'+proxy),'https': ('https://'+proxy), 'ftp': ('ftp://'+proxy)}
            urlx = "http://playserver.in.th/index.php/Vote/prokud/PserverN-15282"
            try:
                reb = requests.get(urlx,timeout=10,proxies =proxiex)
                checkdiff = html.fromstring(reb.content)
                bancheck = checkdiff.xpath('//*[@id="ban-alert-box"]/span/text()')
                if bancheck == ['IPของคุณถูกแบน']:
                    with open('bansave.txt','r') as fproxy:
                        vccproxy = fproxy.read().splitlines()
                        if proxy not in vccproxy:
                            with open('bansave.txt','a') as wf:
                                print(" bansave -- "+ proxy)
                                wf.write(proxy+"\n")
                else:
                    with open('dletsave.txt','r') as fproxy:
                        vccproxy = fproxy.read().splitlines()
                        if proxy not in vccproxy:
                            with open('dletsave.txt','a') as wf:
                                wf.write(proxy+"\n")
                                print(" dletsave -- "+ proxy)
            except:
                print(" "+ proxy +" can not use this proxy")

        run(self)
