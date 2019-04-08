
  ### version 4.0.0  :speech_balloon:
```c
PserverNA
└── update แก้ไขระบบใหม่ให้ยืดหยุ่นได้ดียิ่งขึ้น
      └── version.json @ version 4.0.0
          ├────── control/config.txt
          |          └── @ ลบคำสั่งที่ไม่จำเป็นออก
          |
          ├────── main.py & PserverNA.exe 
          |               @ main.py เปลี่ยนเป็น PserverNA.py
          |
          |
          ├──────── delete ProxyChecker ลบระบบ ProxyChecker
          |
          └──────── @ Auto Porxy เพิ่มระบบ ค้นหา PROXY AUTO
```


  ### version 2.0.3.2  :speech_balloon:
```c
PserverNA
└── update 
      └── version.json @ version 2.0.3.2
          ├────── control/config.txt
          |          └── @ option /เพิ่ม หัวข้อ option
          |                     ├── maxvote   / จำนวนโหวตที่ต้องการ ควรมากกว่ ip ที่มีใน list
          |                     ├── failvote  / จำนวนครั้งที่ ip โหวตพลาด ระบบจะเตะ ip ออก
          |                     ├── requestfail  / จำนวครั้งที่ ip พยามเชื่อมต่อไม่สำเร็จ ระบบจะเตะ ip ออก
          |                     └── requesttimeout / ระยะเวลาในการทำงานเรียกข้อมูล ส่งข้อมูล ควรตั่งให้มากกว่า 3 ขึ้นไป
          |
          ├────── main.py & PserverNA.exe 
          |          └──  @ commands /เพิ่ม commands ในการ call function
          |                     ├── 0 = Call Proxy_checker.py
          |                     └── 1 = Call Playserver_/Playserver.py
          |
          |
          └──────── @ ProxyChecker / เพิ่มโฟเดอร์ ProxyChecker
                        ├── @ Proxy_checker.py / เพิ่ม Proxy Checker Mode เช็ค proxy ไหนสามารถใช้งานได้
                        └── @ list.txt         / ไฟล์สำหรับเก็บ proxy ที่ต้องการเช็ค                            
```
