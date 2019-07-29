## Comparison of ESGF v2 vs v4

In the following table, if no context given, items in the table in the v2 column are the command line flag to the `esg-node` script.  Items in the v4 column are a playbook .yml file

+------------------------+------------------------+--------------------+
|  Action / Location     | ESGF v2 (Bash scripts) | ESGV v4 (Ansible)  |
+========================+========================+====================+
|   CoG                  | NA mod_wsgi   |  /etc/cog
+------------------------+---------------+----------+
|   SLCS                 |
+---
| Tomcat control         | esg-node function | catalina.sh

| Solr index location    | /esg/solr-index | /usr/local/solr-home | 

+ 
| Bootstrap           | wget esg-bootstrap       |  No bootstrap
|                       ./esg-bootstrap          |  git clone esgf-ansible 
  Configuration       | esg-autoinstall.conf     |  inventory file
  (autoinstallation)                                host variables files

| Install latest      |  --install (--upgrade)   | install.yml
| ESGF version
+
| CSR 
| Stop

| Start

| Restart

| Status

| Certificate installation | 

LetsEncrypt request        | NA                | install.yml (tryletsencript) |
