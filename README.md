# HashiCorp Vault on Docker in production mode (standalone mode)

For the cluster mode readme click [here](https://github.com/cisolutions-nl/docker-hashicorp-vault#hashicorp-vault-on-docker-in-production-mode-cluster-mode).

### Requirements:

* Virtual machine
* Docker
* Docker-Compose
* (sudo) rights
* Certificates

### Instructions:

1) Clone the project
```
git clone https://github.com/Nenodema/docker-hashicorp-vault.git
```
2) Enter the project directory and start the container with docker-compose
```
cd docker-hashicorp-vault/standalone
(sudo) docker-compose up -d
```
4) Enter container and initilize vault (save the unseal keys on a secure location)
```
(sudo) docker exec -it vault_vault-server_1 /bin/sh
vault operator init
```
![image](https://user-images.githubusercontent.com/33698556/212346090-229f6778-811a-46ee-8cf0-1688685cf548.png)

7) Go to http://vault_ip:8200/ and unseal the vault with 3 of the 5 keys

8) Login with the "Initial Root Token" which is provided after the vault initionalization

9) Have fun and stay safe

### File structure:

```
`-- docker-hashicorp-vault
    |-- standalone
        |-- config
        |   `-- vault.json
        |-- data
        |-- docker-compose.yml
        |-- logs
        |-- polices
        `-- README.m
```
### Noteworthy links:

* https://www.bogotobogo.com/DevOps/Docker/Docker-Vault-Consul.php
* https://developer.hashicorp.com/vault/docs/concepts/seal


------------------------------------------------------------------------------------------------------------


# HashiCorp Vault on Docker in production mode (cluster mode)

### Requirements:

* Virtual machine (minimum of three)
* Docker
* Docker-Compose
* (sudo) rights
* Certificates

### Instructions:

1) Clone the project
```
git clone https://github.com/Nenodema/docker-hashicorp-vault.git
```
2) Change variables in the following files:
* .env
* config/vault.json
* certs/generate_CA.sh
* certs/generate_cert.sh
* generate_cert_req.sh
3) Generate CA
```
./certs/generate_CA.sh
```
4) Generarte Certificate request per machine
```
./certs/generate_cert.sh
```
5) Generarte Certificate per machine
```
./certs/generate_cert_req.sh
```
6) Copy the "cert.pem" and the "key.pm" to the config directory
```
copy cert.pem key.pem ../config
```
7) Enter the project directory and start the container with docker-compose
```
verify that you are in the following directory: docker-hashicorp-vault/cluster
(sudo) docker-compose up -d --build
```
8) Enter container and initilize vault (save the unseal keys on a secure location)
```
(sudo) docker exec -it vault_vault-server_1 /bin/sh
vault operator init
```
![image](https://user-images.githubusercontent.com/33698556/212346090-229f6778-811a-46ee-8cf0-1688685cf548.png)

9) Go to http://vault_ip:8200/ and unseal the vault with 3 of the 5 keys

10) Login with the "Initial Root Token" which is provided after the vault initionalization

11) Execute steps 1-10 for the other two nodes

12) Join the new two nodes to the first node
```
(sudo) docker exec -it vault_vault-server_1 /bin/sh
vault operator raft join "https://$PRIMARY_NODE:8200"
vault operator unseal (3 times)
```
13) check the status of the cluster
```
vault login (use the "Initial Root Token" which is provided after the vault initionalization
vault operator raft list-peers
Node Address State Voter
 — — — — — — — — — — — — — — — — — — — — — — — — -
vault_node_1 10.99.99.10:8201 leader true
vault_node_2 10.99.99.11:8201 follower true
vault_node_3 10.99.99.12:8201 follower true
```
14) Have fun and stay safe

### File structure:

```
`-- docker-hashicorp-vault
    |-- cluster
        |-- certs
        |   `-- generate_CA.sh
        |   `-- generate_cert.sh
        |   `-- generate_cert_req.sh
        |-- config
        |   `-- vault.json
        |-- data
        |-- docker-compose.yml
        |-- logs
        |-- polices
        `-- .env
        `-- README.m

```
### Noteworthy links:

* https://fongyang.medium.com/hashicorp-vault-on-docker-for-secrets-management-f579867dd1ca
* https://www.velotio.com/engineering-blog/how-to-setup-hashicorp-vault-ha-cluster-with-integrated-storage-raft
