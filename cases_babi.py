import os
import numpy as np
import random
import string
from init_babi import *

def case(num,ver=1.1, use_if=0,max_dummies=10,data_range=100, max_entities=100):

    num_values = 3 # 2 integer values to be compared
    num_variables = 4 # number of entities that will actually be considered
    val = np.random.randint(0,data_range,num_values)+1
    num_dummies=np.random.randint(max_dummies)
    entity_idx = np.random.permutation(max_entities)[:num_variables+num_dummies]
    entity_dict=dict()
    # get entity names (including dummies)
    dummy_dict=dict()
    for i in range(num_variables):
        entity_dict['var_'+str(i+1)]='entity_'+str(entity_idx[i])
    for i in range(num_dummies):
        dummy_dict['var_'+str(i+1)]='entity_'+str(entity_idx[i+4])


    cnt=0 # count lines of sentences
    int_lines = []
    char_lines = []
    true_int_alloc_lines = []
    alloc_lines = []
    false_int_alloc_lines = []
    intro = ['void fun ()','{']
    cnt+=2
    c1=0
    c2=0
    c3=0
    c4=0
    c5=0
    c6=0


    if ver==1.0: # entity1[10]='A'; char[40] entity1=' ';
        input_1 = val[0]

        c1,char_line1 = init_char_arr(entity_dict['var_1'],input_1) # [char source[40] = "";]
        c2,alloc_line1 = alloc_char_arr(entity_dict['var_1'],input_1)
        char_lines.append(char_line1)
        alloc_lines.append(alloc_line1)

        query_line = [entity_dict['var_1']+" [ "+str(val[1])+" ] = '"+random.choice(string.ascii_letters)+"' ;"]
        answer = int(val[0]>val[1])

    elif ver==1.1: # entity1[entity4]='A'; char[40] entity1=' ';
        input_1 = val[0]

        c1,char_line1 = init_char_arr(entity_dict['var_1'],input_1) # [char source[40] = "";]
        c2,alloc_line1 = alloc_char_arr(entity_dict['var_1'],input_1)
        char_lines.append(char_line1)
        alloc_lines.append(alloc_line1)

        c6,int_line4 = init_int(entity_dict['var_4'],val[1])
        int_lines.append(int_line4)

        query_line = [entity_dict['var_1']+" [ "+str(entity_dict['var_4'])+" ] = '"+random.choice(string.ascii_letters)+"' ;"]
        answer = int(val[0]>val[1])

    elif ver==1.2: # entity1[10]='A'; char[entity3] entity1=' '; int entity3 = 8;
        input_1 = entity_dict['var_3']

        c1,char_line1 = init_char_arr(entity_dict['var_1'],input_1) # [char source[40] = "";]
        c2,alloc_line1 = alloc_char_arr(entity_dict['var_1'],input_1)
        char_lines.append(char_line1)
        alloc_lines.append(alloc_line1)

        c5, int_line3 = init_int(entity_dict['var_3'],val[0])
        int_lines.append(int_line3)

        query_line = [entity_dict['var_1']+" [ "+str(val[1])+" ] = '"+random.choice(string.ascii_letters)+"' ;"]
        answer = int(val[0]>val[1])

    elif ver==1.3: # entity1[entity4]='A'; char[40] entity1=' '; entity4= 29; int entity4=8;
        input_1 = val[0]

        c6,int_line4 = init_int(entity_dict['var_4'],val[1])
        int_lines.append(int_line4)

        c1,char_line1 = init_char_arr(entity_dict['var_1'],input_1) # [char source[40] = "";]
        c2,alloc_line1 = alloc_char_arr(entity_dict['var_1'],input_1)
        char_lines.append(char_line1)
        alloc_lines.append(alloc_line1)

        tmp = np.random.randint(2)
        if tmp:
            c4,alloc_line2 = alloc_int(entity_dict['var_4'],val[2])
            val[1]=val[2]
            true_int_alloc_lines.append(alloc_line2)
        else:
            c4,alloc_line2 = alloc_int(entity_dict['var_4'],val[2])
            false_int_alloc_lines.append(alloc_line2)

        query_line = [entity_dict['var_1']+" [ "+str(entity_dict['var_4'])+" ] = '"+random.choice(string.ascii_letters)+"' ;"]
        answer = int(val[0]>val[1])

    elif ver==1.4: # entity1[10]='A'; entity3 = 16; char[entity3] entity1=' '; int entity3 = 8;
        input_1 = entity_dict['var_3']

        c1,char_line1 = init_char_arr(entity_dict['var_1'],input_1) # [char source[40] = "";]
        c2,alloc_line1 = alloc_char_arr(entity_dict['var_1'],input_1)
        char_lines.append(char_line1)
        alloc_lines.append(alloc_line1)

        c5, int_line3 = init_int(entity_dict['var_3'],val[0])
        int_lines.append(int_line3)

        tmp = np.random.randint(2)
        if tmp:
            c6,alloc_line2 = alloc_int(entity_dict['var_3'],val[2])
            val[0]=val[2]
            true_int_alloc_lines.append(alloc_line2)
        else:
            c6,alloc_line2 = alloc_int(entity_dict['var_3'],val[2])
            false_int_alloc_lines.append(alloc_line2)

        query_line = [entity_dict['var_1']+" [ "+str(val[1])+" ] = '"+random.choice(string.ascii_letters)+"' ;"]
        answer = int(val[0]>val[1])

    elif ver==2.0: # strcpy(entity2,entity1);
        input_1 = val[0]
        input_2 = val[1]
        c1,char_line1 = init_char_arr(entity_dict['var_1'],input_1) # [char source[40] = "";]
        c2,alloc_line1 = alloc_char_arr(entity_dict['var_1'],input_1)
        char_lines.append(char_line1)
        alloc_lines.append(alloc_line1)
        c3,char_line2 = init_char_p(entity_dict['var_2']) # char* data;
        c4,alloc_line2 = alloc_char_p(entity_dict['var_2'],input_2) # data = (char *)malloc(50*sizeof(char));
        char_lines.append(char_line2)
        alloc_lines.append(alloc_line2)
        query_line = ["strcpy ( "+entity_dict['var_2']+" , "+entity_dict['var_1']+" ) ;"]
        answer = int(val[0]<=val[1])

    elif ver==2.1: # strcpy(entity2,entity1); char[entity4] entity2=''; int entity4=10;
        input_1 = val[0]
        input_2 = entity_dict['var_4']
        c1,char_line1 = init_char_arr(entity_dict['var_1'],input_1) # [char source[40] = "";]
        c2,alloc_line1 = alloc_char_arr(entity_dict['var_1'],input_1)
        char_lines.append(char_line1)
        alloc_lines.append(alloc_line1)
        c3,char_line2 = init_char_p(entity_dict['var_2']) # char* data;
        c4,alloc_line2 = alloc_char_p(entity_dict['var_2'],input_2) # data = (char *)malloc(50*sizeof(char));
        char_lines.append(char_line2)
        alloc_lines.append(alloc_line2)
        c6,int_line4 = init_int(entity_dict['var_4'],val[1])
        int_lines.append(int_line4)
        query_line = ["strcpy ( "+entity_dict['var_2']+" , "+entity_dict['var_1']+" ) ;"]
        answer = int(val[0]<=val[1])

    elif ver==2.2: # strcpy(entity2,entity1); entity1 = (char*)malloc(entity3 * sizeof(char)); int entity3=10;
        input_1 = entity_dict['var_3']
        input_2 = val[1]
        c1,char_line1 = init_char_arr(entity_dict['var_1'],input_1) # [char source[40] = "";]
        c2,alloc_line1 = alloc_char_arr(entity_dict['var_1'],input_1)
        char_lines.append(char_line1)
        alloc_lines.append(alloc_line1)
        c3,char_line2 = init_char_p(entity_dict['var_2']) # char* data;
        c4,alloc_line2 = alloc_char_p(entity_dict['var_2'],input_2) # data = (char *)malloc(50*sizeof(char));
        char_lines.append(char_line2)
        alloc_lines.append(alloc_line2)
        c5, int_line3 = init_int(entity_dict['var_3'],val[0])
        int_lines.append(int_line3)
        query_line = ["strcpy ( "+entity_dict['var_2']+" , "+entity_dict['var_1']+" ) ;"]
        answer = int(val[0]<=val[1])

    elif ver==2.3: # strcpy(entity2,entity1); char[entity4] entity2=''; entity4 = 20; int entity4=10;
        input_1 = val[0]
        input_2 = entity_dict['var_4']

        c6,int_line4 = init_int(entity_dict['var_4'],val[1])
        int_lines.append(int_line4)

        c1,char_line1 = init_char_arr(entity_dict['var_1'],input_1) # [char source[40] = "";]
        c2,alloc_line1 = alloc_char_arr(entity_dict['var_1'],input_1)
        char_lines.append(char_line1)
        alloc_lines.append(alloc_line1)

        tmp = np.random.randint(2)
        if tmp:
            c4,alloc_line2 = alloc_int(entity_dict['var_4'],val[2])
            val[1]=val[2]
            true_int_alloc_lines.append(alloc_line2)
        else:
            c4,alloc_line2 = alloc_int(entity_dict['var_4'],val[2])
            false_int_alloc_lines.append(alloc_line2)

        c3,char_line2 = init_char_p(entity_dict['var_2']) # char* data;
        c5,alloc_line3 = alloc_char_p(entity_dict['var_2'],input_2) # data = (char *)malloc(50*sizeof(char));
        char_lines.append(char_line2)
        alloc_lines.append(alloc_line3)

        query_line = ["strcpy ( "+entity_dict['var_2']+" , "+entity_dict['var_1']+" ) ;"]
        answer = int(val[0]<=val[1])

    elif ver==2.4: # strcpy(entity2,entity1); entity3 = 80; entity1 = (char*)malloc(entity3 * sizeof(char)); int entity3=10;
        input_1 = entity_dict['var_3']
        c1,char_line1 = init_char_arr(entity_dict['var_1'],input_1) # [char source[40] = "";]
        c2,alloc_line1 = alloc_char_arr(entity_dict['var_1'],input_1)
        char_lines.append(char_line1)
        alloc_lines.append(alloc_line1)
        c3,char_line2 = init_char_p(entity_dict['var_2']) # char* data;

        tmp = np.random.randint(2)
        if tmp:
            c6,alloc_line2 = alloc_int(entity_dict['var_3'],val[2])
            val[0]=val[2]
            true_int_alloc_lines.append(alloc_line2)
        else:
            c6,alloc_line2 = alloc_int(entity_dict['var_3'],val[2])
            false_int_alloc_lines.append(alloc_line2)

        input_2 = val[1]
        c4,alloc_line3 = alloc_char_p(entity_dict['var_2'],input_2) # data = (char *)malloc(50*sizeof(char));
        char_lines.append(char_line2)
        alloc_lines.append(alloc_line3)
        c5, int_line3 = init_int(entity_dict['var_3'],val[0])
        int_lines.append(int_line3)
        query_line = ["strcpy ( "+entity_dict['var_2']+" , "+entity_dict['var_1']+" ) ;"]
        answer = int(val[0]<=val[1])

    elif ver==3.0: # memcpy(entity2,entity1,10*sizeof(char));
        input_1 = val[0]
        input_2 = val[1]
        c1,char_line1 = init_char_arr(entity_dict['var_1'],input_1) # [char source[40] = "";]
        c2,alloc_line1 = alloc_char_arr(entity_dict['var_1'],input_1)
        char_lines.append(char_line1)
        alloc_lines.append(alloc_line1)
        c3,char_line2 = init_char_p(entity_dict['var_2']) # char* data;
        c4,alloc_line2 = alloc_char_p(entity_dict['var_2'],input_2) # data = (char *)malloc(50*sizeof(char));
        char_lines.append(char_line2)
        alloc_lines.append(alloc_line2)
        query_line = ["memcpy ( "+entity_dict['var_2']+" , "+entity_dict['var_1']+" , "+str(input_1)+" * sizeof ( char ) ) ;"]
        answer = int(val[0]<=val[1])

    elif ver==3.1: # memcpy(entity2,entity1,entity4*sizeof(char)); int entity4 = 20;
        input_1 = val[0]
        input_2 = entity_dict['var_4']
        c1,char_line1= init_char_arr(entity_dict['var_1'],input_1) # [char source[40] = "";]
        c2,alloc_line1 = alloc_char_arr(entity_dict['var_1'],input_1)
        char_lines.append(char_line1)
        alloc_lines.append(alloc_line1)
        c3,char_line2 = init_char_p(entity_dict['var_2']) # char* data;
        c4,alloc_line2 = alloc_char_p(entity_dict['var_2'],input_2) # data = (char *)malloc(50*sizeof(char));
        char_lines.append(char_line2)
        alloc_lines.append(alloc_line2)
        c6,int_line4 = init_int(entity_dict['var_4'],val[1])
        int_lines.append(int_line4)
        query_line = ["memcpy ( "+entity_dict['var_2']+" , "+entity_dict['var_1']+" , "+str(input_1)+" * sizeof ( char ) ) ;"]
        answer = int(val[0]<=val[1])

    elif ver==3.2: # memcpy(entity2,entity1,10*sizeof(char));
        input_1 = entity_dict['var_3']
        input_2 = val[1]
        c1,char_line1 = init_char_arr(entity_dict['var_1'],input_1) # [char source[40] = "";]
        c2,alloc_line1 = alloc_char_arr(entity_dict['var_1'],input_1)
        char_lines.append(char_line1)
        alloc_lines.append(alloc_line1)
        c3,char_line2 = init_char_p(entity_dict['var_2']) # char* data;
        c4,alloc_line2 = alloc_char_p(entity_dict['var_2'],input_2) # data = (char *)malloc(50*sizeof(char));
        char_lines.append(char_line2)
        alloc_lines.append(alloc_line2)
        c5, int_line3 = init_int(entity_dict['var_3'],val[0])
        int_lines.append(int_line3)
        query_line = ["memcpy ( "+entity_dict['var_2']+" , "+entity_dict['var_1']+" , "+str(input_1)+" * sizeof ( char ) ) ;"]
        answer = int(val[0]<=val[1])

    elif ver==3.3:
        input_1 = val[0]
        input_2 = entity_dict['var_4']
        c1,char_line1 = init_char_arr(entity_dict['var_1'],input_1) # [char source[40] = "";]
        c2,alloc_line1 = alloc_char_arr(entity_dict['var_1'],input_1)
        char_lines.append(char_line1)
        alloc_lines.append(alloc_line1)

        c3,char_line2 = init_char_p(entity_dict['var_2']) # char* data;
        c4,alloc_line2 = alloc_char_p(entity_dict['var_2'],input_2) # data = (char *)malloc(50*sizeof(char));
        char_lines.append(char_line2)
        alloc_lines.append(alloc_line2)
        c6,int_line4 = init_int(entity_dict['var_4'],val[1])
        int_lines.append(int_line4)

        tmp = np.random.randint(2)
        if tmp:
            c5,alloc_line3= alloc_int(entity_dict['var_4'],val[2])
            val[1]=val[2]
            true_int_alloc_lines.append(alloc_line3)
        else:
            c5,alloc_line3 = alloc_int(entity_dict['var_4'],val[2])
            false_int_alloc_lines.append(alloc_line3)

        query_line = ["memcpy ( "+entity_dict['var_2']+" , "+entity_dict['var_1']+" , "+str(input_1)+" * sizeof ( char ) ) ;"]
        answer = int(val[0]<=val[1])

    elif ver==3.4:
        input_1 = entity_dict['var_3']
        input_2 = val[1]
        c1,char_line1 = init_char_arr(entity_dict['var_1'],input_1) # [char source[40] = "";]
        c2,alloc_line1 = alloc_char_arr(entity_dict['var_1'],input_1)
        char_lines.append(char_line1)
        alloc_lines.append(alloc_line1)
        c3,char_line2 = init_char_p(entity_dict['var_2']) # char* data;
        c4,alloc_line2 = alloc_char_p(entity_dict['var_2'],input_2) # data = (char *)malloc(50*sizeof(char));
        char_lines.append(char_line2)
        alloc_lines.append(alloc_line2)
        c5, int_line3 = init_int(entity_dict['var_3'],val[0])
        int_lines.append(int_line3)

        tmp = np.random.randint(2)
        if tmp:
            c6,alloc_line3 = alloc_int(entity_dict['var_3'],val[2])
            val[0]=val[2]
            true_int_alloc_lines.append(alloc_line3)
        else:
            c6,alloc_line3 = alloc_int(entity_dict['var_3'],val[2])
            false_int_alloc_lines.append(alloc_line3)

        query_line = ["memcpy ( "+entity_dict['var_2']+" , "+entity_dict['var_1']+" , "+str(input_1)+" * sizeof ( char ) ) ;"]
        answer = int(val[0]<=val[1])



    dc=0
    for k,v in dummy_dict.iteritems(): # k : val_1 (set), v : entity_10 (random)
        dc1=0
        dc2=0
        rand_num = np.random.randint(5)
        rand_val = np.random.randint(data_range)
        if rand_num==0:
            dc1,int_line = init_int(v,rand_val)
            int_lines.append(int_line)
        elif rand_num==1:
            dc1, char_line = init_char(v)
            char_lines.append(char_line)
        elif rand_num==2:
            dc1, char_line = init_char_arr(v,rand_val)
            char_lines.append(char_line)
            dc2, alloc_line= alloc_char_arr(v,rand_val)
            alloc_lines.append(alloc_line)
        elif rand_num==3:
            dc1, char_line = init_char_p(v)
            char_lines.append(char_line)
            dc2, alloc_line = alloc_char_p(v,rand_val)
            alloc_lines.append(alloc_line)
        dc+=(dc1+dc2)

    answer_list=['unsafe','safe']
    query_line = [query_line[0]+" # \t"+answer_list[answer]+'\t'+str(0)]
    cnt+=(c1+c2+c3+c4+c5+c6+dc)
    random.shuffle(int_lines)
    random.shuffle(char_lines)
    random.shuffle(alloc_lines)
    lines = intro+int_lines+true_int_alloc_lines+char_lines+alloc_lines+false_int_alloc_lines+query_line+['}']
    lines = '\n'.join(lines)
    query_point = cnt
    return lines,query_point,answer












