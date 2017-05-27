import os
import xml.etree.ElementTree

testres = {}
total_instances = 10
total_builds = 100

# fetch ip address from hosts
ip = ['138.197.13.204','138.197.69.93','138.197.78.172','138.197.7.242','138.197.69.168','138.197.13.156','138.197.69.169','138.197.13.132','138.197.69.37','138.197.69.164']

for instance in range(total_instances):
	for i in range(total_builds/total_instances):
		# command to copy xml to ansible server
		command = 'scp root@' + str(ip[instance]) + ':/var/lib/jenkins/jobs/iTrust-fuzz/builds/' + str(i+1) + '/iTrust*/junitResult.xml .'
		os.system(command)
		e = xml.etree.ElementTree.parse('junitResult.xml')
		for suite in e.iter('suite'):
			for cases in suite:
				for case in cases:
					testname = suite.find('name').text + case.find('testName').text
					if testname not in testres:
						testres[testname] = [0]
					elif len(testres[testname]) != i + 1:
						testres[testname].append(0)

					if (len(case.findall('errorStackTrace')) == 1):
						testres[testname][-1] = 1

		print 'total testcases read ' + str(len(testres))


f = open("useless.txt","w+")
count = 0
for key in testres:
	if 1 in testres[key]:
		continue
	else:
		f.write(key)
		f.write("\n")
		count += 1

f.write("\nTotal Useless Tests " + str(count) + "\n\n")

f = open("failure.txt","w+")
newcount = 0
for key in testres:
	if 1 in testres[key]:
		f.write(key)
		f.write("\nfailed in builds ")
		indices = [i for i, x in enumerate(testres[key]) if x == 1]
		newindices = [x+1 for x in indices]
		str1 = ','.join(str(e) for e in newindices)
		f.write(str1)
		f.write("\n\n")
		newcount += 1
	else:
		continue
f.write("\nTotal Failed Testcases " + str(newcount) + "\n\n")

