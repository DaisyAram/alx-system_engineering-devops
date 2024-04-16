# 0x14. MySQL
> primary-replica cluster
> setting up primary replica setup
> building a  robust database backup strategy

## General Requirements
* Allowed editors: vi, vim, emacs
* All your files will be interpreted on Ubuntu 16.04 LTS
* All your files should end with a new line
* A README.md file, at the root of the folder of the project, is mandatory
* All your Bash script files must be executable
* Your Bash script must pass Shellcheck (version 0.3.7-5~ubuntu16.04.1 via apt-get) without any error
* The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
* The second line of all your Bash scripts should be a comment explaining what is the script doing

### Tasks
0. Install MySQL
> installing MySQL on both web-01 and web-02 servers.

1. Let us in!
>  creating a user and password for both MySQL databases

2. If only you could see what I've seen with your eyes
> create a database with at least one table and one raw in the primary MySQL(web-01) to replicate from

3. Quite an experience to live in fear, isn't it?
> create a new user for the replica server

4. Setup a Primary-Replica infrastructure using MySQL
> MySQL primary must be hosted on web-01
> MySQL replica must be hosted on web-02
> Setup replication for the MySQL database named tyrell_corp
> Provide your MySQL primary configuration as answer file(my.cnf or mysqld.cnf) with the name 4-mysql_configuration_primary
> Provide your MySQL replica configuration as an answer file with the name 4-mysql_configuration_replica

5. MySQL backup
> Bash script that generates a MySQL dump and creates a compressed archive out of it.
