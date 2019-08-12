Comparison of ESGF v2 vs v4
===========================

In the following table, if no context given, items in the table in the v2 column are the command line flag to the `esg-node` script.  Items in the v4 column are a playbook .yml file

+--------------------------+------------------------+------------------------------+
|  Action or Location      | ESGF v2 (Bash scripts) | ESGF v4 (Ansible)            |
+==========================+========================+==============================+
|   CoG location           | NA (mod_wsgi in httpd) | /etc/cog-wsgi-8889           |
+--------------------------+------------------------+------------------------------+
|   SLCS                   | NA (mod_wsgi in httpd) | /etc/slcs-wsgi-8888          |
+--------------------------+------------------------+------------------------------+
| Tomcat control           | esg-node function      | catalina.sh                  |
+--------------------------+------------------------+------------------------------+
| Solr index location      | /esg/solr-index        | /usr/local/solr-home         | 
+--------------------------+------------------------+------------------------------+
| Bootstrap                | - wget esg-bootstrap   | - (No bootstrap)             |
|                          | - ./esg-bootstrap      | - git clone esgf-ansible     |
+--------------------------+------------------------+------------------------------+
| Configuration            | esg-autoinstall.conf   | inventory file               |
| (auto-installation)      |                        | host variables files         |
+--------------------------+------------------------+------------------------------+
| Install latest           | --install (--upgrade)  | install.yml                  |   
| ESGF version             |                        |                              |
+--------------------------+------------------------+------------------------------+
| CSR                      | --generate-esgf-csrs   | local_certs.yml              |
+--------------------------+------------------------+------------------------------+
| Certs / CA               | --update-temp-ca       | local_certs.yml              |
+--------------------------+------------------------+------------------------------+
| Stop                     | --stop                 | stop.yml                     |
+--------------------------+------------------------+------------------------------+
| Start                    | --start                | start.yml                    |
+--------------------------+------------------------+------------------------------+
| Restart                  | --restart              | stop.yml + start.yml         |
+--------------------------+------------------------+------------------------------+
| Status                   | --status               | status.yml                   |     
+--------------------------+------------------------+------------------------------+
| Certificate Installation | - --install-local-certs| local_certs.yml              |
+--------------------------+------------------------+------------------------------+
|    (Web)                 | - --install-keypair    | web_certs.yml                |
+--------------------------+------------------------+------------------------------+
| LetsEncrypt request      | NA                     | install.yml (tryletsencript) |
+--------------------------+------------------------+------------------------------+
| Shard Replicas           | --add-replica-shard    | shards.yml                   |
+--------------------------+------------------------+------------------------------+