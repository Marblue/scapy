## This file is part of Scapy
## Copyright (C) 2007, 2008, 2009 Arnaud Ebalard
##                     2015, 2016 Maxence Tury
## This program is published under a GPLv2 license

"""
Aggregate some TLS crypto objects.
"""

# XXX This line should be removed once standard FFDH groups have been
# registered in the cryptography library.
from scapy.layers.tls.crypto.ffdh import *

from scapy.layers.tls.crypto.suites import *

