Raspberry PI Notes
==================

These are notes that I used to build the API for the Raspberry PI.

Version B revision 1
--------------------

$ cat /proc/cpuinfo
Processor       : ARMv6-compatible processor rev 7 (v6l)
BogoMIPS        : 697.95
Features        : swp half thumb fastmult vfp edsp java tls
CPU implementer : 0x41
CPU architecture: 7
CPU variant     : 0x0
CPU part        : 0xb76
CPU revision    : 7

Hardware        : BCM2708
Revision        : 0002
Serial          : 00000000708f617f

Version B revision 2
--------------------

$ cat /proc/cpuinfo
Processor       : ARMv6-compatible processor rev 7 (v6l)
BogoMIPS        : 847.05
Features        : swp half thumb fastmult vfp edsp java tls
CPU implementer : 0x41
CPU architecture: 7
CPU variant     : 0x0
CPU part        : 0xb76
CPU revision    : 7

Hardware        : BCM2708
Revision        : 000f
Serial          : 000000000efff0ab

Board Types
-----------
See: http://raspberryalphaomega.org.uk/?p=428

Rev. No.  Model  Capabilities
0×2       B1     Original Model B, 256MB RAM, Ethernet, two USB sockets,
                 five LEDs, (P2) JTAG pins, no mounting holes, Pin3=GPIO0,
                 Pin5=GPIO1, Pin13=GPIO21, I2C-0
0×3       B1+    Original Model B with no polyfuses, 256MB RAM, Ethernet,
                 two USB sockets, five LEDs, no mounting holes, Pin3=GPIO0,
                 Pin5=GPIO1, Pin13=GPIO21, I2C-0
0×4       B2     Model B, 256MB RAM, Ethernet, two USB sockets, five LEDs,
                 mounting holes, Pin3=GPIO1, Pin5=GPIO2, Pin13=GPIO27, I2C-1,
                 8 extra IO pads (P5)
0×5       B2     Model B, 256MB RAM, Ethernet, two USB sockets, five LEDs,
                 mounting holes, Pin3=GPIO1, Pin5=GPIO2, Pin13=GPIO27, I2C-1,
                 8 extra IO pads (P5)
0×6       B2     Model B, 256MB RAM, Ethernet, two USB sockets, five LEDs,
                 mounting holes, Pin3=GPIO1, Pin5=GPIO2, Pin13=GPIO27, I2C-1,
                 8 extra IO pads (P5)
0×7       A      Model A, 256MB RAM, no Ethernet, one USB socket, two LEDs,
                 mounting holes, Pin3=GPIO1, Pin5=GPIO2, Pin13=GPIO27, I2C-1,
                 8 extra IO pads (P5)
0×8       A      Model A, 256MB RAM, no Ethernet, one USB socket, two LEDs,
                 mounting holes, Pin3=GPIO1, Pin5=GPIO2, Pin13=GPIO27, I2C-1,
                 8 extra IO pads (P5)
0×9       A      Model A, 256MB RAM, no Ethernet, one USB socket, two LEDs,
                 mounting holes, Pin3=GPIO1, Pin5=GPIO2, Pin13=GPIO27, I2C-1,
                 8 extra IO pads (P5)
0xd       B2     Rev2 Model B, 512MB RAM, Ethernet, two USB sockets, five LEDs,
                 mounting holes, Pin3=GPIO1, Pin5=GPIO2, Pin13=GPIO27, I2C-1,
                 8 extra IO pads (P5)
0xe       B2     Rev2 Model B, 512MB RAM, Ethernet, two USB sockets, five LEDs,
                 mounting holes, Pin3=GPIO1, Pin5=GPIO2, Pin13=GPIO27, I2C-1,
                 8 extra IO pads (P5)
0xf       B2     Rev2 Model B, 512MB RAM, Ethernet, two USB sockets, five LEDs,
                 mounting holes, Pin3=GPIO1, Pin5=GPIO2, Pin13=GPIO27, I2C-1,
                 8 extra IO pads (P5)
