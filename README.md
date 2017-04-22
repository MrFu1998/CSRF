## CSRF攻击
### CSRF是什么
* CSRF（`Cross-site request forgery`），中文名称：跨站请求伪造，也被称为：`one click attack/session riding`，缩写为：CSRF/XSRF。

### CSRF可以做什么
* 可以这么理解`CSRF`攻击：就是攻击者盗用了你的身份，以你的名义发送恶意请求。
`CSRF`能够做的事情包括：以你名义发送邮件，发消息，盗取你的账号，甚至于购买商品，虚拟货币转账......造成的问题包括：个人隐私泄露以及财产安全。

### CSRF原理
如图：
![SCRF原理](http://processon.com/chart_image/58f9ebe8e4b0f645b01fd70b.png)

### 如何防止CSRF攻击
防止`CSRF`攻击的两步走
1. 把会对数据进行更改的请求都采用`POST`方式。
2. 在`cookie`和`form`表单中都添加同一个`csrf_token`。在服务器比较这两个值。如果相等就是合法的请求，如果不相等，就是非法的请求。

### 项目背景及原因
* 此项目背景是以`icbc`用户之间正常转账，然后`stealer`为窃取者，窃取`icbc`用户的`money`
* 此项目纯属个人练习`CSRF`攻击原理，与`icbc`无关，本项目仅用于学习，禁止商业用途，

