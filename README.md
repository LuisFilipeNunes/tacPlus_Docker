# TACACS+ Docker Image

This image is a built version of [tac_plus](http://www.pro-bono-publico.de/projects/),
a TACACS+ implementation written by Marc Huber.

Various configuration options and components were taken from an existing docker image repo which can be found here:
https://github.com/lfkeitel/docker-tacacs-plus

## Configuration
Configuration is stored in two files `tac_base.cfg` and `tac_user.cfg` for the majority of users neither of these need changing should simple, basic TACACS+ testing be required.

Various configuration defaults exist (defined in `tac_user.cfg`)  
**TACACS Key:** `parks`  
**Priv 15 User:** `adm` **password:** `parks`  
**Priv 0 User:** `gato` **password:** `cat`
**Show User:** `cachorro` **password:** `dog`  

The following configuration needs to be set in the OLT for the tests.
```
aaa accounting commands 15 default start-stop group tacacs+
aaa accounting exec default start-stop group tacacs+
aaa authorization exec default group tacacs+ local
aaa authentication login default group tacacs+ local

tacacs-server host <ip> key <key>
```

## Usage

### Building and Running the Docker Image

To build the Docker image, clone the repository and run the following commands:


```
git clone https://github.com/LuisFilipeNunes/tacPlus_Docker
cd tacPlus_Docker
docker build --no-cache -t tacplus .
```

By default all logs (including detailed information on authorization and authentication) are sent to stdout, meaning they're available to view via `docker logs` once the container is operational. This log contains all AAA information.

A log file is also generated with less verbosity (i.e. no debug information). This can be found at `/var/log/tac_plus.log` within the container. This can either be exported via a docker volume or read directly to console by cat or tailing the file via docker exec. E.g. `docker exec <containerid / name>  tail -f /var/log/tac_plus.log`

TACACS+ uses port 49. This is exposed by the container, but will require forwarding to the host if the default bridged networking is used using `-p 49:49`

Example - Running the default container for a quick test and inspecting the logs:
```
docker run -it --rm -p 49:49 tacplus .

```  
### Testing the server

The container should be working. To test it, you can use the tacacs_client.py for it. A.B.C.D  is your server ip. 

```
python3 tacacs_client.py -ip A.B.C.D 

```

You should receive the following confirmation:

```
Authentication successful for adm
Authentication successful for gato
Authentication successful for cachorro
Server is running and operational
```

This test confirms that the TACACS+ server is functioning as expected, successfully authenticating users and indicating operational status.
