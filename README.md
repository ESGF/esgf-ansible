# ESGF-Ansible

### Introduction

The deployment of ESGF Nodes has traditionally been done by a mix of scripts and manual admin actions. This repository holds files which are used by the popular automated system configuration tool [Ansible](https://www.ansible.com/) that will perform the ESGF Node deployment.

### Basic Info

Ansible runs from a host, or 'control', machine and deploys the configuration to 'managed' machines. 

The simple requirements for the control machine is to have Ansible installed in some way. This can be done via a system package manager, or simply via pip, the Python package manager into a Python environment.

The simple requirement for the managed machine is that it can be accessed via ssh from the control machine and that it has a `python>=2.6` interpreter. Also, their must be some way to have escalated privileges on the the managed machine to deploy the configuration.

For all the details and features of Ansible see:
- [Ansible Docs](https://docs.ansible.com/)
- [Ansible Best Practices](https://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html)
- [Ansible Modules](https://docs.ansible.com/ansible/latest/modules/modules_by_category.html)

### Development and Usage

To deploy the specified configurations to your managed machines it is required to specify hosts in an 'inventory' file. It is often convenient to specify two of these inventory files, a 'production' and a 'staging' (or 'testing') file. These can be populated with the respective fully qualified host names of your managed machines and then specified at the command line as desired on the control machine.

A sample testing inventory file, named hosts.test, would look like this
```
[data]
test-data.my.org

[index]
test-indexidp.my.org

[idp]
test-indexidp.my.org
```

Ansible assumes the use of keys for ssh authentication. It provides `--ask-pass` and `-u [user]` to ssh via password authentication. For escalated privileges, if sshing as a non-root user, `--ask-become-pass` is used.

A test deployment to all managed test hosts, with ssh via the root user and password authentication.
```
ansible-playbook -i hosts.test all.yml --ask-pass -u root --tags install
```

A test deployment to all managed test hosts, with ssh via a non-root user, *joe*, that has sudo privileges on the managed machine(s).
```
ansible-playbook -i hosts.test all.yml --ask-pass -u joe --ask-become-pass --tags install
```

The authentication method of choice will also be required below.

A production deployment to all managed production hosts. Optionally just check to see what will happen.
```
ansible-playbook -i hosts.prod all.yml [ --check --diff ] --tags install
```

A test deployment to your data node
```
ansible-playbook -i hosts.test all.yml --tags "install,data" --limit test-data.my.org
```

Node services can be started or stopped using tags "start" or "stop"
```
ansible-playbook -i hosts.test all.yml --tags start
ansible-playbook -i hosts.test all.yml --tags stop
```