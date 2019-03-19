Releases
========

4.0.0-beta2
***********

Critical
--------
- ``gftphost*`` variables renamed to ``globushost*``
- Added variables ``generate_*`` which are required to be specified if the user would like esgf-ansible to generate required files (keys/certs) for the respective service
- Key, certificate, and other file paths specified in each ``host_vars/[hostname].yml`` file are now required to be on the **managed** machine, rather than the **control** machine
- Added requirements to more reliably manage keys/certifcates, users are now required to specify either the file paths as described in the previous bullet or the respective ``generate_*`` variable
- Added ``admin_pass`` variable and requirement for either the ``/esg/config/.esgf_pass`` file to be present on the Node or the ``admin_pass`` variable to be specified

Info
----
- A new tag ``--publisher`` has been added to the ``install.yml`` playbook to easily repeat the esg-publisher setup steps in the event of failure
- No longer managing SELinux state
- Not deploying monitoring software if neither of the ``prometheus_*`` variables are specified
- If setting up ``firewalld`` on CentOS 7, and it was not previously installed/enabled, a reboot will be required after installing/enabling

A number of reported bugs have been resolved and fragile setup steps were made more resilient.

4.0.0-beta1
***********

Critical
--------

Info
----