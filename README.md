<img src="https://github.com/whoamisec75/parscan/blob/main/static/IMG_20211205_145433.jpg"/>
<p align="center"><b><i>Fast parameter scanner</b></i></p> 

`Parscan` is a fast parameter scanner designed to identify the parameters and the vulnerabilities commonly associated with them, note that the `Parscan` does not performs any type of vulnerability scan againt the parameters. Parscan fetches URLs from Wayback Machine then scans each URL and outputs the parameter and vulnerability associated with it.

## Installation

```
▶ git clone https://github.com/whoamisec75/parscan.git
▶ cd parscan
▶ sudo python3 setup.py install
▶ parscan -h
```
## Usage

Scanning a domain: 
```
▶ parscan https://microsoft.com
```

Setting sleep time:
```
▶ parscan https://microsoft.com --sleep-time 5 
```

Specifing output file:
```
▶ parscan https://microsoft.com --output out.txt
```

Output:
```           
   ___  ___ _ ____ ___ ____ ___ _ ___ 
  / _ \/ _ `// __/(_-</ __// _ `// _ \ 
 / .__/\_,_//_/  /___/\__/ \_,_//_//_/
/_/                                   
                         @whoamisec

[INF] Retrieving waybackurls...
[RES] Saved waybackurls: out.txt
[INF] Scanning waybackurls...

 => https://www.microsoft.com/en-us/store/movies-and-tv/browse/top-selling?type=movies&studios=Giant%20Pictures&cid=majornelson

    ~ Location :  type=
    ~ Issue(s) :  xss, lfi

 => https://www.microsoft.com/en-us/download/details.aspx?id=26647

    ~ Location :  id=
    ~ Issue(s) :  xss, sqli, ssti, idor
