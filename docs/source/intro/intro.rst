Introduction
============

    The deployment of ESGF Nodes has traditionally been done by a mix of scripts and manual admin actions.
    ESGF Nodes have been managed this way for many years and each machine is truly in its own unique state.
    The developers of this tool have taken much into consideration to ensure that it performs as reliably as possible with the information and resources available to us.
    We rely on users to provide feedback and help us understand their cases so that we can continue to improve this tool.
    
    Thank you for your participation.

This tool is a collection of files which are used by the popular automated system configuration tool `Ansible <https://www.ansible.com/>`_ that will perform the ESGF Node deployment.
Ansible runs from a *control* machine and deploys the configuration to *managed* machines via SSH.

For all the details and features of Ansible see the `Ansible Docs <https://docs.ansible.com/>`_.

If you have upgraded to a new version of ESGF-Ansible be sure to `check out what's new <../whatsnew/whatsnew.html>`_.

.. warning::
    ESGF-Ansible is completely seperate from the legacy 2.x ESGF-Installer. The tools provided by ESGF-Installer are, in general, incompatible with ESGF-Ansible and should not be used in cooperation with ESGF-Ansible. The FAQ page describes how to upgrade a node from the legacy installer using ESGF-Ansible, after which point the legacy tools should no longer be used.
