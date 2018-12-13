# ESGF-Ansible

### Introduction

The deployment of ESGF Nodes has traditionally been done by a mix of scripts and manual admin actions. This repository holds files which are used by the popular automated system configuration tool [Ansible](https://www.ansible.com/) that will perform the ESGF Node deployment.

For all the details and features of Ansible see:
- [Ansible Docs](https://docs.ansible.com/)
- [Ansible Best Practices](https://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html)
- [Ansible Modules](https://docs.ansible.com/ansible/latest/modules/modules_by_category.html)

### Basic Info

Ansible runs from a host, or 'control', machine and deploys the configuration to 'managed' machines. 

The simple requirements for the control machine is to have Ansible installed in some way. The required way for doing this right now is via a Conda environment and installing the ansible python package via pip. 

The simple requirement for the managed machine is that it can be accessed via ssh from the control machine and that it has a `python>=2.6` interpreter. Also, their must be some way to have escalated privileges on the the managed machine to deploy the configuration.

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

# Note this last host group line is required, do not edit this
[self]
localhost ansible_connection=local ansible_python_interpreter="{{ lookup('env', 'CONDA_PREFIX') }}/bin/python"
```

A test deployment to all managed test hosts, assuming proper configuration
```
ansible-playbook -i hosts.test all.yml
```

A production deployment to all managed production hosts, assuming proper configuration
```
ansible-playbook -i hosts.prod all.yml
```

A test deployment to managed test hosts that are to be data nodes, assuming proper configuration
```
ansible-playbook -i hosts.test data.yml
```