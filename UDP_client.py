import socket

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
        my_socket.sendto('Hello'.encode(), ("127.0.0.1", 8821))
        data, remote_address = my_socket.recvfrom(1024)
        print("The server '{}' sent: {}".format(remote_address, data.decode()))

if __name__ == "__main__":
    main()