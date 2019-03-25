Releases
========

This page contains infomation of what is added or changed with each new release.
All items described in a release are relative to the previous release.
The Critical section outlines any items the are highly likely to require changes from users.
The Info section outlines informative items that may be helpful for users to know, but likely do not require action.


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
- A new tag, ``publisher``, has been added to the ``install.yml`` playbook to easily repeat the esg-publisher setup steps in the event of failure
- No longer managing SELinux state
- New sample files within the ``host_vars/`` directory
- If setting up ``firewalld`` on CentOS 7, and it was not previously installed and enabled, a reboot will be required after installing and enabling
- Not deploying monitoring software if neither of the ``prometheus_*`` variables are specified

A number of reported bugs have been resolved and fragile setup steps were made more resilient.

4.0.0-beta1
***********

Critical
--------

Info
----