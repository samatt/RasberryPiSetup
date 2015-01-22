#Introduction to Raspberry Pi



##What is a Pi?

It is a computer similar to your smartphone or Kindle.
The chip used by the Pi is Broadcomms [BCM2835](https://www.broadcom.com/products/BCM2835)
The Raspberry PI is not an Arduino. 
Gist of it:

*"Comparing a Pi to an Arduino is like comparing a computer to a calculator."*

For a more detailed explanation look at  [this](https://www.adafruit.com/blog/2012/06/18/ask-an-educator-whats-the-difference-between-arduino-raspberry-pi-beagleboard-etc/) blog post on the Adafruit forums.	 

###The Different Models

####Model B+ 
Higher Spec Variant
####Model A+ 
Cheaper, smaller lower power They have others too but not relevant to this lesson



##Communicate with a Pi

###Communicate with a Keyboard and Display

Plug it in!


###Communicate without a Keyboard and Display (over the network)

Communicate with your Pi over a network. The network can either be your home Wi-Fi network, although this will require you to buy a Wi-Fi USB dongle for your pi and configure it to connect to your home Wi-Fi network. Good tutorials on how to connect to NYUs network by [Matt Richardson](https://docs.google.com/a/nyu.edu/document/d/1CXp9Hwm-kh6nZVjRzpAuHjSdQKQT_qWp8dytm3bdNJM/edit#) and [Sergio Majluf](http://itp.nyu.edu/~sam926/raspberry-pi-how-to-config-wi-fi-from-the-command-prompt/).

####Setting up a Static IP on eth0 

This is useful if you want to run your Pi headless and control it from your laptop. (Easiest way to communicate with it in my opinion).

*Note: You'll probably want to do this setup when you are connected to the Pi via a screen*

Your network configuration is stored in the following file: ```/etc/network/interfaces```
so to change it you execture the following command

```
sudo nano /etc/network/interfaces
```

Once the file opens you'll see something like this

```
iface eth0 inet dhcp
```

which you'll want to change to something like this:

```
# iface eth0 inet dhcp
auto eth0
	iface eth0 inet static
	address 192.168.0.10
	netmask 255.255.255.0
```
the # is a comment but it has to to be there from the start of the line.
For more info on the interfaces file you can look at the [Ubuntu interfaces man page](http://manpages.ubuntu.com/manpages/lucid/man5/interfaces.5.html). It may be slightly different but should conver the basics of the syntax that you will use.

**Ctrl+X**  followed by yes to save

Reboot the ethernet interface using the follow two commands consecituvely.

```
sudo ifdown eth0 
sudo ifup eth0
```

Run ```ifconfig``` to see the state of your networks interfaces. You should see something like this:

```
eth0     Link encap:Ethernet  HWaddr 10:fe:ed:25:45:d3  
          inet addr:192.168.0.10  Bcast:255.255.255.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:1545 errors:0 dropped:0 overruns:0 frame:0
          TX packets:923 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:200286 (195.5 KiB)  TX bytes:160211 (156.4 KiB)
```

important things in that block is:

```inet addr:192.168.0.10```
It shows you the IP that you just assigned the ethernet interface. 
This can be now used to ssh in to the Pi.

#####One important thing

If you are going to SSH into PI you need to make sure the ethernet interface of your Mac is set up on the same IP subnet so you should set the ethernet interface of your Mac to be something like 192.168.0.11 (anything between 1 and 254 that is not 10, since the pi is assigned on 10)

Works really well with the [Sublime SFTP Package](http://wbond.net/sublime_packages/sftp)


####Setting up Wi-Fi for your network

If you have a network called Something that has a password Otherthing you can set up that your pi to connect to that network by simply adding the folvocolowing block to the interfaces file. If you wanted to connect to the itpsandbox this is where you would put the network name and password in. (*You will have to registed the MAC address with NYU, more infor on that in Matts tutorial reference above*)

```
auto wlan0
	wpa-ssid "Something"
	wpa-psk	 "otherthing"
```

For more info go to the excellent [Adafruit Tutorial](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-3-network-setup/setting-up-wifi-with-occidentalis) on the subject


##Sublime SFTP package tricks
Keep a copy of the sftp-config.json file in whatever folder of your mac you want to copy to the pi

In that folder you'll basically only want to tweak this block

```
"host": "192.168.0.202",
    "user": "pi",
    "password": "raspberry",
    //"port": "22",    
    "remote_path": "/home/pi/NAME_OF_FOLDER_ON_MAC",
```

In order for this to work you have to first log on to the Pi and creat the folder at the appropriate location and it has to be the same name as the folder on your mac.

##Resources
[Installing img on SD card](http://www.raspberrypi.org/documentation/installation/installing-images)

[Remote Access](http://www.raspberrypi.org/documentation/remote-access/README.md)

[Installing node on the RPi](https://www.adafruit.com/blog/2014/06/13/installing-and-using-node-js-on-raspberry-pi/)