...
```

Parameters and risks:
```json
{
    "q=": [
        "xss"
    ],
    "s=": [
        "xss"
    ],
    "search=": [
        "xss",
        "sqli"
    ],
    "lang=": [
        "xss"
    ],
    "keyword=": [
        "xss",
        "sqli"
    ],
    "query=": [
        "xss",
        "sqli",
        "rce"
    ],
    "page=": [
        "xss",
        "ssrf",
        "lfi",
        "open redirect"
    ],
    "keywords=": [
        "xss"
    ],
    "year=": [
        "xss"
    ],
    "view=": [
        "xss",
        "ssti",
        "sqli",
        "lfi",
        "open redirect"
    ],
    "email=": [
        "xss",
        "idor"
    ],
    "type=": [
        "xss",
        "lfi"
    ],
    "name=": [
        "xss",
        "ssti",
        "ssrf",
        "sqli",
        "lfi"
    ],
    "p=": [
        "xss"
    ],
    "callback=": [
        "xss",
        "open redirect"
    ],
    "jsonp=": [
        "xss"
    ],
    "api_key=": [
        "xss"
    ],
    "api=": [
        "xss"
    ],
    "password=": [
        "xss"
    ],
    "emailto=": [
        "xss"
    ],
    "token=": [
        "xss"
    ],
    "username=": [
        "xss"
    ],
    "csrf_token=": [
        "xss"
    ],
    "unsubscribe_token=": [
        "xss"
    ],
    "id=": [
        "xss",
        "sqli",
        "ssti",
        "idor"
    ],
    "item=": [
        "xss"
    ],
    "page_id=": [
        "xss"
    ],
    "month=": [
        "xss"
    ],
    "immagine=": [
        "xss"
    ],
    "list_type=": [
        "xss"
    ],
    "url=": [
        "xss",
        "ssrf",
        "lfi",
        "open redirect"
    ],
    "terms=": [
        "xss"
    ],
    "categoryid=": [
        "xss"
    ],
    "key=": [
        "xss",
        "idor"
    ],
    "l=": [
        "xss"
    ],
    "begindate=": [
        "xss"
    ],
    "enddate=": [
        "xss"
    ],
    "template=": [
        "lfi",
        "ssti"
    ],
    "preview=": [
        "ssti"
    ],
    "activity=": [
        "ssti"
    ],
    "content=": [
        "lfi",
        "ssti"
    ],
    "redirect=": [
        "ssrf",
        "ssti",
        "open redirect"
    ],
    "access=": [
        "ssrf"
    ],
    "admin=": [
        "ssrf"
    ],
    "dbg=": [
        "ssrf"
    ],
    "debug=": [
        "ssrf"
    ],
    "edit=": [
        "ssrf",
        "idor"
    ],
    "grant=": [
        "ssrf"
    ],
    "test=": [
        "ssrf"
    ],
    "alter=": [
        "ssrf"
    ],
    "clone=": [
        "ssrf"
    ],
    "create=": [
        "ssrf"
    ],
    "delete=": [
        "ssrf",
        "sqli"
    ],
    "disable=": [
        "ssrf"
    ],
    "enable=": [
        "ssrf"
    ],
    "exec=": [
        "ssrf",
        "rce"
    ],
    "execute=": [
        "ssrf",
        "rce"
    ],
    "load=": [
        "ssrf",
        "rce"
    ],
    "make=": [
        "ssrf"
    ],
    "modify=": [
        "ssrf"
    ],
    "rename=": [
        "ssrf"
    ],
    "reset=": [
        "ssrf"
    ],
    "shell=": [
        "ssrf"
    ],
    "toggle=": [
        "ssrf"
    ],
    "adm=": [
        "ssrf"
    ],
    "root=": [
        "lfi",
        "ssrf"
    ],
    "cfg=": [
        "ssrf"
    ],
    "dest=": [
        "ssrf"
    ],
    "uri=": [
        "ssrf",
        "open redirect"
    ],
    "path=": [
        "ssrf",
        "open redirect"
    ],
    "continue=": [
        "ssrf",
        "open redirect"
    ],
    "window=": [
        "ssrf",
        "open redirect"
    ],
    "next=": [
        "ssrf",
        "open redirect"
    ],
    "data=": [
        "ssrf",
        "open redirect"
    ],
    "reference=": [
        "ssrf",
        "open redirect"
    ],
    "site=": [
        "ssrf",
        "open redirect",
        "lfi"
    ],
    "html=": [
        "ssrf",
        "open redirect"
    ],
    "val=": [
        "ssrf",
        "open redirect"
    ],
    "validate=": [
        "ssrf",
        "open redirect"
    ],
    "domain=": [
        "ssrf",
        "open redirect"
    ],
    "return=": [
        "ssrf",
        "open redirect"
    ],
    "feed=": [
        "ssrf",
        "open redirect"
    ],
    "host=": [
        "open redirect",
        "ssrf"
    ],
    "port=": [
        "ssrf",
        "open redirect"
    ],
    "to=": [
        "ssrf",
        "open redirect"
    ],
    "out=": [
        "open redirect",
        "ssrf"
    ],
    "dir=": [
        "ssrf",
        "lfi",
        "rce",
        "open redirect"
    ],
    "show=": [
        "ssrf",
        "lfi",
        "open redirect"
    ],
    "navigation=": [
        "ssrf",
        "open redirect"
    ],
    "open=": [
        "ssrf",
        "open redirect"
    ],
    "file=": [
        "ssrf",
        "lfi",
        "open redirect"
    ],
    "document=": [
        "ssrf",
        "lfi"
    ],
    "folder=": [
        "ssrf",
        "open redirect"
    ],
    "pg=": [
        "ssrf",
        "lfi"
    ],
    "php_path=": [
        "ssrf",
        "lfi"
    ],
    "style=": [
        "ssrf",
        "lfi"
    ],
    "doc=": [
        "idor",
        "ssrf",
        "lfi"
    ],
    "img=": [
        "ssrf"
    ],
    "filename=": [
        "ssrf"
    ],
    "select=": [
        "sqli"
    ],
    "report=": [
        "sqli",
        "idor"
    ],
    "role=": [
        "sqli"
    ],
    "update=": [
        "sqli"
    ],
    "user=": [
        "sqli",
        "idor"
    ],
    "sort=": [
        "sqli"
    ],
    "where=": [
        "sqli"
    ],
    "params=": [
        "sqli"
    ],
    "process=": [
        "sqli",
        "rce"
    ],
    "row=": [
        "sqli"
    ],
    "table=": [
        "sqli"
    ],
    "from=": [
        "sqli"
    ],
    "sel=": [
        "sqli"
    ],
    "results=": [
        "sqli"
    ],
    "sleep=": [
        "sqli"
    ],
    "fetch=": [
        "sqli"
    ],
    "order=": [
        "sqli",
        "idor"
    ],
    "column=": [
        "sqli"
    ],
    "field=": [
        "sqli"
    ],
    "string=": [
        "sqli"
    ],
    "number=": [
        "idor",
        "sqli"
    ],
    "filter=": [
        "sqli"
    ],
    "pdf=": [
        "lfi"
    ],
    "cat=": [
        "lfi",
        "rce"
    ],
    "action=": [
        "lfi"
    ],
    "board=": [
        "lfi"
    ],
    "detail=": [
        "lfi"
    ],
    "date=": [
        "lfi"
    ],
    "download=": [
        "lfi",
        "rce"
    ],
    "prefix=": [
        "lfi"
    ],
    "include=": [
        "lfi"
    ],
    "inc=": [
        "lfi"
    ],
    "locate=": [
        "lfi"
    ],
    "layout=": [
        "lfi"
    ],
    "mod=": [
        "lfi"
    ],
    "conf=": [
        "lfi"
    ],
    "daemon=": [
        "rce"
    ],
    "upload=": [
        "rce"
    ],
    "log=": [
        "rce"
    ],
    "ip=": [
        "rce"
    ],
    "cli=": [
        "rce"
    ],
    "cmd=": [
        "rce"
    ],
    "command=": [
        "rce"
    ],
    "ping=": [
        "rce"
    ],
    "jump=": [
        "rce"
    ],
    "code=": [
        "rce"
    ],
    "reg=": [
        "rce"
    ],
    "do=": [
        "rce"
    ],
    "func=": [
        "rce"
    ],
    "arg=": [
        "rce"
    ],
    "option=": [
        "rce"
    ],
    "step=": [
        "rce"
    ],
    "read=": [
        "rce"
    ],
    "function=": [
        "rce"
    ],
    "req=": [
        "rce"
    ],
    "feature=": [
        "rce"
    ],
    "exe=": [
        "rce"
    ],
    "module=": [
        "rce"
    ],
    "payload=": [
        "rce"
    ],
    "run=": [
        "rce"
    ],
    "print=": [
        "rce"
    ],
    "account=": [
        "idor"
    ],
    "no=": [
        "idor"
    ],
    "group=": [
        "idor"
    ],
    "profile=": [
        "idor"
    ],
    "Lmage_url=": [
        "open redirect"
    ],
    "cgi-bin/redirect.cgi": [
        "open redirect"
    ],
    "cgi-bin/redirect.cgi?": [
        "open redirect"
    ],
    "checkout=": [
        "open redirect"
    ],
    "checkout_url=": [
        "open redirect"
    ],
    "destination=": [
        "open redirect"
    ],
    "file_name=": [
        "open redirect"
    ],
    "file_url=": [
        "open redirect"
    ],
    "folder_url=": [
        "open redirect"
    ],
    "forward=": [
        "open redirect"
    ],
    "from_url=": [
        "open redirect"
    ],
    "go=": [
        "open redirect"
    ],
    "goto=": [
        "open redirect"
    ],
    "image_url=": [
        "open redirect"
    ],
    "img_url=": [
        "open redirect"
    ],
    "load_file=": [
        "open redirect"
    ],
    "load_url=": [
        "open redirect"
    ],
    "login?to=": [
        "open redirect"
    ],
    "login_url=": [
        "open redirect"
    ],
    "logout=": [
        "open redirect"
    ],
    "next_page=": [
        "open redirect"
    ],
    "page_url=": [
        "open redirect"
    ],
    "redir=": [
        "open redirect"
    ],
    "redirect_to=": [
        "open redirect"
    ],
    "redirect_uri=": [
        "open redirect"
    ],
    "redirect_url=": [
        "open redirect"
    ],
    "returnTo=": [
        "open redirect"
    ],
    "return_path=": [
        "open redirect"
    ],
    "return_to=": [
        "open redirect"
    ],
    "return_url=": [
        "open redirect"
    ],
    "rt=": [
        "open redirect"
    ],
    "rurl=": [
        "open redirect"
    ],
    "target=": [
        "open redirect"
    ]

}
```

