Setup
=====

These steps describe how to setup the control machine. SSH access to the managed machine(s) is the responsibility of the user.

1. Clone the esgf-ansible repo at the current version, for example version 4.0.3 ::

    git clone --branch 4.0.3 https://github.com/ESGF/esgf-ansible.git && cd esgf-ansible

2. (Optional, but strongly recommended) Create a Python environment, using a tool like ``virtualenv`` or ``conda``, and activate the environment.

3. Install ``ansible``. ::

    pip install ansible==2.7.5

4. Check the ``ansible`` version is as installed above. ::

    ansible --version


.. warning::
    ESGF-Ansible is completely separate from the legacy 2.x ESGF-Installer. The tools provided by ESGF-Installer are, in general, incompatible with ESGF-Ansible and should not be used in cooperation with ESGF-Ansible. The FAQ page describes how to upgrade a node from the legacy installer using ESGF-Ansible, after which point the legacy tools should no longer be used.
