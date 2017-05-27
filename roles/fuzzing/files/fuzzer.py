# !/usr/bin/python

import os
import random
import re
import time
import requests
import xml.etree.ElementTree

file_list = []

total_builds = 100
total_instances = 10

for root, dirs, files in os.walk("iTrust/iTrust/src/main/edu/ncsu/csc/itrust/", topdown=False):
    for name in files:
        if name.endswith('.java'):
                # print(os.path.join(root, name))
                file_list.append(os.path.join(root, name))

print len(file_list)

# for every commit
def fuzz():
        # shuffle the array
        random.shuffle(file_list)

        # randomly select more than 100 files to fuzz
        n = random.randint(100, len(file_list))
        fuzz_files = file_list[0:n]
        print len(fuzz_files)


        for i in fuzz_files:
                old = ""
                with open(i, "r") as f:
                        old = f.read()
                new, changes = re.subn('!=', '==', old)

                with open(i, "w") as f:
                        f.write(new)
                # print changes

if __name__=='__main__':
        res = ""
        while(res is None or res == ""):
                time.sleep(60)
                data = requests.get('http://localhost:8090/job/iTrust-coverage/lastBuild/api/json')
                res = data.json().get('result')

        for i in range(total_builds/total_instances):
                fuzz()
                os.system('cd iTrust; git commit -a -m "fuzzing";')
                res = ""
		flag = 0
		start = time.time()
                while(res is None or res == ""):
                        time.sleep(20)
                        data = requests.get('http://localhost:8090/job/iTrust-fuzz/lastBuild/api/json')
                        res = data.json().get('result')
			end = time.time()
			if (end - start > 480 and flag == 0):
				os.system('cd iTrust/iTrust/; mvn clean test;')
				flag = 1
                os.system('cd iTrust; git reset --hard 8919266b5ef0e4232db0d63d6fea79aea09d09cd;')
		os.system('sudo service tomcat restart')
		os.system('sudo service mysql restart')
		time.sleep(7)

