Verification
------------

.. warning::
    ESGF-Ansible is completely separate from the legacy 2.x ESGF-Installer. The tools provided by ESGF-Installer are, in general, incompatible with ESGF-Ansible and should not be used in cooperation with ESGF-Ansible. The FAQ page describes how to upgrade a node from the legacy installer using ESGF-Ansible, after which point the legacy tools should no longer be used.

Status
======

The status of a node, or multiple nodes, can be checked with the ``status.yml`` playbook. ::

    ansible-playbook -v -i hosts.test status.yml

This can be neatly combined with ``start.yml`` and ``stop.yml``. The following will restart a node, then check its status. ::

    ansible-playbook -v -i hosts.test stop.yml start.yml status.yml


If you are looking to get started using your node or have questions that are not answered within these docs be sure to `checkout the user support docs <https://esgf.github.io/esgf-user-support/>`_.

Logs
====

While ``status.yml`` will report on various ports and URLs that services are listening on, it is not a replacement for a human inspecting log files.
The following locations may be useful references for the services being ran on a node. 
This list is not comprehensive and potentially is subject to change.

httpd
*****
``/etc/httpd/logs/*``

Tomcat
******
``/usr/local/tomcat/logs/*``

Thredds
*******
``/esg/content/thredds/logs/*``, specifically ``threddsServlet.log``

MyProxy
*******
``/var/log/messages``

CoG
***
``/etc/cog-wsgi-8889/error_log``

SLCS
****
``/etc/slcs-wsgi-8888/error_log``

