#!/usr/bin/python3

# Cron set once a week to pull lists for adblocking
# initial list is referencing:
# https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts

import requests
import logging

logging.basicConfig(
        filename="/opt/fyre/dnsmasq/log/adlistout.log", 
        format="%(asctime)s  %(levelname)s  %(message)s",
        level=logging.INFO)

def main():
    logging.info("Starting Adlist Collection....")
    adlist=open('../lib/initial.txt').read().splitlines()
    num_lines = sum(1 for line in open('../lib/initial.txt'))
    if num_lines > 1: 
        logging.info("Additional lists added. Starting collection...")
        for ad in adlist:
            try:
                r = requests.get(ad, timeout=3)
            except requests.exceptions.RequestException as err:
                logging.error("Unable to collect: %s:  %s" % (ad,err))
            else:
                logging.info("Successfully collected: %s" % ad)
                with open("../lib/00-initial.txt","wb") as f:
                    f.write(r.content)
    else:
        logging.info("Zero additions added to adlist, updating initial list")
        for ad in adlist:
            try:
                r = requests.get(ad, timeout=3)
            except requests.exceptions.RequestException as err:
                logging.error("Unable to collect %s:  %s" % (ad,err))
            else:
                logging.info("Successfully collected: %s" % ad)
                with open("../lib/00-initial.txt","wb") as f:
                    f.write(r.content)

if __name__ == "__main__":
    main()
