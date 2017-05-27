import digitalocean
import time
import requests

def createDroplet(dname):
	user_ssh_key = open('/home/vagrant/.ssh/id_rsa.pub').read()
	droplet = digitalocean.Droplet(token='5d5add6080917f43ba17b4bf4f8fca8c3527e8ed4961cd8a45b2457f8476f7e1',
				name=dname,
				region='nyc2',
				image='ubuntu-14-04-x64',
				size_slug='2gb',
				ssh_keys=['50:93:7e:e5:12:f3:5a:97:f3:68:dc:98:06:0b:c3:93'],
				backups=False)
	droplet.create()
	actions = droplet.get_actions()
	for action in actions:
		while (action.status != 'completed'):
			action.load()
	time.sleep(5)
	headers = {'Content-Type':'application/json', 'Authorization': 'Bearer 5d5add6080917f43ba17b4bf4f8fca8c3527e8ed4961cd8a45b2457f8476f7e1'}
	response = requests.get("https://api.digitalocean.com/v2/droplets/" + str(droplet.id), data={}, headers=headers)
	
	response_json = response.json()
	return response_json['droplet']['networks']['v4'][0]['ip_address']


def createBuildServer():
	ip = createDroplet('jenkins')
	f = open('hosts', 'w+')
	f.write('[jenkins]\n' + ip + ' ansible_ssh_user=root ansible_ssh_private_key_file=~/.ssh/id_rsa\n')
	f.close()
	print "Jenkins server generated"

def createProdServer():
	f = open('hosts','a')
	f.write('\n[prod]\n')
	g = open('roles/config-ansible/files/hosts','w+')
	g.write('[prod]\n')
	for i in xrange(5):
		ip = createDroplet('prod')
		f.write(ip + ' ansible_ssh_user=root ansible_ssh_private_key_file=~/.ssh/id_rsa\n')
		g.write(ip + ' ansible_ssh_user=root ansible_ssh_private_key_file=/root/.ssh/id_rsa\n')
	f.close()
	g.close()
	print "Production servers generated"

createBuildServer()
createProdServer()
print "Hosts file ready!"
