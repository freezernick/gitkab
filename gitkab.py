import argparse, requests, os

# Used for loading the config
scriptDirectory = os.path.dirname(__file__)

# argparse
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

config_parser = subparsers.add_parser('config') # gitkab config
config_subparser = config_parser.add_subparsers()
config_parser.add_argument('--key')
config_parser.add_argument('--update', action='store_true')

config_user = config_subparser.add_parser('user') # gitkab config user ...
config_user_group = config_user.add_mutually_exclusive_group(required=True)
config_user_group.add_argument('--list', action='store_true') # gitkab config user --list
config_user_group.add_argument('--add', action='store_true') # gitkab config user --add
config_user_group.add_argument('--remove', action='store_true') # gitkab config user --remove

def listUsers(args):
    print("list")

def addUser(args):
    print("add")

def removeUser(args):
    print("remove")

def writeConfig(args):
    print("wrote")

def readConfig(args):
    print("read")

def getNamespaces(pk):
    headers = {'PRIVATE-TOKEN': pk}
    response = requests.get('https://gitlab.com/api/v4/namespaces?per_page=100', headers=headers)
    if(response.headers.get('X-Total-Pages') > 1):
        # do stuff
        print("test")
    print(response.text)

args = parser.parse_args()

if(args.key):
    # save / overwrite api key
    print("Updated key")
elif (args.update):
    # load key from config / request
    print("Updated namespaces")