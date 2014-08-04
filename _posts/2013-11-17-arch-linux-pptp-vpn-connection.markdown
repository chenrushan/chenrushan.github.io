---
layout: post
title: Arch Linux PPTP Vpn Connection
categories: arch
tags: arch, linux, pptp
---

Config pptp exactly as [arch linux wiki](https://wiki.archlinux.org/index.php/PPTP_VPN_client_setup_with_pptpclient) says except for the routing part.

### 1. Follow wiki steps

* Install pptpclient
* Add username and password to /etc/ppp/chap-secrets.

        <USERNAME> PPTP <PASSWORD> *

* Create tunnel file /etc/ppp/peers/\<your\_vpn\>.

        pty "pptp <vpn_server_addr> --nolaunchpppd"
        name <USERNAME>
        remotename PPTP
        require-mppe-128
        file /etc/ppp/options.pptp
        ipparam <your_vpn>

### 2. Routing

If you don't know what route table is, see next section.

As arch wiki says, you just run `ip route add default dev ppp0` to route all trafic through your VPN. But this may fail depending on the current route table of your system, if there's already a default route, you should first delete it before adding a new one.

* run `ip route` to check if there's already a default route. Each line of the `ip route` output can be used directly as argument to `ip route add`.

    For me, the output is:

        default via 192.168.1.1 dev wlp2s0  metric 302
        69.90.184.209 via 192.168.1.1 dev wlp2s0  src 192.168.1.100
        192.168.1.0/24 dev wlp2s0  proto kernel  scope link  src 192.168.1.100
        192.168.1.0/24 dev wlp2s0  proto kernel  scope link  src 192.168.1.100  metric 302
        192.168.1.100 via 127.0.0.1 dev lo  metric 302

    So there's a default route.

* Keep a note of the current default route, and delete it with the following command.

        ip route del default

* Add new default route through vpn connection.

        ip route add default dev ppp0

* If you turn off vpn, make sure add the old default route.

### 3. Understand route table

Most of the content of this section comes from [this tutorial](http://www.techrepublic.com/article/understand-the-basics-of-linux-routing/)

Take the following route table as example (run `route -n` to get such output).

    Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
    0.0.0.0         192.168.1.1     0.0.0.0         UG    302    0        0 wlp2s0
    69.90.184.209   192.168.1.1     255.255.255.255 UGH   0      0        0 wlp2s0
    192.168.1.0     0.0.0.0         255.255.255.0   U     302    0        0 wlp2s0
    192.168.1.100   127.0.0.1       255.255.255.255 UGH   302    0        0 lo

The meaning of each field is:

* **Destination**: the destination network.

* **Gateway**: the defined gateway for the specified network. 0.0.0.0 is specified if no gateway is needed for the network

* **Genmask**: the netmask for the destination network

* **Iface**: the network interface

* **Flags**
    - `U` means the route is up.
    - `G` means that specified gateway should be used for this route
    - `H` means it is a HOST route and that allows us to see the host to which we are connected to

The first line of the above route table contains a destination of default (shown as 0.0.0.0), which means everything not alreay classified. In this case, everything not destined for 69.90.184.209, 192.168.1.100, 192.168.1.0/255.255.255.0 will be sent to 192.168.1.1 -- which is the forwarding gateway -- and the route to the internet. NOTE that only one default route is allowed at any given time, replacing the default route can be done by first deleting the current one and then adding a new one.

For 192.168.1.0/255.255.255.0 network, no gateway is specify, since it's the local network which does not require a forwarding gateway.
