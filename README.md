# Using Beaglebone
my enountour with beaglebone black

###For connecting beaglebone thru LAN
 * connect beaglebone to ur laptop via USB
 * then enter in ur terminal
  `ssh ubuntu@192.168.7.2`

###For connecting beagle to wifi
```ssh ubuntu@192.168.7.2
sudo ifconfig wlan2 up
sudo iwlist wlan2 scanning
sudo iwconfig wlan2 essid D-Link_DIR-816
sudo dhclient wlan2```
