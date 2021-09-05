# Fyre dnsmasq Configuration
Adblocking setup for Fyre
### Setup
Install dnsmasq    
`pacman -S dnsmasq`  

Stop dnsmasq from running to make changes  
`systemctl stop dnsmasq`  

Start dnsmasq on boot  
`systemctl enable dnsmasq`  

Make a backup of the original dnsmasq conf  
 `cp /etc/dnsmasq.conf /etc/dnsmasq.conf.bak`   
 
Remove the orginial conf file and create a new file with the following settings  
`rm /etc/dnsmasq.conf && vim /etc/dnsmasq.conf`  

```bash
# DNS
cache-size=1000
domain-needed
bogus-priv
dns-forward-max=150
no-poll
server=8.8.8.8
server=8.8.4.4
local=/fyre.local/
listen-address=::1,127.0.0.1,192.168.1.10
expand-hosts
domain=fyre.local
no-resolv
log-queries=extra
log-facility=/opt/fyre/dnsmasq/log/dnsmasq.log # log output
conf-dir=/opt/fyre/dnsmasq/lib/

# DHCP
dhcp-range=192.168.1.50,192.168.1.200,12h
dhcp-option=option:router,192.168.1.1
dhcp-authoritative
dhcp-leasefile=/opt/fyre/dnsmasq/log/dhcp-leases.log
```

### Adblocking
Adlists will be stored in /opt/fyre/dnsmasq/lib   
To add more, just add files into the initial.txt list and reload the daemon and dnsmasq service   
`systemctl reload-daemon && systemctl restart dnsmasq`
