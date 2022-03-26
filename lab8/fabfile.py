 from fabric.api import *


# Set the name of the user login to the remote host
env.user = 'student'
env.port = '8626'
env.hosts =['myvmlab.senecacollege.ca']

# Define the task to get the hostname of remote machines:
def getHostname():
    name = run("hostname")
    print("The host name is:",name)

def installPackage(pkg='dummy'):
    cmd = 'yum install ' + pkg + ' -y'
    status = sudo(cmd)
    print(status)

def removePackage(pkg=''):
    if pkg == '':
       cmd = 'yum remove dummy -y'
    else:
       cmd = 'yum remove ' + pkg + ' -y'
    status = sudo(cmd)
    print(status)


def updatePackage(pkg = ''):
    if pkg == '':
       cmd = 'yum update -y'
    else:
       cmd = 'yum update ' + pkg + ' -y'
    status = sudo(cmd)
    print(status)


