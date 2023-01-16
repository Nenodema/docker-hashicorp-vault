import hvac
import os

VAULT_HOST = os.environ.get('VAULT_HOST', 'http://localhost:8200/')
VAULT_TOKEN = os.environ.get('VAULT_TOKEN')

if __name__ == '__main__':
    client = hvac.Client(url=VAULT_HOST, token=VAULT_TOKEN)
    if not client.is_authenticated():
        raise PermissionError('Authentication token incorrect.')

    list_secrets_result = client.secrets.kv.v1.list_secrets(
        mount_point='demo_secrets_engine_v1',
        path='server1',
    )

    print('The following keys found under the selected path ("/v1/secret/hvac"): {keys}'.format(
        keys=','.join(list_secrets_result['data']['keys']),
    ))
