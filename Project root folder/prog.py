import re
import json

count=0
with open('websiteData.txt') as data:
	email_hash={}
	for lines in data:#current file is line based file
		lst = re.findall('[a-zA-Z0-9_.!#$%&*+-=?^~]*@[a-zA-Z0-9_]+\.[a-zA-z]{3}\.?[a-za-z]{0,2}',lines)#returns list
		#lst1 =re.findall('^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$',lines)
		if lst:
			for email in lst:
				if email_hash.get(email):
					email_hash[email]['Occurance'] += 1
				else:
					email_hash.update({email:{'Occurance' : 1}})#inserting email as new key and initializing count
					email_name=re.split('@',email)[0]
					if re.search('[a-zA-Z0-9_]+\.[a-zA-Z0-9_]+',email_name) and len(email_name)>=8:
						email_hash[email]['EmailType'] = 'Human'
					else:
						email_hash[email]['EmailType'] = "Non-Human"

print(email_hash)
email_json = json.dumps(email_hash)
with open('result.json','w') as fil:
	fil.write(email_json)

print(email_json)

