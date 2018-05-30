from fogbugz import FogBugz
import csv
import sys

# Fill in the following values as appropriate to your installation
S_FOGBUGZ_URL   = 'https://fogbugz.unity3d.com'
TOKEN			= ""
S_EMAIL         = ''
S_PASSWORD      = ''

fb = FogBugz(S_FOGBUGZ_URL, TOKEN)
#fb.logon(S_EMAIL, S_PASSWORD)

#Get all cases in milestone 2018.2
resp = fb.search(q='milestone:"'+ sys.argv[1] +'"',cols="ixBug")
#print resp
#print sys.argv[1]
filename = "listOfBugz.csv"

csv = open(filename, "w")

for case in resp.cases.childGenerator():
	if case.ixBug.string != None:
		bugID = case.ixBug.string

	row = bugID +","+ "\n"

	csv.write(row)