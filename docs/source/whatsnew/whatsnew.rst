Releases
========

This page contains infomation about what is added or changed with each new release.
The Critical section outlines any items the are highly likely to require changes from users.
The Info section outlines informative items that may be helpful for users to know, but likely do not require action.
All items described within a release are relative to the previous release.

4.0.6 (2020-04-07)
******************

Critical
--------
- Now installs the new filebeat log transmitter and the respective configuration

Info
- Does not remove old log collection software that is already installed
- The filebeat installation requires a signed certificate from an ESGF CA, see ``esgf-globus-ca.yml``

4.0.5 (2019-10-29)
******************

Critical
--------
- All Globus tools setup steps will be skipped if the user does not provide Globus account credentials

Info
----
- Added `developer documentation page  <../developers/developers.html>`_
- Added `compatability infomation page  <../faq/comptable.html>`_
- Tomcat updated to ``8.5.46``
- ESG-Search updated to ``v4.17.10``
- CoG update to ``v3.15.3``
- A number of updates within the ESGF-Publisher Conda environment
- Added playbook for node status tool ``install_ns.yml``
- Updated ACME Challenge (for LetsEncrypt certifcates) to v2
- Added ``roles/httpd/templates/robots.txt`` to direct web crawlers to not crawl ESGF data nodes


4.0.4 (2019-07-10)
******************

Critical
--------

Info
----
- With the release of the latest versions of Globus tools it is now required to deploy all Globus services, even if all are not going to be used.
- Hostnames that are used in config files can be better controlled by using the ``hostname`` variables in ``group_vars/all.yml``
- Solr ``6.6.6`` requires either a whitelist of shards or an explicit directive that no whitelist will be provided, the latter was chosen
- Cog updated to ``v3.14.3``
- ESGF-ORP updated to ``v2.11.0``
- ESGF-Security updated to ``v2.8.11``
- esgpublisher updated to ``v3.7.0``
- udunits2 updated to ``2.2.27``
- Small changes to the configuration of myproxy-server regarding the locations of certificates and keys


4.0.3 (2019-05-15)
******************

Critical
--------

Info
----
- A missing dependency for the Globus Transfer API was added to ensure Globus integration within CoG is operational.
- Tomcat webapps are now always cleaned out and re-installed
- Cog updated to ``v3.14.1``
- Tomcat updated, ``8.5.34`` -> ``8.5.39``
- Solr updated, ``6.6.5`` -> ``6.6.6``
- Java 8 set to be updated to latest version of OpenJDK 8. This is also a switch to using ``yum`` to install Java.


4.0.2 (2019-04-15)
******************

Critical
--------

Info
----
- Resolve missing GridFTP directory mount points at node startup


4.0.1 (2019-04-10)
******************

Critical
--------
- Previous releases of ESGF-Ansible created entries in ``/etc/fstab`` for the bind mounts required by GridFTP. These are now setup to be created when starting GridFTP and removed when stopping GridFTP. Their presence in ``/etc/fstab`` may or may not cause unexpected behavior and they should be safely removed.

Info
----
- New ``status.yml`` playbook, see the new `Verification Section <../verify/verify.html>`_.
- Default memory for Tomcat has been increased.


4.0.0-beta2 (2019-03-27)
************************

Critical
--------
- ``gftphost*`` variables renamed to ``globushost*``
- Added variables ``generate_*`` which are required to be specified if the user would like esgf-ansible to generate required files (keys/certs) for the respective service
- Key, certificate, and other file paths specified in each ``host_vars/[hostname].yml`` file are now required to be on the **managed** machine, rather than the **control** machine
- Added requirements to more reliably manage keys/certifcates, users are now required to specify either the file paths as described in the previous bullet or the respective ``generate_*`` variable
- Added ``admin_pass`` variable and requirement for either the ``/esg/config/.esgf_pass`` file to be present on the Node or the ``admin_pass`` variable to be specified

Info
----
- New sample files within the ``host_vars/`` directory to help with all the new changes above
- A new tag, ``publisher``, has been added to the ``install.yml`` playbook to easily repeat the esg-publisher setup steps in the event of failure
- No longer managing SELinux state
- If setting up ``firewalld`` on CentOS 7, and it was not previously installed and enabled, a reboot will be required after installing and enabling
- Not deploying monitoring software if neither of the ``prometheus_*`` variables are specified

A number of reported bugs have been resolved and fragile setup steps were made more resilient.

4.0.0-beta1 (2019-02-25)
************************

Critical
--------

Info
----