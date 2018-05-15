# ldap_tal

Installing & configuring OpenLDAP with ansible, and managing the DB with python, worked with Ubuntu 16.04

## Notice

Run the ansilbe playbook with the --extra-vars flag, the first var will be the name of the domain, and the second var will be the admin's password.
Example: ansible-playbook playbook.yml --extra-vars "name=example.com pass=Aa123456"
Afterwards, adjust the domain name and the admin's password in the python script, and you're ready to go!