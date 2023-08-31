# tacPlus_Docker
Docker Image based em Ubuntu Bionic.

## Command to build this image

```
git clone https://github.com/LuisFilipeNunes/tacPlus_Docker
cd tacPlus_Docker
docker build --no-cache -t tacplus .
```

## Command to run the container mapping external TACACS+  config file.

```
 docker run -td --name tacplus -p 49:49 -e DEBUGLEVEL=64 \
      -v $(pwd)/tac_plus.conf:/etc/tacacs+/tac_plus.conf \
      tacplus
```
the above command uses $(pwd) to copy the current directory to the command. If your .conf file is located elsewhere, you need to provide the correct path in the command.
