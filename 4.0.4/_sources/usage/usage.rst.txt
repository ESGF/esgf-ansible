Usage
=====
Quick Configuration
-------------------
There are two types of files a user is responsible for making, Inventory Files and Host Variable Files.

More comprehensive information and advice can be found in the `Config <../config/config.html>`_ section.

Inventory Files
***************
This file specifies the managed machines.
It is specified at the command line via ``-i [inventory file name]``.

See the sample inventory file, `sample.hosts <https://github.com/ESGF/esgf-ansible/blob/4.0.4/sample.hosts>`_ for more information.

Also, see `Ansible's Inventory Info <https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html>`_.

Host Variable Files
*******************
These files specify options for each managed machine.
It is automatically detected for each managed machine and must be named ``host_vars/[hostname].yml`` where ``[hostname]`` is the hostname of each managed machine.

See the sample host variable file, `host_vars/myhost.my.org.yml <https://github.com/ESGF/esgf-ansible/blob/4.0.4/host_vars/myhost.my.org.yml>`_ for more information.

Also, see the other sample files in `host_vars <https://github.com/ESGF/esgf-ansible/blob/4.0.4/host_vars>`_, and find the sample file
that best describes the desired use case.

Examples
--------
This section assumes the configuration information is understood and the required files have been created.

These examples are **not** presented in a "step by step" style. Within reason, the commands outlined below can be performed at any point in the lifetime of a node. 
That being said, the *information* presented in earlier examples is requisite for later examples.

These examples are **not** comprehensive, they only show some common patterns and useful commands. Refer to the Ansible documentation and the ``--help`` flag for more information.
The primary command line tool used is ``ansible-playbook`` ::

    ansible-playbook --help


Although not discussed in this guide, the ``ansible`` command line tool can be useful as well. ::

    ansible --help


It is recommended that users use the verbose flag ``-v[v...]``, where each additional ``v`` adds more output.

.. warning::
    The ``--check`` and ``--diff`` flags do not work as intended with our complicated use case and will result in an error. For this reason they should not be used.

SSH Authentication
******************
SSH authentication is not required for local deployments, where the control and managed machine are the same host. 
Ansible assumes the use of keys for SSH authentication. It provides ``--ask-pass`` and ``-u [user]`` to SSH via password authentication as an alternative user. 
For escalated privileges, if SSHing as a non-root user, ``--ask-become-pass`` is used to prompt for a sudo password. 
See `Ansible's examples <https://docs.ansible.com/ansible/latest/user_guide/intro_getting_started.html#your-first-commands>`_ as well.

A test deployment to all managed test hosts, with SSH via non-root user, *joe*, and key authentication. ::

    ansible-playbook -v -i hosts.test -u joe --ask-become-pass install.yml


A test deployment to all managed test hosts, with SSH via the root user and password authentication. ::

    ansible-playbook -v -i hosts.test --ask-pass -u root install.yml


A test deployment to all managed test hosts, with SSH via a non-root user, *joe*, that has sudo privileges on the managed machine(s). ::

    ansible-playbook -v -i hosts.test --ask-pass -u joe --ask-become-pass install.yml


**The authentication method of choice will also be required in all the examples below.**


Deployment Control
******************
These examples show various ways of controlling the deployment process. 
Deployments are done in the order of includes in `install.yml <https://github.com/ESGF/esgf-ansible/blob/4.0.4/install.yml>`_.
This order is base, idp, index then data. 
While repeating steps will not cause any problems, it simply slows things down. 
Additionally, for a more reliable deployment process it may be desired to do one phase at a time. 
Or if the deployment got interrupted after completing, for example, the `base` steps, these steps could be skipped when the deployment is started again.

Controlling the deployment is done with tags. The tags available in the `install.yml <https://github.com/ESGF/esgf-ansible/blob/4.0.4/install.yml>`_ play are ``base``, ``idp``, ``index``, ``data`` and ``publisher``.
These can be used with ``--tags`` and ``--skip-tags``,  as well as with ``--limit [hostname]`` to control exactly what is done and where.
The ``base`` steps will be done everytime unless specified via ``--skip-tags``.

