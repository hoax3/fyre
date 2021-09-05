#!/bin/python3

# Cron set once a week to pull lists for adblocking
# initial list is referencing:
# https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts

import requests

# multiple adlists added to initial.txt 
def multi_list():
    adlist= open('./initial.txt').read().splitlines()
    for ad in adlist:
        r=requests.get(ad)
        status = r.status_code
        if status!=200:
            print("[%s] : Unable to pull from %s" % (status,ad))
        else:
            with open("00-initial.txt","wb") as f:
                f.write(r.content)

# If no additions have been added to initial.txt                
def initial_list():
    adlist=open('./initial.txt',"r").read().splitlines()
    for ad in adlist:
        r=requests.get()
        with open("00-initial.txt","w") as f:
            f.write(response.text)

num_lines = sum(1 for line in open('./initial.txt'))

if num_lines>1:
    multi_list()
else:
    initial_list()

    
