#!usr/local/bin

f = open('./input4.txt')

fields = set(['byr','iyr','eyr','hgt','hcl','ecl','pid','cid'])

passport = {}

valid = 0

"""
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
"""
def is_valid(p):
	# this would only run in passports with all keys
	#print p

	if len(p.keys()) <7:
		return False

	if len(p['byr']) != 4 or (int(p['byr']) < 1920 or int(p['byr']) > 2002):
		return False

	if len(p['iyr']) != 4 or (int(p['iyr']) < 2010 or int(p['iyr']) > 2020):
		return False
	
	if len(p['eyr']) !=4 or (int(p['eyr']) < 2020 or int(p['eyr']) > 2030):
		return False

	h = p['hgt']

	
	if 'cm' in h or 'in' in h:
		if 'cm' in h:
			# these are cm
			h = h.split('cm')[0]
			if not h.isdigit() or int(h) < 150 or int(h) >193:
				return False
		elif 'in' in h:
			h = h.split('in')[0]
			if not h.isdigit() or int(h) <59 or int(h) > 76:
				return False

	else:
		return False

	hcl = p['hcl'].split('#')

	if '#' not in p['hcl'] or len(hcl[1])!=6:
		return False
	else:
		hair = hcl[1]
		if not hair.islower()  and not all(i.isalnum() for i in hair): 
			return False

	# amb blu brn gry grn hzl oth	
	color = set(['amb', 'blu', 'brn', 'gry', 'grn','hzl','oth'])
		
	if p['ecl'] not in color:
		return False
	

	if len(p['pid']) != 9 or not  p['pid'].isdigit():
		return False
	
	return True
	
for l in f:
	#print l
	if l.strip() != "":
		items = l.strip().split()
		for e in items:
			(key, value) = e.split(':')
			passport[key] = value
	else:
		# check validity 
		diff = fields.difference(set(passport.keys()))
		#print diff

		if len(diff) == 0:
			if is_valid(passport):
				valid = valid + 1
		elif len(diff) == 1 and diff.pop() == 'cid':
			if is_valid(passport):
				valid = valid + 1
		passport = {}

print "valid"
print valid	
