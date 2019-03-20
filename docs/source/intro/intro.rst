Introduction
============
The deployment of ESGF Nodes has traditionally been done by a mix of scripts and manual admin actions. 
This repository holds files which are used by the popular automated system configuration tool `Ansible <https://www.ansible.com/>`_ that will perform the ESGF Node deployment.

Ansible runs from a *control* machine and deploys the configuration to *managed* machines via SSH.

For all the details and features of Ansible see the `Ansible Docs <https://docs.ansible.com/>`_.

.. warning::
    ESGF-Ansible is completely seperate from the legacy 2.x ESGF-Installer. The tools provided by ESGF-Installer are, in general, incompatable with ESGF-Ansible and should not be used in cooperation with ESGF-Ansible. The FAQ page describes how to upgrade a node from the legacy installer using ESGF-Ansible, after which point the legacy tools should no longer be used.

Requirements
============

Here is a summary of the requirements,
see `Ansible Installation <https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html>`_ for more information.

+---------+-------------------------+-----------------------------------+
|         | Control Machine         | Managed Machine                   |
+=========+=========================+===================================+
| OS      | Any, Not Windows        | CentOS 6/7                        |
+---------+-------------------------+-----------------------------------+
| Python  | >=2.7                   | 2 (CentOS 6/7 has 2.6/7)          |
+---------+-------------------------+-----------------------------------+
| Ansible | 2.7                     | None                              |
+---------+-------------------------+-----------------------------------+
| Other   | SSH to Managed Machine  | Account with escalated privileges |
+---------+-------------------------+-----------------------------------+


SSL Certificates
----------------

To anyone new to ESGF and/or Web-based service deployments, running services in HTTPS is *a must*, 
and this requires SSL certificates recoginized by current browsers and other http(s) clients, eg. ``wget``, ``curl``, Python ``requests``.  
If you haven't already, please check with your organization to see if you already purchase certificates from vendor.  
If so, purchase one for your targeted ESGF Node server.  If not, free certificates can be obtained from ``LetsEncrypt``.  
See the `Web Certificate Section <../usage/usage.html#web-certificate-installation>`_ within this site for more information.


Firewall
--------

By default the firewall for a machine will not be configured.
Users may set the following, applicable, variable and ESGF-Ansible will take steps to configure the firewall::

    configure_centos6_iptables: true
    # or
    configure_centos7_firewalld: true

The required open ports for each node type are as follows, for the default configuration

+---------+----------------------------+
| Type    | Ports                      |
+=========+============================+
| Data    | 80, 443, 50000:51000, 2811 |
+---------+----------------------------+
| IDP     | 80, 443, 7512              |
+---------+----------------------------+
| Index   | 80, 443                    |
+---------+----------------------------+