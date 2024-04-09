import socket

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind(('0.0.0.0', 8821))
        (client_data, client_address) = server_socket.recvfrom(1024)
        client_data = client_data.decode() 
        server_socket.sendto(client_data.encode(), client_address)

if __name__ == "__main__":
    main()