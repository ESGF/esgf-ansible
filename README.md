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

### Usage

#### Info
To deploy the specified configurations to your managed machines it is required to specify hosts in an 'inventory' file. It is often convenient to specify two of these inventory files, a 'production' and a 'staging' (or 'testing') file, if the resources for both are available. These can be populated with the respective fully qualified host names of your managed machines and then specified at the command line by using `-i <inventory file name>`. There is a sample inventory file at the base level of the repo, `sample.hosts`.

The second important file that will be unique for each sites deployment is a variable file. There is a sample variables file that contains all available options and info in the base level of the repo, `sample.vars.yml`.

#### Examples
Ansible assumes the use of keys for ssh authentication. It provides `--ask-pass` and `-u [user]` to ssh via password authentication. For escalated privileges, if sshing as a non-root user, `--ask-become-pass` is used.

A test deployment to all managed test hosts, with ssh via the root user and password authentication and a variable file named `myvars.test.yml`. Note the '@' is required.
```
ansible-playbook -i hosts.test --ask-pass -u root -e @myvars.test.yml install.yml
```

A test deployment to all managed test hosts, with ssh via a non-root user, *joe*, that has sudo privileges on the managed machine(s).
```
ansible-playbook -i hosts.test --ask-pass -u joe --ask-become-pass -e @myvars.test.yml install.yml
```

*The authentication method of choice will also be required below.*

A production deployment to all managed production hosts. Optionally just check to see what will happen.
```
ansible-playbook -i hosts.prod [ --check --diff ] -e @myvars.prod.yml install.yml
```

A useful command for a data-only deployment or a deployment only to your data node
```
ansible-playbook -i hosts.test -e @myvars.test.yml --tags data --limit host-data.my.org install.yml
```

If you have already done the `base` steps, the steps that are needed on every node type, and don't want to wait for them to be repeated
```
ansible-playbook -i hosts.test -e @myvars.test.yml --skip-tags base install.yml
```
or, to only do the `base` steps on your idp and index node
```
ansible-playbook -i hosts.test -e @myvars.test.yml --tags base --limit host-index-idp.my.org install.yml
```

The tags available in the `install.yml` play are: `base`, `idp`, `index`, and `data`. 
These can be used with `--tags` and `--skip-tags` as well as with the `--limit` flag to control exactly what is done and where.


Node services can be started or stopped using the control play and tags "start" or "stop"
```
ansible-playbook -i hosts.test --tags start control.yml 
ansible-playbook -i hosts.test --tags stop control.yml
```
To just start your data node, if it is a different host than your IDP and Index node.
```
ansible-playbook -i hosts.test --tags start --limit host-data.my.org control.yml
```

### Advice and Contributing

If your site would like to use advanced or more specific configuration files and options it is encouraged that you fork this repository. If there are features you believe would benefit all sites that you would like to contribute, create a pull request.