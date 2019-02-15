FAQ
====

**Q: How can I use this to upgrade my older node?**

**Answer:** Make sure you stop all services on your older node using the legacy tools for doing so. 
If there are valid certificates and keys in place on the machine that you would like to continue to use, 
put those in a place on your control machine and specify that path in your host variable file. 
Once you have filled your variable file(s) and your inventory file, 
the same example commands above for doing clean installs can be used to perform the upgrade. 
While many considerations have been made for upgrades and the preservation of customizations, 
it is still recommended that users create backups of site-specific changes to their node.

**Q: Ansible is stuck on a task for a long period of time and doesn't seem to be doing anything.**

**Answer:** Ansible will not report the result of a task until the task is completed. 
Some tasks can take several minutes to complete. Make sure the verbose flag is specified, ``-v``, to get more information upon the completion of tasks.

**Q: My deployment failed, what should I do?**

**Answer:** Try to determine if the failure was related to a bug in the steps taken by the installer or if it was some intermitten, or site-specific, issue. 
This second case could be things such as bad SSH authentication, a temporary network issue, an issue with the machine being deployed to, 
or a variable improperly specified in the host variables file. 
In this second case, attempt to determine and resolve the error, then start the deployment again. 
If it is confidently determined be the first case, please `submit an issue <https://github.com/ESGF/esgf-ansible/issues/new>`_ to this repository.