A production deployment to all managed production hosts ::

    ansible-playbook -v -i hosts.prod install.yml


A useful command for a data-only deployment or a deployment only to your data node ::

    ansible-playbook -v -i hosts.test --tags data --limit host-data.my.org install.yml


If you have already done the `base` steps, the steps that are needed on every node type, and don't want to wait for them to be repeated ::

    ansible-playbook -v -i hosts.test --skip-tags base install.yml

or, to only do the `base` steps on your idp and index node ::

    ansible-playbook -v -i hosts.test --tags base --limit host-index-idp.my.org install.yml


Multiple tags can be specified at once, for example ::

    ... --tags "data, idp" --skip-tags "base, index" ...

Starting and Stopping Services
******************************
Node services can be started or stopped using the start.yml and stop.yml playbooks. 
In the examples below, start tags and stop tags are any combination of 
``[cog, slcs, myproxy, tomcat, solr, dashboard-ip, gridftp, httpd, postgres, monitoring, data, idp, index]``. 
These tags can also be used in any combination in ``--skip-tags``.

By default, if no start tags are specified, all services will be started. 
The services ``httpd``, ``postgres`` and ``monitoring`` will always be started, unless specified via ``--skip-tags``. 
If no stop tags are specified, all services, **except** ``httpd``, ``postgres`` and ``monitoring``, will be stopped. 
The services ``httpd``, ``postgres`` and ``monitoring`` will only be stopped if their respective tag is specified via ``--tags``. ::

    ansible-playbook -v -i hosts.test start.yml [ --tags [start tags] ]
    ansible-playbook -v -i hosts.test stop.yml [ --tags [stop tags] ]


Multiple playbooks may be specified and are executed in the order specified. For example, to restart ``cog``, ``slcs`` and ``myproxy`` ::

    ansible-playbook -v -i hosts.test stop.yml start.yml --tags "cog, slcs, myproxy"


To start or stop a data-only node use ``--limit [data node hostname]``. Only the common tags and those associated with data nodes will have an effect. ::

    ansible-playbook -v -i hosts.test --limit host-data.my.org start.yml [ --tags [start tags] ]
    ansible-playbook -v -i hosts.test --limit host-data.my.org stop.yml [ --tags [stop tags] ]

Local Certificate Installation
******************************
Globus certificates, aka 'local certs', for Globus services are retrieved as part of the post-install process. 
These certifcates allow the site to register their GridFTP and/or MyProxy servers with Globus. 
They also establish trust for these services within ESGF.  
If not specified in the host's variable file and ``generate_globus`` or ``generate_myproxyca`` are specfied,
the deployment will place a private key and a certificate signing request (CSR) for that service in the home directory of the root user on the node. 
The certifcates are obtained by emailing the CSR (do not email the private key) to the addresses in `esgf-globus-ca.yml <https://github.com/ESGF/esgf-ansible/blob/master/esgf-globus-ca.yml>`_. 
Once signed and retrieved from an ESGF certificate authority, these can be specified in the host's variable file and installed using the local_certs.yml playbook. ::

    ansible-playbook -v -i hosts.prod local_certs.yml

or, for data-only::

    ansible-playbook -v -i hosts.prod --limit host-data.my.org local_certs.yml


Web Certificate Installation
****************************
Certificates for web services may be installed independent from the primary installation process via the ``web_certs.yml`` playbook. 
See the sample host variable file to see how to specify what certifcate/key/cachain to install. 
This can be used to try to setup LetsEncrypt certificates as well. 
See the ``try_letsencrypt`` variable in the sample host variable file for more information. ::

    ansible-playbook -v -i hosts.prod web_certs.yml

Solr Shard Replication
**********************
A number of Solr shards are loaded as remote indices. 
For improved load times these can be replicated locally. 
shards.yml is provided to ease this process. ::

    ansible-playbook -v -i hosts.prod --extra-vars="remote_hostname=[remote host to replicate locally] local_port=[start at 8985 and increment]" --tags add shards.yml

If you would like to remove the replicated shard. ::

    ansible-playbook -v -i hosts.prod --extra-vars="remote_hostname=[remote host replicated locally] local_port=[port used by replicated shard]" --tags remove shards.yml