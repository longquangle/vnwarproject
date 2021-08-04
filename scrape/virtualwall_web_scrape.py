from bs4 import BeautifulSoup
import requests
import csv


links = ['http://www.virtualwall.org/da/0a.htm', 'http://www.virtualwall.org/db/0b.htm', 
'http://www.virtualwall.org/dc/0c.htm', 'http://www.virtualwall.org/dd/0d.htm', 
'http://www.virtualwall.org/de/0e.htm', 'http://www.virtualwall.org/df/0f.htm', 
'http://www.virtualwall.org/dg/0g.htm', 'http://www.virtualwall.org/dh/0h.htm', 
'http://www.virtualwall.org/di/0i.htm', 'http://www.virtualwall.org/dj/0j.htm', 
'http://www.virtualwall.org/dk/0k.htm', 'http://www.virtualwall.org/dl/0l.htm', 
'http://www.virtualwall.org/dm/0m.htm', 'http://www.virtualwall.org/dn/0n.htm', 
'http://www.virtualwall.org/do/0o.htm', 'http://www.virtualwall.org/dp/0p.htm', 
'http://www.virtualwall.org/dq/0q.htm', 'http://www.virtualwall.org/dr/0r.htm', 
'http://www.virtualwall.org/ds/0s.htm', 'http://www.virtualwall.org/dt/0t.htm', 
'http://www.virtualwall.org/du/0u.htm', 'http://www.virtualwall.org/dv/0v.htm', 
'http://www.virtualwall.org/dw/0w.htm', 'http://www.virtualwall.org/dx/0x.htm', 
'http://www.virtualwall.org/dy/0y.htm', 'http://www.virtualwall.org/dz/0z.htm']

## setting up csv file
csv_file = open('virtualwall_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['ID', 'Service Branch', 'Rank', 'Grade at Loss', 'First', 'Middle', 'Last', 
	'Home City', 'Home State', 'Panel', 'Birth', 'Start Tour', 'Incident Date', 
	'Casualty Date', 'Age', 'Death Location', 'Remains', 'Casualty Type', 
	'Casualty Reason', 'Casualty Details'])

## accessing each last name url to find the personal urls
for last_name_url in links:
	print(last_name_url)
	source = requests.get(last_name_url).text
	soup = BeautifulSoup(source, 'lxml').body.table.tr.find('table', class_='blackonwhite').tr.td
	soup = soup.find('table', class_='names').find_all('a')

	for name in soup:
		url_end = str(name).split('"')[1]
		personal_url = 'http://www.virtualwall.org/d' + url_end[0].lower() + '/' + url_end
		
		## accessing the perosnal site
		personal_source = requests.get(personal_url).text
		soup = BeautifulSoup(personal_source, 'lxml')
		info = str(soup.head.find_all('script')).split('"')
		personal_id = info[3]
		branch = info[21]
		rank = info[5]
		grade = info[9]
		first = info[11]
		middle = info[13]
		last =  info[15]
		home_city = info[27]
		home_state = info[29]
		panel = info[31]
		birth = info[35]
		start_tour = info[37]
		incident_date = info[55]
		casualty_date = info[39]
		age = info[41].split(' ')[0]
		location = info[43]
		remains = info[45]
		casual_type = info[47]
		casual_reason = info[49]
		casual_detail = info[51]

		csv_writer.writerow([personal_id, branch, rank, grade, first, middle, last,
			home_city, home_state, panel, birth, start_tour, incident_date, casualty_date, 
			age, location, remains, casual_type, casual_reason, casual_detail])

csv_file.close()
