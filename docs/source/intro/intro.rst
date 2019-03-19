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

Here is a summary of the requirements, see `Ansible Installation <https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html>`_ for more information.

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

To anyone new to ESGF and/or Web-based service deployments, running services in HTTPS is *a must*, and this requires SSL certificates recoginized by current browsers and other http(s) clients, eg. ``wget``, ``curl``, Python ``requests``.  If you haven't already, please check with your organization to see if you already purchase certificates from vendor.  If so, purchase one for your targeted ESGF Node server.  If not, free certificates can be obtained from ``LetsEncrypt``.  See the `Web Certificate Section <../usage/usage.html#web-certificate-installation>`_ within this site for more information.

Additional Info
---------------

The simple requirements for the control machine is to have Ansible installed in some way. 
This can be done via a system package manager, or simply via pip, the Python package manager into a Python environment. 
The later is the recommended way as this repository was developed and tested with the latest Ansible at the time, ``2.7``. 
It has been found that Ansible ``2.4`` is not supported. **Using anything other than Ansible 2.7 will result in untested behavior.**

The requirements for the managed machine are that it can be accessed via SSH from the control machine and that the managed machine has a Python interpreter. 
Also, an ESGF requirement is that the OS of the managed machine must be **CentOS 6 or 7**. Work is being done to support RedHat 6 and 7 as well. 
Ansible works reliably with Python 2 on the managed machine. Ansible is working towards supporting Python 3 on managed machines, see `Ansible's remarks <https://docs.ansible.com/ansible/latest/reference_appendices/python_3_support.html>`_, 
but is aware of incompatabilities. Since the system Python on CentOS/Redhat 6 and 7 is 2.6 and 2.7, respectively, this is not an issue.  
Also, there must be some way to have escalated privileges on the managed machine to deploy the configuration. This is described more below.
