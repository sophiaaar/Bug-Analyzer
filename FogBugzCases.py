from fogbugz import FogBugz
from testrail import *
import csv
import sys

client = APIClient('')
client.user = ''
client.password = ''

plans = client.send_get('get_plans/2')
#tests = client.send_get('get_tests/5696')
#print(plans)
#plansStr = ''.join((str(v) for v in plans))

#planIDsList = list()

for plan in plans:
	planID = plan["id"]
	planWithEntries = client.send_get('get_plan/'+planID)
	#print(planID)
#	planIDsList.append(planID)

#for plan_id in planIDsList:
#	planWithEntries = client.send_get('get_plan/'+plan_id)

#file = open("plansOutput.txt", "w")
#file.write(plansStr)
#file.close()

#file2 = open("testsOutput.txt", "w")
#testsStr = ''.join((str(x) for x in tests))
#file2.write(testsStr)
#file2.close()

S_FOGBUGZ_URL   = ''
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