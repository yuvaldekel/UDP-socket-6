import socket
import datetime

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
        what_to_send = ''
        while what_to_send == '':
            what_to_send = input("what would you like to send to the server: ")
        start = datetime.datetime.now()
        my_socket.sendto(what_to_send.encode(), ("127.0.0.1", 8821))
        data, remote_address = my_socket.recvfrom(1024)
        end = datetime.datetime.now()
        time_took = end - start
        print("The server '{}' sent: {} took {} microseconds".format(remote_address[0], data.decode(), time_took.microseconds))

if __name__ == "__main__":
    main()