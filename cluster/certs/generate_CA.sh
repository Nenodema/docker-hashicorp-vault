openssl req -newkey rsa:3072 -keyout vault-server-ca-key.pem -out vault-server-ca.pem -days 3650 -nodes -x509 -subj "/C=NL/ST=CITY/O=ORG/OU=UNIT/CN=Vault Server CA"
