
<p align="center">
  <a href="https://github.com/syntaxp/PserverNA">
    <img src="https://user-images.githubusercontent.com/47280575/55755362-ff75db00-5a78-11e9-8a33-6ea3af4bdb0e.jpg" alt="PserverNA logo" width="72" height="72">
  </a>
</p>
<h3 align="center">PserverNA</h3>

<p align="center"> 
  PserverNA เป็นเพียงซอฟแวร์ที่ให้บริการเชื่อมต่อ API ของAntiCaptcha กับ เว็ป Playserver เราไม่มีการเรียกเก็บเงินใดๆ
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
- [Proxylist.txt](#proxy)
- [UPDATE!!](https://github.com/syntaxp/PserverNA/blob/master/update.md)

## Quick start
- [Download the latest release.](https://github.com/syntaxp/PserverNA/archive/master.zip)
- สมัครสมาชิก [anti-captcha.com](http://getcaptchasolution.com/e80kqlwlmw) 



## Basic work

```text
PserverN
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
autoproxy = 0 # ค้นหาพร๊อกซี่อัตโนมัติ (bata) 1 เปิด/  0 ปิด

```
***example: config.txt***
```java
[default]
key_anticap = d4555884848484c48a4cac88ac
server = 15282
userid  = pserverna

[option]
maxvote = 1000
autoproxy = 1

```
## Proxy
**[proxy.txt](https://github.com/syntaxp/PserverNA/blob/master/control/proxy.txt)**
```text
proxy.txt จะเป็นไฟล์ txt ที่ใช้สำหรับเก็บรายชื่อ proxy ต่างๆที่ใช้สำหรับโหวต
เนื้องจาก การโหวต Playserver ปกติ เมื่อโหวตสำเร็จ จะติดดีเลเป็นเวล 61 วิ
เราจึงจำเป็นต้องมี proxy ใช้สำหรับโหวตเพิ่มขึ้นเพื่อการทำงานโหวตที่ไวขึ้น
Playserver กำจัดสิทธ์โหวตให้เพียง IP ที่ให้บริการในไทย นั้นหมายความว่า เราเลือกเฉพาะ Proxy ไทยในการโหวต

- สามารถหา Proxy ได้จากไหน ?
proxy จะมี 2 แบบ 
แบบปกติคือแจกตามเว็ปทั่วไปสามารถ search ได้จาก google 'proxy list' , 'proxy list thai'
แบบที่ 2 จะเป็น proxy แบบเช่า ซึ่งจะยกประเด็นนี้ไปในหัวข้อ private proxy

หลังจากที่เราได้ proxy มาแล้วให้เราก๊อปแล้วนำไปวางใน proxylist.txt
```
***example: proxylist.txt***
```text
103.15.140.141:44759
103.15.140.142:44759
103.15.140.177:44759
103.15.226.124:80
103.15.241.161:8080
103.15.245.26:8080
103.15.51.160:8080
103.15.83.73:58486
103.15.83.82:8080
103.16.61.46:52424
103.17.38.24:8080
103.18.243.154:8080
103.18.32.242:46734
103.19.110.177:8080
```


