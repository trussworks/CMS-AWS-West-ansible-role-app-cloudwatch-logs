CMS-AWS-West-ansible-role-app-cloudwatch-logs
=========

A role for adding application specific configs for AWS Cloudwatch Logs.


Requirements
------------

This role requires the ansible-role-aws-cloudwatch-logs-agent to set up the
initial Cloudwatch Logs agent config.

Role Variables
--------------

This role has a number of variables; the most important ones that are not
assigned by default are app.name and app.logs, which need to be defined in order
for the role to actually function (you need to tell it what logs to create).
Three other variables have defaults defined in defaults/main.yml:

- stream_name: This is the name for the log stream in AWS Cloudwatch Logs.
  Defaults to the EC2 instance id.
- group_prefix: This is a prefix prepended to the file path to generate the
  AWS Cloudwatch Logs log group. Defaults to "/aws/ec2".
- awslogs_daemon: The name of the awslogs service. Defaults to awslogsd (the
  name on Amazon Linux 2).

Dependencies
------------

- ansible-role-aws-cloudwatch-logs-agent, for setting up the main AWS Cloudwatch
  Logs daemon

Example Playbook
----------------

Here is a sample call of this role in a playbook:

```ansible
- role: CMS-AWS-West-ansible-role-app-cloudwatch-logs
  vars:
    app:
      name: test-app
      logs:
        - file: /var/log/test_app.log
```
