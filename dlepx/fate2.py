import asyncio
from proxybroker import Broker
import threading,requests,time,json
from lxml import html
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

session = requests.Session()
retry = Retry(connect=5, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

def checkpxer(proxy,urlx):
    proxiex = {'http': ('http://'+proxy),'https': ('https://'+proxy), 'ftp': ('ftp://'+proxy)}
    try:
        reb = session.get(urlx,timeout=5,proxies =proxiex)
        checkdiff = html.fromstring(reb.content)
        bancheck = checkdiff.xpath('//*[@id="ban-alert-box"]/span/text()')
        if bancheck == ['IPของคุณถูกแบน']:
            with open('proxydict/p_blist.txt','r') as fp:
                vp = fp.read().splitlines()
                if proxy not in vp:
                    with open('proxydict/p_blist.txt','a') as wf:
                        wf.write(proxy+"\n")
                        print(proxy+" This proxy has ban ")
        else:
            with open('proxydict/p_wlist.txt','r') as fp:
                vp = fp.read().splitlines()
                if proxy not in vp:
                    with open('proxydict/p_wlist.txt','a') as wf:
                        wf.write(proxy+"\n")
                        print(proxy +" This proxy  connected")
    except:
        print(proxy+" This proxy fail to connect server")



async def show(proxies):
    while True:
        proxy = await proxies.get()
        if proxy is None: break
        pl = (str(proxy.host)+":"+str(proxy.port))
        urlx = ("http://playserver.in.th/index.php/Vote/prokud/PserverN-15282")
        with open('proxydict/p_list.txt','r') as fp:
            vp = fp.read().splitlines()
            if proxy not in vp:
                with open('proxydict/p_list.txt','a') as wf:
                    wf.write(pl+"\n")
                    threading.Thread(target = checkpxer, args = (pl,urlx)).start()



def fate2():
    proxies = asyncio.Queue()
    broker = Broker(proxies)
    tasks = asyncio.gather(
        broker.find(countries =['TH'],types=['HTTP', 'HTTPS'], limit=1000),
        show(proxies))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(tasks)