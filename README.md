
# ESGF-Ansible
## CoG + Python3 

This branch has several specific modifications to support the deployment of an updated version of CoG based on Python3 + Django2.  The `master` version of CoG remains Python2 for legacy deployment for now.  For nodes that have already installed the CoG database (under Python2), you may use this branch as a means to upgrade upgrade.  If you want to install this CoG on a fresh system, you'll need to explore manually upgrading your PostgreSQL server to >94 first before the cog_db is setup due to a Django2 incompatiblity.

### How to use this branch:

 * add `-b python3_cog` to clone esgf-ansible with this as your default branch before running the playbooks or checkout this branch: `python3_cog`

## Documentation

Please refer to [our documentation site](https://esgf.github.io/esgf-ansible/) for details on requirements, setup and usage of this tool. 

If you are using a new version of ESGF-Ansible be sure to [check out what's new](https://esgf.github.io/esgf-ansible/whatsnew/whatsnew.html).

The site also hosts documentation for each release of the tool, `beta` and later. For `alpha` releases refer to the `README.md` included with those.

## Support

Please [open an issue](https://github.com/ESGF/esgf-ansible/issues/new/choose) for support.

## Advice and Contributing

If your site would like to use more specific configuration files and options, or make large site-specific additions, it is encouraged that you fork this repository.  

If there are features you believe would benefit all sites that you would like to contribute, please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits, and [open a pull request](https://github.com/ESGF/esgf-ansible/compare).

ESGF-Ansible follows [Ansible Best Practices](https://docs.ansible.com/ansible/latest/user_guide/playbooks_best_practices.html). Most control can be done from the variables within `group_vars/*` and by altering files, or templates, for a given role. 

<img src="https://esgf.llnl.gov/media/images/logos/esgf.png" alt="ESGF Logo"/>
