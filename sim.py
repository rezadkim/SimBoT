#Simsimi
#Rekode authornya cantumin lah kontol
#Kau kira tools bapak kau yang buat?

import requests,os,json

#WARNA
merah = "\033[1;91m"
lime = "\033[1;92m"
blue = "\033[1;96m"
putih = "\033[1;97m"
kuning = "\033[1;93m"
tutup = "\033[0m"
url = "https://wsapi.simsimi.com/190410/talk/"

logo = kuning+"""
   _____       ___     ______
  / __(_)_ _  / _ )___/_  __/
 _\ \/ /  ' \/ _  / _ \/ /   
/___/_/_/_/_/____/\___/_/"""+tutup

def bahasa():
	global bhs
	os.system('reset')
	print logo
	print
	print lime+"{1} "+putih+"Indonesia"
	print lime+"{2} "+putih+"English"
	print merah+"{0} "+putih+"Exit"
	print
	lang = raw_input(lime+"[+] "+tutup+"Bahasa : ")
	if lang in ['1','01']:
		bhs = "id"
		main()
	elif lang in ['2','02']:
		bhs = "en"
		main()
	else:
		exit(merah+"\n[!]"+tutup+" Exit")
		

def main():
	try:
		os.system('reset')
		print logo
		print u'\u001b[2m { "Author" : "ZeDD Parker"'
		print u'\u001b[2m   "Media" : {'
		print u'\u001b[2m      "Fb_id" : "parkergans3"'
		print u'\u001b[2m      "Ig" : "@rezadkim"'
		print u'\u001b[2m      "GitHub" : "https://github.com/rezadkim"'
		print u'\u001b[2m    }'
		print u'\u001b[2m }'+tutup
		print
		nama = raw_input(lime+"[+] "+tutup+"Nama : ")
		api  = raw_input(lime+"[+] "+tutup+"Api KEY : ")
		print
		while(True):
			try:
				msg = raw_input(blue+"     [+] "+tutup+nama+" : ")
				payload = "{\n\t\"utext\": \"%s\", \n\t\"lang\": \"%s\" \n}"%(msg,bhs)
				headers = {'Content-Type':"application/json",'x-api-key':api} #<-API KEY
				respon = requests.request("POST",url,data=payload,headers=headers)
				y = json.loads(respon.text)
				print kuning+"     [+]"+tutup+" Simi : "+y["atext"]
			except KeyboardInterrupt:
				exit(merah+"\n[!]"+tutup+" Exit")
			except KeyError:
				exit(merah+"\n[!]"+tutup+" Api Key Invalid")
	except KeyboardInterrupt:
		exit(merah+"\n[!]"+tutup+" Exit")
		
if __name__=="__main__":
	bahasa()
