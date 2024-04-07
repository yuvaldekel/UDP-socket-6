import socket

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
        what_to_send = ''
        while what_to_send == '':
            what_to_send = input("what would you like to send to the server: ")
        my_socket.sendto(what_to_send.encode(), ("127.0.0.1", 8821))
        data, remote_address = my_socket.recvfrom(1024)
        print("The server '{}' sent: {}".format(remote_address[0], data.decode()))

if __name__ == "__main__":
    main()