import os
from fabric.api import *

try:
    from config.fabric import github_username, github_password
    github_username = github_username
    github_access_token = github_password
except ImportError:
    print("Set up config/fabric.py file")

env.hosts = ['localhost']
env.origin = "https://github.com/MaxASchwarzer/RedditClassifier"
env.branch = "master"

git_repository = "/home/max/RedditClassifier"

def start():
    _git_pull()
    with lcd(git_repository), settings(user="max"): # max is a user with blocked network access
        # TODO: Replace below echo with python commands such that results go to output.txt, e.g., local('python build_dictionary.py')
        local('echo "hello" > output.txt')
    with lcd('~/'), settings(sudo_user="root"):
        local('cp ' + os.path.join(git_repository, 'output.txt') + ' ~/output.txt')
        local('uuencode output.txt output.txt > output.tte')
        local('cat output.tte | mail -s "Max\'s Reddit RNN Classifier" seakango@gmail.com')
        local('cat output.tte | mail -s "Max\'s Reddit RNN Classifier" maxa.schwarzer@gmail.com')


def _git_pull():
    with lcd(git_repository):
        with settings(prompts={"Username for 'https://github.com': ": github_username,
                           "Password for 'https://KentShikama@github.com': ": github_password}):
            local('git fetch --all')
        local('git checkout {0}'.format(env.branch))
        local('git reset --hard origin/{0}'.format(env.branch))