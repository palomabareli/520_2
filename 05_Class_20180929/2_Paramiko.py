import paramiko

try:
    client = paramiko.client.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # client.connect('127.0.0.1',
    #         username =  'bran',
    #         password = '4linux',
    #         port = '2222'
    #     )   
     
    client.connect('192.168.202.8',
            username = 'sabado',
            password = 'sabado'
        )    
except Exception as ex:
    print('Error in the aplication: {0}'.format(ex.message))
    exit()


stdin, stdout, stderr = client.exec_command('ls -la')    
#stdin, stdout, stderr = client.exec_command('cat /etc/*-release')    

if (stdout.channel.recv_exit_status() == 0):
    print(stdout.read().decode('utf-8'))
else:
    print(stderr.read().decode('utf-8'))  

