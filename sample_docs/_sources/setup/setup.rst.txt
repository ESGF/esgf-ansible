Setup
=====

These steps describe how to setup the control machine. SSH access to the managed machine(s) is the responsibility of the user.

1. Clone the esgf-ansible repo at the current version, for example version 4.0.0 ::

    git clone --branch v4.0.0 https://github.com/ESGF/esgf-ansible.git && cd esgf-ansible

2. (Optional, but recommended) Create a Python environment, using a tool like ``virtualenv`` or ``conda``, and activate the environment.

3. Install ``ansible``. ::

    pip install ansible==2.7.5

4. Check the ``ansible`` version is as installed above.::

    ansible --version
