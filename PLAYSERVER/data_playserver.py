# -*- coding: utf-8 -*-
import os ,configparser,requests,re,sys
from msvcrt import getch
import urllib.parse

loadconfig = configparser.RawConfigParser()
loadconfig.readfp(open(r"control/config.txt"))
server = loadconfig.get("default", "server")
url_server = ("https://playserver.in.th/index.php/Server/")
url_vote = ("https://playserver.in.th/index.php/Vote/prokud/")
url_image = ("http://playserver.co/index.php/VoteGetImage/")
header_backvote = ("http://playserver.in.th/index.php/Vote/prokud/")
try:
    rquest_unpack = requests.get(url_server+server)
    unpack_text = re.search(url_vote+'(.+?)"',rquest_unpack.text)
    unpack_unicode = (unpack_text.group(1))
    unpack_Entities = urllib.parse.quote(unpack_unicode)
except:
    print('\n Please Check you config.txt/[server_id]  !! ')
    junk = getch()
    sys.exit()
url_getpic = ("http://playserver.co/index.php/Vote/ajax_getpic/"+unpack_Entities)
url_submitpic = ("http://playserver.co/index.php/Vote/ajax_submitpic/"+unpack_Entities)
headerXtap = {

"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
"Connection": "keep-alive",
"Accept-Encoding": "gzip, deflate",
"Referer": (header_backvote+unpack_Entities)
}
