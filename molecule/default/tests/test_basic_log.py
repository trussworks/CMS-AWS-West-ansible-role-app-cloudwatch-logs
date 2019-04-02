def test_app_log(host):
    config_file = host.file("/etc/awslogs/config/test-app.conf")
    assert config_file.exists
    assert (config_file.mode == 0o644)
    assert (config_file.user == 'root')
    assert (config_file.group == 'root')
    assert config_file.contains("file = /var/log/test_app.log")
    assert config_file.contains(
            "log_group_name = /aws/ec2/var/log/test_app.log")
