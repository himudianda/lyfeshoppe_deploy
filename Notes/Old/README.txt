## Instructions

Read the Deploy web apps with Docker book that was included and then read on.

## Staging server

The staging server will be driven by Vagrant.

- Move the `Vagrantfile` to the `website/` folder in the LyfeShoppe project
- Read the `staging/instance/settings.py` file and adjust any settings
- Run `vagrant up` from the `website/` folder
- Follow the instructions in the `Vagrantfile` starting on line 150

## Production server

We need to first get the files onto our production server. 

### Get the files from our workstation to production

An install script was created to help automate this for you.

- Open `install/scp-to-ip` and input your server's IP address
- Run `install/scp-to-ip` from the `deploy/` folder in the LyfeShoppe project

### Prepare the production server

Run the commands below from your production server after you've done the above. You only need to do this once when you initially provision a machine. The commands were taken from **Chapter 9** of the **Deploy web apps with Docker** book, additional commands were also added.

Of course you could automate the below commands in a number of ways based on your needs. You could do everything from create a simple shell script all the way to writing a custom Flask application so you can provision and deploy everything through a web interface.

```
# Production database configuration, a few commands below will use these values
DB_DATABASE="lyfeshoppe"
DB_USERNAME="lyfeshoppe"
DB_PASSWORD="bestpassword"


# Prevent CoreOS from updating itself and rebooting
sudo systemctl disable update-engine
sudo systemctl stop update-engine

sudo systemctl disable update-engine-stub
sudo systemctl stop update-engine-stub

# Set up the remote git repos
sudo mkdir -p /var/git/nginx.git /var/git/nginx
sudo mkdir -p /var/git/website.git /var/git/website

sudo git --git-dir=/var/git/nginx.git --bare init
sudo chown -R core:core /var/git/nginx.git
sudo chown -R core:core /var/git/nginx

sudo git --git-dir=/var/git/website.git --bare init
sudo chown -R core:core /var/git/website.git
sudo chown -R core:core /var/git/website

# Move the SSL certificates to the correct location
sudo mv /tmp/lyfeshoppe.crt /etc/ssl/certs
sudo mv /tmp/lyfeshoppe.key /etc/ssl/private
sudo mv /tmp/dhparam.pem /etc/ssl/private

# Move the htpasswd file to the correct location
sudo mv .htpasswd /etc/nginx

# Move the iptables rules
sudo mv /tmp/rules-save /var/lib/iptables
sudo chown root:root /var/lib/iptables/rules-save

# Move the unit files to the correct location
sudo mv /tmp/postgres.service /etc/systemd/system
sudo mv /tmp/redis.service /etc/systemd/system
sudo mv /tmp/celery.service /etc/systemd/system
sudo mv /tmp/website.service /etc/systemd/system
sudo mv /tmp/nginx.service /etc/systemd/system

# Move the git hooks to the correct location
sudo mv /tmp/nginx /var/git/nginx.git/hooks/post-receive
sudo mv /tmp/website /var/git/website.git/hooks/post-receive
chmod +x /var/git/nginx.git/hooks/post-receive
chmod +x /var/git/website.git/hooks/post-receive

# Move the firewall rules to the correct location
sudo mv /tmp/rules-save /var/lib/iptables
sudo chown root:root /var/lib/iptables/rules-save

# Enable and start iptables
sudo systemctl enable iptables-restore
sudo systemctl start iptables-restore

# Restart Docker because we made an iptables change
sudo systemctl restart docker

# Move the instance files to the correct location
sudo mkdir -p /home/core/instance
sudo mv /tmp/__init__.py /home/core/instance
sudo mv /tmp/settings.py /home/core/instance

# Set proper ownership for all of the core user's contents
sudo chown -R core:core /home/core/instance

# Pull in the Docker images we're using that aren't ours
/usr/bin/docker pull redis:2.8.21
sudo systemctl enable redis.service
sudo systemctl start redis.service

/usr/bin/docker pull postgres:9.4.3
sudo systemctl enable postgres.service
sudo systemctl start postgres.service

# ------------------------------------------------------------------------------
# BEFORE PROCEEDING PAST THIS POINT MAKE SURE YOU GIT PUSH BOTH NGINX AND THE
# WEBSITE REPOS FROM YOUR WORKSTATION
# ------------------------------------------------------------------------------

# Enable and start all of the services
sudo systemctl enable celery.service website.service nginx.service
sudo systemctl start celery.service website.service nginx.service

# Initialize the database
/usr/bin/docker exec -it postgres createdb -U postgres "${DB_DATABASE}"
/usr/bin/docker exec -it postgres psql -U postgres -c "CREATE USER ${DB_USERNAME} WITH PASSWORD '${DB_PASSWORD}'; GRANT ALL PRIVILEGES ON DATABASE ${DB_DATABASE} to ${DB_USERNAME};"
/usr/bin/docker exec -it website run db init
/usr/bin/docker exec -it website run db seed
```
