import sys
sys.path.insert(1, '..\\..')

import unittest
from AutomationTools import *

SERVER_IP = '127.0.0.1'
SERVER_USERNAME = 'jbalmonte1'
SERVER_PASSWORD = 'CassiAdmin!'
SERVER_INTERFACES = ['SSH']
SERVER_SSH_PORT = '2222'
SERVER_HOME_DIRECTORY = '/home/jbalmonte1'

def test_decorator(func):
    def print_test_description(*func_args, **func_kwargs):
        print('================')
        print(f'Executing {func.__name__}'.upper())
        print('================')
        return func(*func_args, **func_kwargs)
    return print_test_description

class UnitTestRemoteAccess(unittest.TestCase):
    @test_decorator
    def test_execute_ssh_command(self):
        remote_access = RemoteAccessTools(SERVER_IP, SERVER_USERNAME, SERVER_PASSWORD, SERVER_INTERFACES, SERVER_SSH_PORT)
        self.assertEqual(remote_access.execute_ssh_command("pwd"), SERVER_HOME_DIRECTORY, 'Assertion Failure: Failed to execute SSH command')
        
if __name__ == '__main__':
    unittest.main()
