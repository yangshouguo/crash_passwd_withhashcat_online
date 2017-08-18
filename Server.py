#!/usr/bin/env python
# coding=utf-8


from SocketServer import StreamRequestHandler,ThreadingTCPServer
import traceback
import time
import os
host = "" #监听本地IP
port = 7890 #监听本地端口
sock = (host,port)
log_dir_name = 'log.dat'
log_dir_file = ''
execute_cmd = 'python crack_with_hashcat.py '
seprate = '--------------------------------------'
#用于处理socket请求，读取协议内容，执行请求，返回数据
class MStreamRequestHandler(StreamRequestHandler):
    def handle(self):

            try:
                sock = self.request
                newdata_fromclient = sock.recv(1024) #
                print 'connected by ',self.client_address
                print 'data:',newdata_fromclient
                temp = newdata_fromclient.split(' ')
                #result = self.get_crash_result(temp[0],temp[1])
                result = ','.join(temp)
                sock.sendall(result)
            except:
                traceback.print_exc()
                log_dir_file.write('error')
                return
            finally:
                print 'connect break from',self.client_address
    def get_crash_result(self,hashvalue, which_dic):#hashvalue -> 哈希串 ， which_dic -> 指定某一种字典
        time1 = time.localtime()
        back_cmd = '\'%s\' %s.dict' %(hashvalue,which_dic)
        new_cmd = execute_cmd+back_cmd
        returndata = os.popen(new_cmd)
        result = returndata.read()
        if (len(result)<1):
            result = '!!!not found!!!'
        time2 = time.localtime()


        log_dir_file.write(seprate)
        log_dir_file.write('from :'+self.client_address)
        log_dir_file.write('hashvalue:' + hashvalue)
        log_dir_file.write('dict:'+which_dic)
        log_dir_file.write('start time and end time :'+time1+" "+time2)
        log_dir_file.write(seprate)
        
        return returndata
        

def openlogdir():
    log_dir_file = open(log_dir_name , 'a')
    if (not log_dir_file):
        print 'error when open log file'
def main():
    openlogdir() #打开日志文件
    server = ThreadingTCPServer(sock, MStreamRequestHandler)
    server.serve_forever()

if __name__ == '__main__':
    main()


