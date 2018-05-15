# Importing ldap lib
import ldap
import ldap.modlist

# Domain name - Change it so it will match your domain name
dc = "dc=test;dc=com"

# Connecting to the LDAP server, here, the server is the localhost
con = ldap.initialize('ldap://127.0.0.1')

# Binding to the server with admin credentials - change the password for the password that you've
# used in the SLAPD configuration
con.simple_bind_s("cn=admin," + dc,"Aa123456")

# ---------------------------------------------

# Functions to manage Users
def getUsers():
        users = con.search_s(dc, ldap.SCOPE_SUBTREE, "(objectClass=inetOrgPerson)")
        print(users)

def deleteUser(dn):
        con.delete_s(dn)

# Class for the User object
class User:
        # ou isn't mandatory - if not specified, will create in root dir
        def __init__(self, firstName, lastName, password, ou=None):
                self.firstName = firstName
                self.lastName = lastName
                self.password = password
                self.ou = ou
                if(self.ou != None):
                        self.dn = "cn=" + self.firstName + ' ' + self.lastName + ";ou=" + self.ou +
                        ";" + dc
                else:
                        self.dn = "cn=" +  self.firstName + ' ' + self.lastName + ";" + dc

                # Configuring the object's properties
                modlist = {
                        "objectClass": ["inetOrgPerson"],
                        "uid": [self.firstName],
                        "sn": [self.lastName],
                        "givenName": [self.firstName + ' ' + self.lastName],
                        "cn": [self.firstName + ' ' + self.lastName],
                        "displayName": [self.firstName + ' ' + self.lastName],
                        "userPassword": [self.password]
                        }
                con.add_s(self.dn, ldap.modlist.addModlist(modlist))

# Functions to manage OUs
def getOUs():
        ous = con.search_s(dc, ldap.SCOPE_SUBTREE, "(objectClass=organizationalUnit)")
        print(ous)

def deleteOU(dn):
        con.delete_s(dn)

# Class for the OU object
class OU:
        # ou isn't mandatory - if not specified, will create in root dir
        def __init__(self, name, ou=None):
                self.name = name
                if(self.ou != None):
                        self.dn = "ou=" + self.name + ";ou=" + self.ou + ";" + dc
                else:
                        self.dn = "ou=" + self.name + ";" + dc
                modlist = {
                        "objectClass": ["organizationalUnit"]
                        }
                con.add_s(self.dn, ldap.modlist.addModlist(modlist))

# Functions to manage Devices
def getDevices():
        devices = con.search_s(dc, ldap.SCOPE_SUBTREE, "(objectClass=device)")
        print(devices)

def deleteDevice(dn):
        con.delete_s(dn)

# Class for the Device object
class Device:
        # ou isn't mandatory - if not specified, will create in root dir
        def __init__(self, name, desc, ou=None):
                self.name = name
                self.desc = desc
                self.ou = ou
                if(self.ou != None):
                        self.dn = "cn=" + self.name + ";ou=" + self.ou + ";" + dc
                else:
                        self.dn = "cn=" + self.name + ";" + dc
                modlist = {
                        "objectClass": ["device"],
                        "description": [self.desc]
                        }
                con.add_s(self.dn, ldap.modlist.addModlist(modlist))