# inet_4031_adduser_script

Automated user and group creation script for Ubuntu Linux.  
This repository was created for INET 4031 – Lab 8 Part 2 (Automating User Management).

## Description

`create-users.py` reads user data from `create-users.input` and:

- Creates user accounts on the system
- Creates primary groups for each user
- Adds users to additional groups (such as group01 and group02)
- Skips commented or invalid lines in the input file

The script was written to demonstrate how system administrators can automate user management tasks using Python.

## Input File Format

The `create-users.input` file contains one user per line, with colon-delimited fields:

```text
username:password:last_name:first_name:group_list
