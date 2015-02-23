#!/usr/bin/python
import os
import time


nv_version=72#v7r2
burn_begin='<BURN>'
burn_end='</BURN>'



def split_data_file(in_file_name):
    '''
    split input file  to tmp file
    '''

    #FIXME ALL of the file operation need exception handler
    data_file = open(in_file_name,'r')
    data = data_file.readlines()
    
    #get tmp file name as out_tmp_file_modem_0
    #get tmp file name as out_tmp_file_modem_1
    modem_0 = open(out_tmp_file_modem_0,'w')
    modem_1 = open(out_tmp_file_modem_1,'w')

    for line in data:
        if -1 != line.find('MODEM0'):
            modem_0.write(line.strip(' \t'))

        if -1 != line.find('MODEM1'):
            modem_1.write(line.strip(' \t'))
    
    data.close()
    modem_0.close()
    modem_1.close()

    return out_tmp_file_modem_0,out_tmp_file_modem_1

def get_nv_id(in_line):
    if -1 == in_line.find("NV_ID"):
        l=in_line.split('"')
        n=l[2]
        return int(n)
    return 0;

def merge_oper(in_des_file,in_data_file):
    '''
    input:
      in_des_file: target file contains origin nv items
      in_data_file: data file contains new nv items
    output:
      new_`in_des_file`: in the same folder as in_des_file
    '''
    des_file=open(in_des_file,'r')
    des_data=des_file.readlines();
    des_file.close()

    des_data_bak=des_data

    data_file=open(in_data_file,'r')
    new_data=data_file.readlines();
    data_file.close()

    global burn_begin
    global burn_end
    for item in des_data:
        #BURN NV DATA SHOULD BE IGNORED
        if -1 != item.find(burn_begin):
            is_burn_data=True
        if -1 != item.find(burn_end):
            is_burn_data=False
        if True == is_burn_data:
            continue


    
        
def main_proc(in_modem_0,in_modem_1,in_data):
    '''
    data : nv data file name 
    in_modem_0: nv file name for modem 0
    in_modem_1: nv file name for modem 1
    '''

if __name__ == '__main__':
    print 'nv merge tool for seattle & balong v7r2'
