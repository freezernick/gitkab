import argparse, requests, os, configparser

# Used for loading the config
scriptDirectory = os.path.dirname(__file__)
cfgpath = os.path.join(scriptDirectory, 'config.cfg')

# argparse
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

def configure(args):
    if(args.key):
        read()
        config['Gitlab']['Key'] = args.key
        write()

def write():
    global config
    with open(cfgpath, 'w+') as configfile:
        config.write(configfile)

# configparser
config = configparser.ConfigParser()

config_parser = subparsers.add_parser('config') # gitkab config
config_subparser = config_parser.add_subparsers()
config_parser.set_defaults(func=configure)
config_parser.add_argument('--key')
config_parser.add_argument('--update', action='store_true')

config_user = config_subparser.add_parser('user') # gitkab config user ...
config_user_group = config_user.add_mutually_exclusive_group(required=True)
config_user_group.add_argument('--list', action='store_true') # gitkab config user --list
config_user_group.add_argument('--add', action='store_true') # gitkab config user --add
config_user_group.add_argument('--remove', action='store_true') # gitkab config user --remove

args = parser.parse_args()

if(os.path.exists(cfgpath) == False):
    print("No config found!")
    config.add_section('GitLab')
    print("Please enter your API key:")
    config['GitLab']['Key'] = input()
    config.add_section('Namespaces')
    write()
    exit()

def listUsers(args):
    print("list")

def addUser(args):
    print("add")

def removeUser(args):
    print("remove")

def read():
    global config
    config.read(cfgpath)

def getNamespaces(pk):
    headers = {'PRIVATE-TOKEN': pk}
    response = requests.get('https://gitlab.com/api/v4/namespaces?per_page=100', headers=headers)
    if(response.headers.get('X-Total-Pages') > 1):
        # do stuff
        print("test")
    print(response.text)