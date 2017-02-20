import os
import numpy as np
import random
import string


def init_int(var,num): # 1, [int a = 3;]
    line_out = "  int "+str(var)+" = "+str(num)+";"
    cnt = 1
    return cnt, line_out

def init_char(var): # 1, [char a = 'b';]
    line_out = "  char "+str(var)+" = '"+random.choice(string.ascii_letters)+"';"
    cnt = 1
    return cnt, line_out

def init_char_arr(var,num): # 1, [char source[40] = "";]
    str_out = "  char "+str(var)+"["+str(num)+'] = "";'
    cnt = 1
    return cnt, str_out

def init_char_p(var): # 1, [char* dest;]
    str_out = "  char* "+str(var)+";"
    line_out=str_out+"\n  "+var+" = NULL;"
    cnt = 2
    return cnt, line_out

def alloc_int(var,num): # 1, [entity1 = 40;]
    line_out="  "+var+" = "+str(num)+";"
    cnt = 1
    return cnt, line_out

def alloc_char_arr(var,num): # 2, [memset(source, 'C', 100-1);\nsource[100-1]='\0';]
    rand_char = random.choice(string.ascii_letters)
    str_out="  memset("+var+", '"+rand_char+"', "+str(num)+"-1);"
    line_out=str_out+"\n  "+var+"["+str(num)+"-1]='\0';"
    cnt = 2
    return cnt, line_out

def alloc_char_p(var,num): # 2, [memset(source, 'C', 100-1);\nsource[100-1]='\0';]
    str_out='  '+var+" = (char*)malloc("+str(num)+"*sizeof(char));"
    line_out=str_out+"\n  "+var+"["+str(num)+"-1]='\0';"
    cnt = 2
    return cnt, line_out