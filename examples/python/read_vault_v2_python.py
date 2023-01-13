import hvac

client = hvac.Client(
    url='http://VAULT_IP:8200',
    token='TOKEN',
)

auth_response = client.is_authenticated()

read_response = client.secrets.kv.v2.read_secret_version(mount_point='demo_v2', path='server1')

username = read_response['data']['data']['username']
password = read_response['data']['data']['password']

print('Authenticated:', auth_response)
print('Username from vault:', username)
print('Secret from vault:', password)
