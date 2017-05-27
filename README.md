# Build and Deployment Pipeline

## Screencast
[Build and Deployment Pipeline](https://drive.google.com/file/d/0B9erCuXnrQQrQ2N6bVU0WHV2VnM/view)  
[Fuzzing and Test Coverage](https://drive.google.com/file/d/0B9erCuXnrQQrZnFsM00yV0x6aFU/view)  

## Arhitecture Diagram


## Features
- [Srcipt](https://github.com/shrenujgandhi/Build-and-Deployment-Pipeline/blob/master/droplet.py) to spawn Digital Oceans's droplet instance
- Jenkins build from github repo using maven and git plugin [script](https://github.com/shrenujgandhi/Build-and-Deployment-Pipeline/blob/master/roles/config-jenkins/tasks/main.yml#L87)
- Jenkins code coverage report using cobertura plugin [script](https://github.com/shrenujgandhi/Build-and-Deployment-Pipeline/blob/master/roles/config-jenkins/tasks/main.yml#L93)
- Python script to perfom fuzzing [script](https://github.com/shrenujgandhi/Build-and-Deployment-Pipeline/blob/master/roles/fuzzing/files/fuzzer.py)
- [Ansible script](https://github.com/shrenujgandhi/Build-and-Deployment-Pipeline/tree/master/roles/config-ansible/files) to perform rolling deployment on `git push` using `post-receive` hook


## Attribution
This project was designed and developed by [Shrenuj Gandhi](https://github.com/shrenujgandhi), [Sumeet Agarwal](https://github.com/sumeet29), [Amritanshu Agrawal](https://github.com/amritbhanu) and Jeewan Khetwani under the supervision of [Dr. Christopher Parnin]().
