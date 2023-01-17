FROM vault:latest
# copy CA file to /tmp directory of container
COPY config/vault-server-ca.crt /tmp
# add CA to CA file of container
RUN cat /tmp/vault-server-ca.crt >> /etc/ssl/certs/ca-certificates.crt
