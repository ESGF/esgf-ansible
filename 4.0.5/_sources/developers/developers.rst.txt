Developers Guide
================

Adding WSGI services to an ESGF node
------------------------------------

It's easy to add new services developed with Flask, Django, etc. and proxy using the esgf-httpd configuration and mod_wsgi express.

This guide assumes you have set up a project using flask at the example location ``/opt/esgf/flaskdemo/demo`` and you have the application entry point accessible in the ``/opt/esgf/flaskdemo/demo.wsgi``.  Your demo app must world-readable and recommended to be owned by the ``apache`` user and group.  These instructions assume to be run by a root user, as many server configs disallow a shell run under the apache user, but a regular user can be used to run the service for testing purposes.  

- Create and activate a conda environment to run your webapp. 

.. code:: console

    source /usr/local/conda/bin/activate
    conda create -n flaskdemo
    conda activate flaskdemo

.. note:: 
    if your app was developed in Python 2.7 you'll need to create the environment with the following instead:

.. code:: console

    conda create -n flaskdemo 'python<3.0'

- Install modules needed to run your app.  Our demo uses flask, but you could use django (and expect additional required packages.)  Note that diffculty has been encountered with mod_wsgi version 4.6.7, so we recommend an earlier version:

.. code:: console

   pip install flask 'mod_wsgi<4.6'

- Run the `mod_wsgi-express` command to create a httpd service instance for your webapp and start the instance. 

.. code:: console

    cd /opt/esgf/flaskdemo/demo
    mod_wsgi-express setup-server --server-root /etc/wsgi-demo --user apache --group apache --host localhost --port 8087 --mount-point /demo demo.wsgi
    /etc/wsgi-demo/apachectl start

- You should be able to access the demo now under ``http://localhost:8087/demo`` using ``curl`` or ``wget``. 

- For external access on 443 for https, add the following directives to `/etc/httpd/conf/httpd.ssl.conf`: 

.. code:: console

    ProxyPass /demo http://localhost:8087/demo
    ProxyPassReverse /demo http://localhost:8087/demo

- Restart httpd

- If you want the site available also on 80 for old insecure http, you can add the same directives to ``/etc/httpd/conf/esgf-httpd.conf``.  In addition you need to add a rule to exempt ``/demo`` from the automatic redirection of http traffic to https as done for several of the ESGF Tomcat webapps that are proxied in that section.


