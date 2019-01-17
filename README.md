# ESGF-Ansible

## Introduction

The deployment of ESGF Nodes has traditionally been done by a mix of scripts and manual admin actions. This repository holds files which are used by the popular automated system configuration tool [Ansible](https://www.ansible.com/) that will perform the ESGF Node deployment.

## Basic Info

Ansible runs from a host, or 'control', machine and deploys the configuration to 'managed' machines. 

The simple requirements for the control machine is to have Ansible installed in some way. This can be done via a system package manager, or simply via pip, the Python package manager into a Python environment. The later is the recommended way as this repository was developed and tested with the latest Ansible at the time, `2.7`. It has been found that Ansible `2.4` is not supported. Using anything other than `ansible==2.7` will result in untested behavior.

The simple requirement for the managed machine is that it can be accessed via ssh from the control machine and that it has a `python>=2.6` interpreter. Also, their must be some way to have escalated privileges on the the managed machine to deploy the configuration.

For all the details and features of Ansible see:
- [Ansible Docs](https://docs.ansible.com/)
- [Ansible Best Practices](https://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html)
- [Ansible Modules](https://docs.ansible.com/ansible/latest/modules/modules_by_category.html)

## Usage

### Info
To deploy the specified configurations to your managed machines it is required to specify hosts in an 'inventory' file. It is often convenient to specify two of these inventory files, a 'production' and a 'staging' (or 'testing') file, if the resources for both are available. These can be populated with the respective fully qualified host names of your managed machines and then specified at the command line by using `-i <inventory file name>`. There is a sample inventory file at the base level of the repo, `sample.hosts`.

The second important file(s) that will be unique for each site's deployment are host variable files. There is a sample variables file that contains all available options and info at `host_vars/myhost.my.org.yml`. Note the format of any host variable file must be `[hostname].yml`, to match with that in the inventory file. It is required to specify one for each host your site will be deploying to. Ansible will automatically them and assign them to the respective hosts.

### Examples

#### SSH Authentication
Ansible assumes the use of keys for ssh authentication. It provides `--ask-pass` and `-u [user]` to ssh via password authentication. For escalated privileges, if sshing as a non-root user, `--ask-become-pass` is used.

A test deployment to all managed test hosts, with ssh via the root user and password authentication.
```
ansible-playbook -i hosts.test --ask-pass -u root install.yml
```

A test deployment to all managed test hosts, with ssh via a non-root user, *joe*, that has sudo privileges on the managed machine(s).
```
ansible-playbook -i hosts.test --ask-pass -u joe --ask-become-pass install.yml
```

*The authentication method of choice will also be required below.*

#### Deployment Control
A production deployment to all managed production hosts. Optionally just check to see what will happen.
```
ansible-playbook -i hosts.prod [ --check --diff ] install.yml
```

A useful command for a data-only deployment or a deployment only to your data node
```
ansible-playbook -i hosts.test --tags data --limit host-data.my.org install.yml
```

If you have already done the `base` steps, the steps that are needed on every node type, and don't want to wait for them to be repeated
```
ansible-playbook -i hosts.test --skip-tags base install.yml
```
or, to only do the `base` steps on your idp and index node
```
ansible-playbook -i hosts.test --tags base --limit host-index-idp.my.org install.yml
```

Multiple tags can be specified at once, for example 
```
... --tags "data,idp" --skip-tags "base,index" ...
```

The tags available in the `install.yml` play are: `base`, `idp`, `index`, and `data`.
These can be used with `--tags` and `--skip-tags` as well as with `--limit [hostname]` to control exactly what is done and where.

#### Starting and Stopping
Node services can be started or stopped using the control play and tags "start" or "stop"
```
ansible-playbook -i hosts.test --tags start control.yml 
ansible-playbook -i hosts.test --tags stop control.yml
```
To just start your data node, if it is a different host than your IDP and Index node.
```
ansible-playbook -i hosts.test --tags start --limit host-data.my.org control.yml
```

#### Local Certs
Globus certificates and keys, aka 'local certs', for globus services are retrieved as part of the post-install process. If not provided, the deployment will place a private key and CSR for these services in the HOME directory on the node. Once signed and retrieved from an ESGF certificate authority, these can be specified in the variables file and installed using the `local_certs.yml` playbook.
```
ansible-playbook -i hosts.prod local_certs.yml
```
or, for data-only
```
ansible-playbook -i hosts.prod --limit host-data.my.org local_certs.yml
```

## Advice and Contributing

If your site would like to use more specific configuration files and options, or make large site-specific additions, it is encouraged that you fork this repository. If there are features you believe would benefit all sites that you would like to contribute, create a pull request.