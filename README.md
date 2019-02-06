<img src="https://esgf.llnl.gov/media/images/logos/esgf.png" alt="ESGF Logo"/>

# ESGF-Ansible
## Table of Contents
- **[Introduction](#introduction)**
- **[Basic Info](#basic-info)**
- **[Usage](#usage)**
  - **[Info](#info)**
    - **[Inventory Files](#inventory-files)**
    - **[Host Variables Files](#host-variables-files)**
    - **[Playbooks](#playbooks)**
  - **[Examples](#examples)**
    - **[SSH Authentication](#ssh-authentication)**
    - **[Deployment Control](#deployment-control)**
    - **[Starting and Stopping Services](#starting-and-stopping-services)**
    - **[Local Certs](#local-certs)**
    - **[Web Certs](#web-certs)**
    - **[Solr Shards](#solr-shards)**
- **[FAQ](#faq)**
- **[Advice and Contributing](#advice-and-contributing)**

## Introduction

The deployment of ESGF Nodes has traditionally been done by a mix of scripts and manual admin actions. This repository holds files which are used by the popular automated system configuration tool [Ansible](https://www.ansible.com/) that will perform the ESGF Node deployment.

## Basic Info

Ansible runs from a 'control' machine and deploys the configuration to 'managed' machines.

The simple requirements for the control machine is to have Ansible installed in some way. This can be done via a system package manager, or simply via pip, the Python package manager into a Python environment. The later is the recommended way as this repository was developed and tested with the latest Ansible at the time, `2.7`. It has been found that Ansible `2.4` is not supported. __Using anything other than `ansible==2.7` will result in untested behavior.__

The simple requirement for the managed machine is that it can be accessed via SSH from the control machine and that the managed machine has a Python interpreter. Ansible works reliably with Python 2 on the managed machine. Ansible is working towards supporting Python 3 on managed machines, see [their info](https://docs.ansible.com/ansible/latest/reference_appendices/python_3_support.html), but is aware of incompatabilities. Since the system Python on CentOS/Redhat 6 and 7 is 2.6 and 2.7, respectively, this is not an issue.  Also, there must be some way to have escalated privileges on the managed machine to deploy the configuration. This is described more below.

For all the details and features of Ansible see:
- [Ansible Docs](https://docs.ansible.com/)
- [Ansible Best Practices](https://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html)
- [Ansible Modules](https://docs.ansible.com/ansible/latest/modules/modules_by_category.html)

## Usage

### Info
#### Inventory Files
To deploy the specified configurations to your managed machines it is required to specify hosts in an 'inventory' file. It is often convenient to have several of these inventory files, for example, 'production' and 'staging' (or 'testing') inventory files could be populated with their respective hosts and then specified at the command line as described in the examples below. The inventory files must be populated with the fully qualified domain names of your managed machines and then specified at the command line by using `-i [inventory file name]`. See the sample inventory file with more info at the base level of the repo, [sample.hosts](sample.hosts).

#### Host Variables Files
The second important file(s) that will be unique for each site's deployment are host variable files. See the sample host variable file that contains all available options and info, [host_vars/myhost.my.org.yml](host_vars/myhost.my.org.yml). Note the format of the file name of any host variable file must be `host_vars/[hostname].yml`, where `[hostname]` matches with that specified in the inventory file. It is required to specify one for each host your site will be deploying to. Ansible will automatically find them and assign them to the respective hosts. More advanced users may like to review or revise variables within [group_vars](group_vars) to make their own modifications, see [Advice and Contributing](#advice-and-contributing).

#### Playbooks
Ansible uses 'playbooks' to define what actions to take on the managed machine(s). The primary playbook used is [install.yml](install.yml) for performing deployments. Other utility-like playbooks are outlined below as well.

### Examples

This section assumes the information in [Info](#info) is understood and the proper files have been created.

These examples are __not__ presented in a "step by step" style. Within reason, the commands outlined below can be performed at any point in the lifetime of a node. That being said, the *information* presented in earlier examples is requisite for later examples.

These examples are __not__ comprehensive, they only show some common patterns and useful commands. Refer to the docs linked above and the `--help` flag for more information.
The primary command line tool used is `ansible-playbook`.
```
ansible-playbook --help
```

Although not discussed in this guide, the `ansible` command line tool can be useful as well.
```
ansible --help
```

It is recommended that users use the verbose flag `-v[v...]`, where each additional `v` adds more output.

#### SSH Authentication
SSH authentication is not required for local deployments, where the control and managed machine are the same host. Ansible assumes the use of keys for SSH authentication. It provides `--ask-pass` and `-u [user]` to SSH via password authentication. For escalated privileges, if SSHing as a non-root user, `--ask-become-pass` is used to prompt for a sudo password. See [Ansible's examples](https://docs.ansible.com/ansible/latest/user_guide/intro_getting_started.html#your-first-commands) as well.

A test deployment to all managed test hosts, with SSH via the root user and password authentication.
```
ansible-playbook -v -i hosts.test --ask-pass -u root install.yml
```

A test deployment to all managed test hosts, with SSH via a non-root user, *joe*, that has sudo privileges on the managed machine(s).
```
ansible-playbook -v -i hosts.test --ask-pass -u joe --ask-become-pass install.yml
```

__*The authentication method of choice will also be required below.*__

#### Deployment Control
These examples show various ways of controlling the deployment process. Deployments are done in the order of includes in [install.yml](install.yml). This order is base, idp, index then data. While repeating steps will not cause any problems, it simply slows things down. Additionally, for a more reliable deployment process it may be desired to do one phase at a time. Or if the deployment got interrupted after completing, for example, the `base` steps, these steps could be skipped when the deployment is started again.

Controlling the deployment is done with tags. The tags available in the [install.yml](install.yml) play are `base`, `idp`, `index`, and `data`.
These can be used with `--tags` and `--skip-tags`,  as well as with `--limit [hostname]` to control exactly what is done and where.
The `base` steps will be done everytime unless specified via `--skip-tags`.

A production deployment to all managed production hosts.
```
ansible-playbook -v -i hosts.prod install.yml
```

A useful command for a data-only deployment or a deployment only to your data node
```
ansible-playbook -v -i hosts.test --tags data --limit host-data.my.org install.yml
```

If you have already done the `base` steps, the steps that are needed on every node type, and don't want to wait for them to be repeated
```
ansible-playbook -v -i hosts.test --skip-tags base install.yml
```
or, to only do the `base` steps on your idp and index node
```
ansible-playbook -v -i hosts.test --tags base --limit host-index-idp.my.org install.yml
```

Multiple tags can be specified at once, for example 
```
... --tags "data, idp" --skip-tags "base, index" ...
```

#### Starting and Stopping Services
Node services can be started or stopped using the [start.yml](start.yml) and [stop.yml](stop.yml) playbooks. In the examples below, start tags and stop tags are any combination of `[cog, slcs, myproxy, tomcat, solr, dashboard-ip, gridftp, httpd, postgres, monitoring, data, idp, index]`. These tags can also be used in any combination in `--skip-tags`.

By default, if no start tags are specified, all services will be started. The services `httpd`, `postgres` and `monitoring` will always be started, unless specified via `--skip-tags`. If no stop tags are specfied, all services, **except** `httpd`, `postgres` and `monitoring`, will be stopped. The services `httpd`, `postgres` and `monitoring` will only be stopped if their respective tag is specified via `--tags`.
```
ansible-playbook -v -i hosts.test start.yml [ --tags "start tags" ]
ansible-playbook -v -i hosts.test stop.yml [ --tags "stop tags" ]
```

Multiple playbooks may be specfified and are executed in the order specified. For example, to restart `cog`, `slcs` and `myproxy`:
```
ansible-playbook -v -i hosts.test stop.yml start.yml --tags "cog, slcs, myproxy"
```

To start or stop a data-only node use `--limit [data node hostname]`. Only the common tags and those associated with data nodes will have an effect.
```
ansible-playbook -v -i hosts.test --limit host-data.my.org start.yml [ --tags "start tags" ]
ansible-playbook -v -i hosts.test --limit host-data.my.org stop.yml [ --tags "stop tags" ]
```

#### Local Certs
Globus certificates and keys, aka 'local certs', for globus services are retrieved as part of the post-install process. If not specified in the host's variable file, the deployment will place a private key and CSR for these services in the HOME directory of the root user on the node. Once signed and retrieved from an ESGF certificate authority, these can be specified in the host's variable file and installed using the [local_certs.yml](local_certs.yml) playbook.
```
ansible-playbook -v -i hosts.prod local_certs.yml
```
or, for data-only
```
ansible-playbook -v -i hosts.prod --limit host-data.my.org local_certs.yml
```

#### Web Certs
Certificates for web services may be installed independent from the primary installation process via the [web_certs.yml](web_certs.yml) playbook. See the sample host variable file to see how to specify what certifcate/key/cachain to install. This can be used to try to setup LetsEncrypt certificates as well. See the `try_letsencrypt` variable in the sample host variable file for more information.
```
ansible-playbook -v -i hosts.prod web_certs.yml
```

#### Solr Shards
A number of Solr shards are loaded as remote indices. For improved load times these can be replicated locally. [shards.yml](shards.yml) is provided to ease this process.
```
ansible-playbook -v -i hosts.prod --extra-vars="remote_hostname=[remote host to replicate locally] local_port=[start at 8985 and increment]" --tags add shards.yml
```

If you would like to remove the replicated shard.
```
ansible-playbook -v -i hosts.prod --extra-vars="remote_hostname=[remote host replicated locally] local_port=[port used by replicated shard]" --tags remove shards.yml
```

## FAQ
__Q: How can I use this to upgrade my older node?__

__Answer:__ Make sure you stop all services on your older node using the legacy tools for doing so. If there are valid certificates and keys in place on the machine that you would like to continue to use, put those in a place on your control machine and specify that path in your host variable file. Once you have filled your variable file(s) and your inventory file as described above, the same example commands above for doing clean installs can be used to perform the upgrade. While many considerations have been made for upgrades and the preservation of customizations, it is still recommended that users create backups of site-specific changes to their node.

__Q: Ansible is stuck on a task for a long period of time and doesn't seem to be doing anything.__

__Answer:__ Ansible will not report the result of a task until the task is completed. Some tasks can take several minutes to complete. Make sure the verbose flag is specified, `-v`, to get more information upon the completion of tasks.

__Q: My deployment failed, what should I do?__

__Answer:__ Try to determine if the failure was related to a bug in the steps taken by the installer or if it was some intermitten, or site-specific, issue. This second case could be things such as bad SSH authentication, a temporary network issue, an issue with the machine being deployed to, or a variable improperly specified in the host variables file. In this second case, attempt to determine and resolve the error, then start the deployment again. If it is confidently determined be the first case, please [submit an issue](https://github.com/ESGF/esgf-ansible/issues/new) to this repository.

## Advice and Contributing

If your site would like to use more specific configuration files and options, or make large site-specific additions, it is encouraged that you fork this repository. If there are features you believe would benefit all sites that you would like to contribute, create a pull request.