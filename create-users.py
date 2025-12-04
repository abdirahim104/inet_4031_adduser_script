#!/usr/bin/python3

# INET4031
# Abdirahim Abdullahi
# 11/28/25
# 12/3/25

# os  → used to execute system commands (adduser, passwd, group operations)
# re  → used for pattern matching to detect commented lines (those beginning with #)
# sys → used to read input passed via STDIN (the input file redirected into the program)
import os
import re
import sys

def main():
    # Process each line coming from STDIN (redirected input file)
    for line in sys.stdin:

        # Detect whether the line begins with '#' meaning it is a comment and should be skipped
        match = re.match("^#", line)

        # Split the non-comment line into fields separated by colons
        fields = line.strip().split(':')

        # Skip this line if:
        # 1. It is a comment (match == True), OR
        # 2. It does not contain exactly 5 fields.
        #
        # This ensures only valid user lines are processed. Invalid or incomplete lines
        # could cause errors if processed, so the script safely ignores them.
        if match or len(fields) != 5:
            continue

        # Extract username, password, and GECOS field components.
        # The GECOS field stores user information in /etc/passwd:
        # Format → FirstName LastName,,,
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])

        # Split the group list into individual group names.
        # If the field is "-", it means "no groups to add".
        groups = fields[4].split(',')

        # Inform the user that an account is about to be created
        print("==> Creating account for %s..." % (username))

        # Build the Linux command to create a new user with:
        # - disabled password (initially)
        # - GECOS field populated
        # This prepares the user entry before setting the actual password.
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)
        #os.system(cmd)

        # Inform the user that a password is being set for the account
        print("==> Setting the password for %s..." % (username))

        # Build the Linux command that:
        # - Echoes the password twice (as required by passwd)
        # - Pipes it into the passwd command to set the password
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)
        #os.system(cmd)

        # Assign the user to groups listed in the last field
        for group in groups:

            # If the group field is "-", it means "no groups to assign"
            # Otherwise, the user is added to each valid group with adduser <user> <group>
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                #os.system(cmd)

if __name__ == '__main__':
    main()
