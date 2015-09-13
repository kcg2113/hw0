fname = 'iowa-liquor-sample.csv'
sms = 'single malt scotch'
num_sms = 0

with open(fname, 'r') as f:
	for line in f:
		if sms in line.lower():
			num_sms += 1
		
print 'number of single malt scotches: %s' %  num_sms
