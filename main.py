import getpass,time
import paramiko
from multiprocessing.dummy import Pool as ThreadPool


USERNAME = raw_input("Please type your login: ")
PASSWORD = getpass.getpass()
HOST = 'localhost'
PORT = 2220
COMMAND = 'sleep 2'
HOSTS_LIST = ['localhost', 'localhost', 'localhost', 'localhost','localhost', 'localhost', 'localhost', 'localhost']


def main():
    start_time = record_time()
    parallel(10)
    tell_time(start_time)
    start_time = record_time()
    loop_run()
    tell_time(start_time)


def exec_command(host):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=USERNAME, password=PASSWORD, port=PORT)
        stdin, stdout, stderr = ssh.exec_command(COMMAND)
        for line in stderr.readlines():
            print line


def parallel(number):
    pool = ThreadPool(number)
    results = pool.map(exec_command, HOSTS_LIST)
    pool.close()
    pool.join()
    return results


def loop_run():
    for host in HOSTS_LIST:
        exec_command(host)


def record_time():
    what_time = time.time()
    return what_time


def tell_time(number):
    print("--- Execution took %s seconds ---" % (record_time() - number))


if __name__ == '__main__':
    main()


__author__ = 'Oleksandr Sechko'