import argparse
from tacacs_plus.client import TACACSClient

def tacacs_request(server_ip, server_port, secret_key, username, password):
    try:
        client = TACACSClient(server_ip, server_port, secret_key)
        auth_result = client.authenticate(username, password)
        
        if auth_result and auth_result.status == 1:
            print(f"Authentication successful for {username}")
            return True
        else:
            print(f"Authentication failed for {username}")
            return False
    
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description='TACACS Client')
    parser.add_argument('-ip', '--server-ip', help='TACACS server IP address', required=True)
    args = parser.parse_args()

    server_ip = args.server_ip
    server_port = 49 
    secret_key = "parks"
    
    # List of username-password pairs to test
    credentials_list = [
        ("adm", "parks"),
        ("gato", "cat"),
        ("cachorro", "dog")
    ]

    success_count = 0
    for username, password in credentials_list:
        if tacacs_request(server_ip, server_port, secret_key, username, password):
            success_count += 1

    if success_count == len(credentials_list):
        print("Server is running and operational")
    else:
        print("Not all authentication attempts were successful.")

if __name__ == "__main__":
    main()
