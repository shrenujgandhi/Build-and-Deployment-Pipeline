[<img src="https://github.com/shrenujgandhi/Readme-Images/blob/master/AP.png" width="150">](https://github.com/shrenujgandhi/Build-and-Deployment-Pipeline)
[<img src="https://github.com/shrenujgandhi/Readme-Images/blob/master/DO.png" width="90">](https://github.com/shrenujgandhi/Build-and-Deployment-Pipeline)

# Build and Deployment Pipeline

## Screencast
[Build and Deployment Pipeline](https://drive.google.com/file/d/0B9erCuXnrQQrQ2N6bVU0WHV2VnM/view)  
[Fuzzing and Test Coverage](https://drive.google.com/file/d/0B9erCuXnrQQrZnFsM00yV0x6aFU/view)  

## Arhitecture Diagram
The initial setup performed by the ansible scripts is depicted in the diagram below  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src="https://github.com/shrenujgandhi/Build-and-Deployment-Pipeline/blob/master/images/Architecture%20Diagram.jpg" width="800">  
Once the setup is completed, developer can work in the repository and when a push is executed, Jenkins build job will be triggered. If the build succeeds, then the built package is deployed automcatically to the production servers. This is how CI is achieved.

## Features
- [Srcipt](https://github.com/shrenujgandhi/Build-and-Deployment-Pipeline/blob/master/droplet.py) to spawn Digital Oceans's droplet instance
- Jenkins build from github repo using maven and git plugin [script](https://github.com/shrenujgandhi/Build-and-Deployment-Pipeline/blob/master/roles/config-jenkins/tasks/main.yml#L87)
- Jenkins code coverage report using cobertura plugin [script](https://github.com/shrenujgandhi/Build-and-Deployment-Pipeline/blob/master/roles/config-jenkins/tasks/main.yml#L93)
- Python script to perfom fuzzing [script](https://github.com/shrenujgandhi/Build-and-Deployment-Pipeline/blob/master/roles/fuzzing/files/fuzzer.py)
- [Ansible script](https://github.com/shrenujgandhi/Build-and-Deployment-Pipeline/tree/master/roles/config-ansible/files) to perform rolling deployment on `git push` using `post-receive` hook

## References
* [iTrust application instructions](http://agile.csc.ncsu.edu/iTrust/wiki/doku.php?id=home_deployment_instructions)
* [iTrust Application](https://github.ncsu.edu/engr-csc326-staff/iTrust-v23/tree/master/iTrust)
* [Tomcat installation](https://github.com/ansible/ansible-examples/blob/master/tomcat-standalone/roles/tomcat/tasks/main.yml)
* [Java installation](http://stackoverflow.com/questions/19275856/auto-yes-to-the-license-agreement-on-sudo-apt-get-y-install-oracle-java7-instal)
* [Ansible edit line in file](http://docs.ansible.com/ansible/lineinfile_module.html)
* [Ecplise installation](https://github.com/caarlos0/ansible-role-eclipse/blob/bb17568189047dc6e702f1bffd4a47ac571ed5ed/tasks/install_Ubuntu.yml)
* [SSH congiurations](http://debuggable.com/posts/disable-strict-host-checking-for-git-clone:49896ff3-0ac0-4263-9703-1eae4834cda3)
* [Droplet API](https://developers.digitalocean.com/documentation/v2/#droplets)
* [Files in python](https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files)
* [Python Droplet issues](https://github.com/koalalorenzo/python-digitalocean/issues/59)
* [Droplet API Issues](https://github.com/digitalocean/api-v2/issues/92)
* [Article on rolling update](http://docs.ansible.com/ansible/guide_rolling_upgrade.html)
* [Ansible Docs](http://docs.ansible.com/ansible/fetch_module.html)
* [Ansible issues](https://github.com/ansible/ansible/issues/14064)
* [SQL dump](http://stackoverflow.com/questions/2537486/create-dump-file-from-database-in-mysql)
* [Slurp module](http://docs.ansible.com/ansible/slurp_module.html)

## Attribution
This project was designed and developed by [Shrenuj Gandhi](https://github.com/shrenujgandhi), [Sumeet Agarwal](https://github.com/sumeet29), [Amritanshu Agrawal](https://github.com/amritbhanu) and Jeewan Khetwani under the supervision of [Dr. Christopher Parnin]().
