
<p align="center">
  <a href="https://github.com/syntaxp/PserverNA">
    <img src="https://user-images.githubusercontent.com/47280575/59976572-9837e380-95f0-11e9-9ee6-d41de7c7846e.png" alt="PserverNA logo" width="77" height="75">
  </a>
</p>
<h3 align="center">PserverNX</h3>

<p align="center"> 
  PserverNX เป็นเพียงซอฟแวร์ที่ให้บริการเชื่อมต่อ API ของAntiCaptcha กับ เว็ป Playserver เราไม่มีการเรียกเก็บเงินใดๆ
  เพียงแต่ผู้ใช้จำเป็นต้องเช่า KEY ของเว็ป AntiCaptcha เพื่อใช้บริการ แกะรหัส รูปภาพ เราไม่มีส่วนเกี่ยวของ กับ AntiCaptcha ในทางใดทั้งสิ้น
  <br>

   <a href="https://discord.gg/Mgu73TN">
  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSakv86QJPY-E6rxMEo_WzAwYUzyndjdY_d-Zu2ZOr9UuMjClxy5A" alt="discord logo" width="45" height="45">
  <a href="https://discord.gg/Mgu73TN">Discord</a>


</p>


## คู่มือ การใช้งาน
- <a href="https://www.youtube.com/watch?v=KWmf4K1T_SU">วิธีติดตั่ง/ตัวอย่าง(VIDEO)</a>
- [Quick start](#quick-start)
- [การทำงานเบื้องต้นของโปรแกรม](#basic-work)
- [KEY](#key)
- [การตั่งค่า config.txt](#config)
- [proxydict](#proxy)
- [UPDATE!!](https://github.com/syntaxp/PserverNA/blob/master/update.md)

## Quick start
- [Download the latest release.](https://github.com/syntaxp/PserverNA/archive/master.zip)
- สมัครสมาชิก [anti-captcha.com](http://getcaptchasolution.com/e80kqlwlmw) 



## Basic work

```text
PserverNX
|
└──> ดึงข้อมูลจาก / Playserver.in.th
        ├── รหัสรูปภาพ, รูปภาพ 
        | 
        └── > ส่งต่อรูปภาพต่อไปยัง / anti-captcha.com
                   ├── แกะรหัสรูปภาพ
                   |
                   └──> ส่งกลับมาที่ PserverN ──> ส่งคำตอบไปยัง Playserver.in.th
                            
```


## Key
KEY จะถูกสร้างให้อัตโนมัติ หลังจากที่เราเป็นสมาชิกของ ของ [anti-captcha.com](http://getcaptchasolution.com/e80kqlwlmw) 

สามารถเช็ค key ของตัวเองได้ที่ [apisetup](https://anti-captcha.com/clients/settings/apisetup) (`* ต้อง login ก่อนถึงจะเข้าชมหน้าเว็ปได้`)

![key](https://user-images.githubusercontent.com/47280575/54017688-5d34b000-41b9-11e9-9840-cbbcb38cf9f8.png)


## Config
**การตั่งค่า  [config.txt](https://github.com/syntaxp/PserverNA/blob/master/control/config.txt)**

```python
[default]
key = # key ของ Anticaptcha
server = # sever id ตัวอย่าง url <playserver.in.th/index.php/Vote/prokud/PserverN-15282> id sever คือ 15282
userid = #user id ของเกม

[option]
maxvote = 500 # จำนวนโหวตที่ต้องการ ควรมากกว่ ip ที่มีใน list
maximage = 2 # จำนวนสต๊อกรูปต่อ 1 ไอพี ไม่ควรมากกว่า 5
max_thread = 50 # จำนวนเช็ค proxy ไม่ให้มากกว่านี้
t_request = 5 # เวลาที่ใช้ในการ เรียกข้อมูล
m_request = 5 # จำนวนการเชื่อมต่อ server ใหม่ถ้าไม่สามารถเชื่อมต่อได้ 
f_request = 3 # จำนวนที่ต้องการดีด proxy ออกหาก โหวตพลาดกี่ครั้ง
s_dlefail = 1 # เปิด ปิดการแจ้งเตือน เช็ค proxy ที่ใช้งานไม่ได้
s_psnfail = 1 # เปิด ปิดการแจ้งเตือนหากโหวตพลาด
s_psnw = 1 # เปิด ปิดการเตือนหาก proxy มีดีเลย์
dl = 0.2 # ใช้ในอานาคต


```
***example: config.ini***
```java
[default]
key_anticap = d4555884848484c48a4cac88ac
server = 15282
userid  = pserverna

[option]
maxvote = 1000
maximage = 2
max_thread = 50
t_request = 5
m_request = 5
f_request = 3
s_dlefail = 1
s_psnfail = 1
s_psnw = 1
dl = 0.2
```

## Proxy
**[proxydict](https://github.com/syntaxp/PserverNA/tree/master/proxydict)**


```text
p_list.txt = proxy ที่หามาได้
p_blist.txt = proxy ที่ถูกแบน
p_wlist.txt = proxy ที่สามารถใช้งานได้
```
```text
p_list.txt จะเป็นไฟล์ txt ที่ใช้สำหรับเก็บรายชื่อ proxy ต่างๆที่ใช้สำหรับโหวต
เนื้องจาก การโหวต Playserver ปกติ เมื่อโหวตสำเร็จ จะติดดีเลเป็นเวล 61 วิ
เราจึงจำเป็นต้องมี proxy ใช้สำหรับโหวตเพิ่มขึ้นเพื่อการทำงานโหวตที่ไวขึ้น
Playserver กำจัดสิทธ์โหวตให้เพียง IP ที่ให้บริการในไทย นั้นหมายความว่า เราเลือกเฉพาะ Proxy ไทยในการโหวต

- สามารถหา Proxy ได้จากไหน ?
proxy จะมี 2 แบบ 
แบบปกติคือแจกตามเว็ปทั่วไปสามารถ search ได้จาก google 'proxy list' , 'proxy list thai'
แบบที่ 2 จะเป็น proxy แบบเช่า ซึ่งจะยกประเด็นนี้ไปในหัวข้อ private proxy

หลังจากที่เราได้ proxy มาแล้วให้เราก๊อปแล้วนำไปวางใน p_list.txt
```

***example: p_list.txt***
```text
103.15.140.141:44759
103.15.140.142:44759
```



## Chat Commands

| Command         | Description | Example  |
| ------ | -------------------------- | --- |
| psn | เริ่มการทำงาน Autovote  | psn |
| dle | เช็ค proxy เช็คจาก (p_list.txt) | dle |
| ca  | เช็ค  key anti-captcha | ca |
| fate2| เรียกใช้งาน  [fatex](#fatex) | fate2 |
| fate0 <minutes_ago>| ดึง proxy จาก  https://github.com/fate0/proxylist | fate0 16 |
| get <config_name> | โชว์ config | get key |
| <config_name> <value> | เปลี่ยน value config | key 12345678901100 |
  
  
## fateX 

<img src="https://user-images.githubusercontent.com/47280575/59977053-b6084700-95f6-11e9-8953-3eb3a44b4d2f.png" alt="PserverNA logo" width="40" height="35">


**fateX** และ **fate0**
ทำหน้าเหมือนกันคือใช้งาน ดึง proxy มาแล้วทำการช็ค จากนั้น proxy จะถูกส่งไปยัง proxydict ตามสถานะที่เช็ค



