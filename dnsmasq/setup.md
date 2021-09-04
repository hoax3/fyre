# Fyre dnsmasq Configuration
Adblocking setup for Fyre
### Setup
Install dnsmasq    
`pacman -S dnsmasq`  

Stop dnsmasq from running to make changes  
`sudo systemctl stop dnsmasq`  

Make a backup of the original dnsmasq conf  
 `cp /etc/dnsmasq.conf /etc/dnsmasq.conf.bak`   
 
Remove the orginial conf file and create a new file with the following settings  
`rm /etc/dnsmasq.conf && vim /etc/dnsmasq.conf`  

```bash
no-dhcp-interface=eth0
cache-size=1000
domain-needed
bogus-priv
dns-forward-max=150
no-poll
server=8.8.8.8
server=8.8.4.4
no-resolv
log-queries=extra
log-facility=/opt/fyre/dnsmasq/log/dnsmasq.log # log output
conf-dir=/opt/fyre/dnsmasq/lists/
#server=/localnet/192.168.1.16 #IP of host
```

> If static address, will set server to ip, if dhcp, will make bash script below to echo IP at startup  
`echo "server=$(hostname -I | awk '{print $1}')" >> /etc/dnsmasq.conf`

### Adblocking
Adlists will be stored in /opt/fyre/dnsmasq/lists   
To add more, just add files into the directory and reload the daemon and dnsmasq service   
`systemctl reload-daemon && systemctl restart dnsmasq`
