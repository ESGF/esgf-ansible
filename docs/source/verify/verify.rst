Verification
------------

Status
======

The status of a node, or multiple nodes, can be checked with the `status.yml` playbook. :

    ansible-playbook -v -i hosts.test status.yml

This can be neatly combined with `start.yml` and `stop.yml`. The following will restart a node, then check its status :

    ansible-playbook -v -i hosts.test stop.yml start.yml status.yml

Logs
====

While `status.yml` will report on various ports and URLs that services are listening on, it is not a replacement for a human inspecting log files.
The following locations may be useful references for the services being ran on a node.

httpd:
``/etc/httpd/logs/*``

tomcat:
``/usr/local/tomcat/logs/*``

Thredds:
``/esg/content/thredds/logs/*``, specifically ``threddsServlet.log``

MyProxy:
``/var/log/messages``

CoG:
``/etc/cog-wsgi-8889/error_log``

SLCS:
``/etc/slcs-wsgi-8889/error_log``

