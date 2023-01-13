import hvac

client = hvac.Client(
    url='http://VAULT_IP:8200/',
    token='TOKEN',
)

auth_response = client.is_authenticated()

read_response = client.secrets.kv.v1.read_secret(mount_point='demo_v1', path='server1')

username = read_response['data']['username']
password = read_response['data']['password']

print('Authenticated:', auth_response)
print('Username from vault:', username)
print('Secret from vault:', password)

