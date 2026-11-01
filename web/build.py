"""Builds app/src/main/assets/index.html from web/template.html and the embedded drum samples (web/kitdata.json)."""
import os
here=os.path.dirname(os.path.abspath(__file__))
s=open(os.path.join(here,'template.html'),encoding='utf-8').read().replace('/*__KITDATA__*/',open(os.path.join(here,'kitdata.json'),encoding='utf-8').read())
head,body=s.split('<div class="app">',1)
full='<!doctype html>\n<html lang="ru">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'+head.replace('<meta name="claude:viewport-fit-sides" content="cover">\n','')+'</head>\n<body>\n<div class="app">'+body+'\n</body>\n</html>\n'
full=full.replace('.app{max-width:560px;margin:0 auto;padding-block:18px 16px;','.app{max-width:560px;margin:0 auto;padding-block:calc(18px + env(safe-area-inset-top,0px)) calc(16px + env(safe-area-inset-bottom,0px));')
open(os.path.join(here,'..','app','src','main','assets','index.html'),'w',encoding='utf-8').write(full)
