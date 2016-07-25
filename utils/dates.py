import re

#works only for 1931-2030
def convert_date_UTC(date):
	if re.match(r"\d(\d)?[/:\-]\d[/:\-]", date):
		i = re.match(r"\d(\d)?[/:\-]", date).end()
		date = date[:i] + "0" + date[i:]
	if re.match(r"\d[/:\-]\d(\d)?[/:\-]", date):
		date = "0" + date

	year, month, day = "","",""	
	if re.match(r"\d\d[/:\-]\d\d[/:\-]\d\d(\d\d)?$", date):
		year = date[6:] if re.match(r"\d\d[/:\-]\d\d[/:\-]\d\d\d\d$", date) else ("19" + date[6:] if int(date[6:]) > 30 else "20" + date[6:])
		if int(date[3:5]) > 12:
			day = date[3:5]
			month = date[0:2]
		else:
			day = date[0:2]
			month = date[3:5]
	elif re.match(r"\d\d\d\d[/:\-]\d\d[/:\-]\d\d$", date):
		return date
	else:
		raise ValueError("Not a valid date.")		
		return ""
	return ("%s-%s-%s" %(year, month, day))
