Requirements
============

System
------

Here is a summary of the system requirements,
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
and this requires SSL certificates recognized by current browsers and other http(s) clients, eg. ``wget``, ``curl``, Python ``requests``.  
If you haven't already, please check with your organization to see if you have already purchased certificates from a vendor.  
If not, purchase one for your targeted ESGF Node server. Free certificates can be obtained from ``LetsEncrypt``.  
See the `Web Certificate Section <../usage/usage.html#web-certificate-installation>`_ within this site for more information.


Firewall
--------

By default the firewall for a machine will **not** be configured.
Users may set the following, applicable, variable and ESGF-Ansible will take steps to configure the firewall::

    configure_centos6_iptables: true
    # or
    configure_centos7_firewalld: true

See the `Host Variables Configuration Section <../config/config.html#host-variable-files>`_ for links to info about these variables.

The required open ports for each node type are as follows, for the default configuration:

+---------+----------------------------+
| Type    | Ports                      |
+=========+============================+
| Data    | 80, 443, 50000:51000, 2811 |
+---------+----------------------------+
| IDP     | 80, 443, 7512              |
+---------+----------------------------+
| Index   | 80, 443                    |
+---------+----------------------------+