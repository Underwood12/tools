#!/usr/bin/env python3
# -*- coding: utf-8 -*- ########################################################
#               ____                     _ __                                  #
#    ___  __ __/ / /__ ___ ______ ______(_) /___ __                            #
#   / _ \/ // / / (_-</ -_) __/ // / __/ / __/ // /                            #
#  /_//_/\_,_/_/_/___/\__/\__/\_,_/_/ /_/\__/\_, /                             #
#                                           /___/ team                         #
#                                                                              #
# nullscan                                                                     #
# A modular framework designed to chain and automate security tests            #
#                                                                              #
# FILE                                                                         #
# domain.py                                                                    #
#                                                                              #
# AUTHOR                                                                       #
# noptrix@nullsecurity.net                                                     #
#                                                                              #
################################################################################


# sys imports


# own imports
from modules.libs.base import Base, tool, timeout


class Domain(Base):
  """ Domain (DNS) module (tcp/53)"""


  def __init__(self, target, opts):
    """ init """

    Base.__init__(self, target, opts)

    return


  @tool
  def host_dns_version(self):
    """
    DESCR: Determine remote DNS server version. (ext)
    TOOLS: host
    """

    self._host_dns_version('tcp')

    return


  @tool
  def dig_dns_version(self):
    """
    DESCR: Determine remote DNS server version. (ext)
    TOOLS: dig
    """

    self._dig_dns_version('tcp')

    return


  @tool
  def snoop_cache(self):
    """
    DESCR: Test for DNS cache snoop leak. (ext)
    TOOLS: dig
    """

    self._snoop_cache('tcp')

    return


  @tool
  def fpdns(self):
    """
    DESCR: Fingerprint the remote DNS server. (ext)
    TOOLS: fpdns
    """

    self._fpdns('tcp')

    return


  @tool
  def nmap_domain(self):
    """
    DESCR: Scan domain service with corresponding NSE scripts. (ext)
    TOOLS: nmap
    """

    opts = '-n -sS -Pn --open --nsock-engine epoll'
    opts += ' --script dns-cache-snoop,dns-random-srcport,dns-nsid,'
    opts += f"dns-random-txid -p {self.target['port']} {self.target['host']}"

    self._run_tool('nmap', opts, nullscan_tool='nmap_domain')

    return


# EOF
