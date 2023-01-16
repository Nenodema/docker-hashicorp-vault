openssl x509 -days 3600 -req -in cert.csr -CA vault-server-ca.pem -CAkey  vault-server-ca-key.pem -CAcreateserial -out cert.pem -sha256 -extfile server_cert.conf
