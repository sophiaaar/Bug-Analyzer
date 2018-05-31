from fogbugz import FogBugz
from testrail import *
import csv
import sys

client = APIClient('')
client.user = ''
client.password = ''

plans = client.send_get('get_plans/2&milestone_id=130')

runIdsList = list()

print("getting plans")
for plan in plans:
	planID = plan["id"]
	planWithEntries = client.send_get('get_plan/'+str(planID))

	entries = planWithEntries["entries"]
	for entry in entries:
		runs = entry["runs"]
		for run in runs:
			runID = run["id"]
			runIdsList.append(runID)

testIdsList = list()
print("getting tests")
for runId in runIdsList:
	tests = client.send_get('get_tests/'+str(runId))
	for test in tests:
		testID = test["id"]
		testIdsList.append(testID)

defectsList = list()
print("getting defects")
for testId in testIdsList:
	results = client.send_get('get_results/'+str(testId))
	for result in results:
		defects = result["defects"]
		defectsList.append(str(defects))

print("number of defects "+len(defectsList))

S_FOGBUGZ_URL   = ''
TOKEN			= ""
S_EMAIL         = ''
S_PASSWORD      = ''

fb = FogBugz(S_FOGBUGZ_URL, TOKEN)
#fb.logon(S_EMAIL, S_PASSWORD)

#Get all cases in milestone 2018.2
resp = fb.search(q='milestone:"'+ sys.argv[1] +'"',cols="ixBug,sTitle,sArea")
#print resp
#print sys.argv[1]
filename = "listOfBugz.csv"

bugIdsList = list()

csv = open(filename, "w")
#check if 
for case in resp.cases.childGenerator():
	if case.sTitle.string != None:
		title = case.sTitle.string.encode('utf-8').decode('ascii', 'ignore').replace(',',' ')
	else:
		title = "No Title"

	if case.sArea.string != None:
		area = case.sArea.string.replace(',',' ')
	else:
		area = ""

	if case.ixBug.string != None:
		bugID = case.ixBug.string
		bugIdsList.append(bugID)

		if bugID in defectsList:
			inTestrail = "true"
		else:
			inTestrail = "false"

		row = bugID +","+ area +","+ title +","+ inTestrail +","+ "\n"
		csv.write(row)


