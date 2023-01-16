import hvac
import os

VAULT_HOST = os.environ.get('VAULT_HOST', 'http://localhost:8200/')
VAULT_TOKEN = os.environ.get('VAULT_TOKEN')

if __name__ == '__main__':
    client = hvac.Client(url=VAULT_HOST, token=VAULT_TOKEN)
    if not client.is_authenticated():
        raise PermissionError('Authentication token incorrect.')

    response = client.secrets.kv.v1.read_secret(
        mount_point='demo_secrets_engine_v1',
        path='server1',
    )
    print(response)
    try:
        username = response['data']['username']
        password = response['data']['password']
    except KeyError:
        raise KeyError('Make sure you created the secrets "username" and "password" in your vault.')

    print('Read credentials successfully:')
    print(f'- Username found: {username}')
    print(f'- Password found: {password}')