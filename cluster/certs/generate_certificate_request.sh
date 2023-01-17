openssl req -newkey rsa:3072 -keyout key.pem -out cert.csr -nodes -subj "/C=NL/ST=CITY/O=ORG/OU=UNIT/CN=FQDN"
  cat <<EOF > server_cert.conf
basicConstraints = CA:FALSE
subjectKeyIdentifier = hash
authorityKeyIdentifier = keyid,issuer:always
keyUsage = critical, digitalSignature, keyEncipherment
extendedKeyUsage = serverAuth, clientAuth
subjectAltName = @alt_names
[alt_names]
DNS.1 = HOSTNAME_1
DNS.2 = HOSTNAME_2
DNS.3 = HOSTNAME_3
IP.1 = IP_1
IP.2 = IP_2
EOF
