from netmiko import ConnectHandler


def collect_data(ip, port, username, password):
    data = {}

    # Connect to the switch
    device = {
        'device_type': 'cisco_ios',
        'host': ip,
        'port': port,
        'username': username,
        'password': password,
    }
    connection = ConnectHandler(**device)

    data['version'] = connection.send_command('show version')
    data['startup_config'] = connection.send_command('show startup-config')
    data['current_config'] = connection.send_command('show running-config')
    data['acls'] = connection.send_command('show access-lists')
    data['interfaces'] = connection.send_command('show interfaces')
    connection.disconnect()
    return data


if __name__ == '__main__':
    collect_data(ip="localhost",
                 port=8800,
                 username="user1",
                 password="pass")
