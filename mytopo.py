#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call
from mininet.link import TCIntf
from mininet.util import custom

import requests
import json


def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='10.0.0.0/8')

    info( '*** Adding controller\n' )
    controler0=net.addController(name='controler0',
                      controller=RemoteController,
                      ip='127.0.0.1',                
                      port=6633)

    info( '*** Add switches\n')
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
  

    info( '*** Add hosts\n')
   
    Doctor = net.addHost('Doctor',ip='10.0.0.1')
    Tactile = net.addHost('Tactile',ip='10.0.0.3')
    Robot = net.addHost('Robot',ip='10.0.0.2')
   
    info( '*** Add links\n')   

    net.addLink(Doctor,s1)
    net.addLink(Tactile,s1)
    net.addLink(Robot,s2)
    net.addLink(s1,s2)
   
    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
   
    net.get('s1').start([controler0])
    net.get('s2').start([controler0])

   
    s1.cmd("ovs-vsctl set-manager ptcp:6632")  
    s2.cmd("ovs-vsctl set-manager ptcp:6632")


    info( '*** Post configure switches and hosts\n')
    #client1.cmd("iperf -s -p 1024")
    #enable All
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()
