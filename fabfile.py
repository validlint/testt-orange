from fabric.api import env , run as myrun
from fabric.operations import local as localrun


env.name = "local"

def qa(action='start'):
    if action=='start' :
        command= 'up -d'
    else:
        command=action

    localrun("SRCDIR=. DATADIR=.  HTTPPORT=6565 RESTART=no docker-compose -p minisites %s" % command )

def mysql():
	localrun("docker exec -ti minisites_mysql_1 mysql -uroot -ppassword wordpress")

def web():
	localrun("docker exec -ti minisites_web_1 bash")

def dump_mysql():
	localrun("docker exec -ti minisites_mysql_1 mysqldump --opt --lock-tables=false -uroot -ppassword wordpress > /var/www/html/wp-content/uploads/dump.sql")



# In case of sync db
# 
# update wp_options set option_value='http://cdrdev.pilotsystems.net' where option_name = 'home' or option_name = 'siteurl' ;


# TO DEPLOY..

# ADD DEPENDENCIES
# apt-get install python-dev libssl-dev
# wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py
# pip install fabric
# curl -L https://github.com/docker/compose/releases/download/1.12.0/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose && chmod +x /usr/local/bin/docker-compose

# PREPARE SSHKEY and copy it ( deploy_key , and preprod to download data )
# ssh-keygen && cat ~/.ssh/id_rsa.pub 

# CREATE USER
# adduser bpi
# cd /home/bpi/ && git clone ssh://git@pp.webpick.info:2229/pilot/bpi.git
# GET THE DATA
# cd bpi/ && fab sync_down
# UPDATE TABLE : 
# fab mysql  
# RUN QUERY : 
# update wp_options set option_value='http://pp.blog.cinemadureel.org/' where option_name = 'home' or option_name = 'siteurl' ;

