Configuration
=============

There are two types of files a user is responsible for making, Inventory Files and Host Variable Files.

Inventory Files
---------------

This file serves a simple, yet critical, role in the deployment process.
Its role is to specify the managed machines.
Managed machines are placed in logical groups that allow for enhanced deployment control. 
The groups used by ESGF are ``data``, ``idp`` and ``index``.
At least one host must be specified within each group.
The inventory file to use is easily changed when a deployment is performed, so feel free to create as many as you would like, to accommodate various deployment circumstances.
There are a few factors that will affect how this file looks. These factors may vary from site to site.

Remote vs Local Deployment
**************************

One of the first choices to make is the choice of a control machine. 
As mentioned in the Setup portion of this guide, this is where Ansible will be installed and the deployment will be ran from.
This is a step away from the legacy installation strategy, where installation tools were required to be installed and run on the machine itself.
The recommended choice is to do a remote deployment.
Perform the Setup steps on any host that is **not** any one of your site's ESGF Nodes.
It is often most convenient to use your usual work station machine that has SSH access to your site's ESGF Nodes.
A local deployment means that the Setup steps are performed on a machine that is to be an ESGF Node.

Node Type
*********

Regardless of Node type (data-only, index/idp, all, etc.) all three groups, ``data``, ``idp`` and ``index``, must have a host assigned to them.
In the case of data-only this means another site's index/idp host(s) must be assigned to their respective group.


See the sample inventory file, `sample.hosts <https://github.com/ESGF/esgf-ansible/blob/4.0.0-beta2/sample.hosts>`_ for more information regarding inventory files.

Host Variable Files
-------------------

The host variable file provides an interface that allows users to configure common options for their deployments.
Options regarding certificates and keys for various services require the most attention as certain requirements have been placed on these variables.
See the host variables directory, `host_vars <https://github.com/ESGF/esgf-ansible/blob/4.0.0-beta2/host_vars>`_, and find the sample file
that best describes the desired use case.
Also see the sample host variable file, `host_vars/myhost.my.org.yml <https://github.com/ESGF/esgf-ansible/blob/4.0.0-beta2/host_vars/myhost.my.org.yml>`_ for a comprehensive overview.
Advanced users may want to make configuration choices beyond what is provided in the host variable file
, see the `Contributing Guide <https://github.com/ESGF/esgf-ansible#advice-and-contributing>`_ for more information on this.