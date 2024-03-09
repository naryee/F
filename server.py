import socket
import pickle
import json
import xml.etree.ElementTree as ET

# Create a socket object, create a socket object using socket.socket(). This will be the endpoint that clients can connect to.
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server configuration, define Host and Port that the server will listen on
SERVER_IP = '127.0.0.1' #local host
SERVER_PORT = 12345

# Bind the socket to the address and port
server_socket.bind((SERVER_IP, SERVER_PORT))

# Listen for incoming connections, allow up to 5 queued connections
server_socket.listen(5)

print(f"Server is listening on {SERVER_IP}:{SERVER_PORT}")

while True:
    # Accept a new connection
    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")

    # Receive data from the client
    data = client_socket.recv(1024)

    # Deserialize and process the received data based on format
    try:
        # Deserialize binary data (pickle)
        deserialized_dict_binary = pickle.loads(data)
        print("Deserialized Dictionary (Binary):", deserialized_dict_binary)

        # Deserialize JSON data
        deserialized_dict_json = json.loads(data.decode('utf-8'))
        print("Deserialized Dictionary (JSON):", deserialized_dict_json)

        # Deserialize XML data
        root = ET.fromstring(data)
        deserialized_dict_xml = {elem.tag: elem.text for elem in root}
        print("Deserialized Dictionary (XML):", deserialized_dict_xml)

        # Handle encrypted text data (decryption logic here)
        decrypted_text_data = "Decrypted text data"  # Placeholder for decryption logic

        # Configurable option to print contents to screen or file
        print("Decrypted Text Data:", decrypted_text_data)  # Example of printing decrypted text

    except Exception as e:
        print("Error processing data:", e)

    # Close the client connection
    client_socket.close()
