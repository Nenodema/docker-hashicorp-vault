# How to run the python examples

### Prerequisite
Make sure you have a Hashicorp Vault instance running on an accessible host.

### Steps to run the code

1. Create a virtual environment and install `requirements.txt`

```bash
python3 -m venv venv
source venv/bin/activate
pip install -f requirements.txt
```

2. Export environment
```bash
export VAULT_HOST=http://localhost:8200/  # The host of the vault;
export VAULT_TOKEN=abc123  # The access key to the vault
```

3. Run a script 
```bash
python read_from_kv_engine_v1.py
```

### Scripts
| file name                 | description                                          |
|---------------------------|------------------------------------------|
| create_kv_credentials.py  | Creates a secret into the secrets vault. |
| read_from_kv_engine_v1.py | Reads a secret (v1) from the vault       |
| read_from_kv_engine_v2.py | Reads a secret (v2) from the vault       |
