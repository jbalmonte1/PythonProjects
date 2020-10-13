'''
Created on 17 Feb 2020

@author: jalmonte
'''

import paramiko
from scp import SCPClient

class RemoteAccessTools():
    '''
    This module is used for remotely accessing application's backend components.
    '''

    def __init__(self, ip, username, password, interfaces, ssh_port = 22, sftp_port = 22, pem = None):
        '''
        Constructor. Automatically establishes {interface} connections
        '''
        
        self.remote_info = {'ip': ip, 'username': username, 'password': password, 'ssh_port': ssh_port, 'sftp_port': sftp_port, 'key': pem}
        self.interfaces = [interfaces] if not isinstance(interfaces, list) else interfaces
        self.ssh = ''
        self.sftp = ''
        self.transport = ''
        
        for interface in interfaces:
            print(f'Establishing {interface} connection')
            if interface == 'SSH':
                self._setup_ssh()
            elif interface == 'SFTP':
                self._setup_sftp()
            else:
                raise RuntimeError(f'Interface {interface} not supported')
            
    def __del__(self):
        '''
        Destructor. Automatically closes {self.interface} connections
        '''
        
        for interface in self.interfaces:
            print(f'Closing {interface} connection')
            if interface == 'SSH':
                self.ssh.close()
            elif interface == 'SFTP':
                self.transport.close()
                self.sftp.close()
        
    def _setup_ssh(self):
        '''
        Establishes SSH connection to remote server
        '''
        
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        if self.remote_info['password'] == "":
            self.ssh.connect(self.remote_info['ip'], port=self.remote_info['ssh_port'], username=self.remote_info['username'], key_filename=self.remote_info['key'])
        else:
            self.ssh.connect(self.remote_info['ip'], port=self.remote_info['ssh_port'], username=self.remote_info['username'], password=self.remote_info['password'])
        
        print(f'SSH connection successfully established')
        
    def _setup_sftp(self):
        '''
        Establishes SFTP connection to remote server
        '''
        
        self.transport = paramiko.Transport((self.remote_info['ip'], self.remote_info['ssh_port']))
        self.transport.connect(None, self.remote_info['username'], self.remote_info['password'])

        self.sftp = paramiko.SFTPClient.from_transport(self.transport)
        
        print(f'SFTP connection successfully established')
        
    def execute_ssh_command(self, command, target_dir=None):
        '''
        Executes ssh command from target dir
        '''
        
        if target_dir:
            stdin, stdout, stderr = self.ssh.exec_command(f'cd {target_dir}; {command}')
        else:
            stdin, stdout, stderr = self.ssh.exec_command(command)
        return stdout.read().decode().strip()
        
    def upload_file_through_sftp(self, filename, localpath, remotepath):
        '''
        Uploads file with {filename} from {localpath} to {remotepath} in remote server through sftp
        '''
        
        localpath = localpath + '/' if localpath[-1] != '/' else localpath
        remotepath = remotepath + '/' if remotepath[-1] != '/' else remotepath
        self.sftp.put(f'{localpath}{filename}', f'{remotepath}{filename}')
        
    def download_file_through_sftp(self, filename, remotepath, localpath):
        '''
        Downloads file with {filename} from {remotepath} to {localpath} from remote server through sftp
        '''
        
        localpath = localpath + '/' if localpath[-1] != '/' else localpath
        remotepath = remotepath + '/' if remotepath[-1] != '/' else remotepath
        self.sftp.get(f'{remotepath}{filename}', f'{localpath}{filename}')
        
    def upload_file_through_scp(self, filename, localpath, remotepath):
        '''
        Uploads file with {filename} from {localpath} to {remotepath} in remote server through sftp
        '''
        
        localpath = localpath + '/' if localpath[-1] != '/' else localpath
        remotepath = remotepath + '/' if remotepath[-1] != '/' else remotepath
        
        with SCPClient(self.ssh.get_transport()) as scp:
            scp.put(f'{localpath}{filename}', recursive=True, remote_path=f'{remotepath}')
            
    def download_file_through_scp(self, filename, localpath, remotepath):
        '''
        Downloads file with {filename} from {localpath} to {remotepath} in remote server through sftp
        '''
        
        localpath = localpath + '/' if localpath[-1] != '/' else localpath
        remotepath = remotepath + '/' if remotepath[-1] != '/' else remotepath
        
        with SCPClient(self.ssh.get_transport()) as scp:
            scp.get(f'{remotepath}{filename}', f'{localpath}')