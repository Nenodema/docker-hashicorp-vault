FROM vault:latest
COPY config/vault-server-ca.crt /tmp
RUN cat /tmp/vault-server-ca.crt >> /etc/ssl/certs/ca-certificates.crt

