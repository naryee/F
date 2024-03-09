import socket
import pickle
import json
import xml.etree.ElementTree as ET

#Create a socket object for the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server details
SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345

# Connect to the server
client_socket.connect((SERVER_IP, SERVER_PORT))

# Create a dictionary and serialize it using different formats
data_dict = {'key1': 'value1', 'key2': 'value2'}

# Serialize dictionary using pickle (binary format)
serialized_dict_binary = pickle.dumps(data_dict)

# Serialize dictionary using JSON format
serialized_dict_json = json.dumps(data_dict).encode('utf-8')

# Serialize dictionary using XML format
root = ET.Element('data')
for key, value in data_dict.items():
    ET.SubElement(root, key).text = value
serialized_dict_xml = ET.tostring(root)

# Create a text file and encrypt it (example encryption function)
text_data = "This is a sample text file."
encrypted_text_data = text_data.encode('utf-8')  # Placeholder for encryption logic

# Send serialized dictionary in binary format to the server
client_socket.send(serialized_dict_binary)

# Send serialized dictionary in JSON format to the server
client_socket.send(serialized_dict_json)

# Send serialized dictionary in XML format to the server
client_socket.send(serialized_dict_xml)

# Send encrypted text file to the server
client_socket.send(encrypted_text_data)

# Receive response from the server
response = client_socket.recv(1024)
print("Response from server:", response.decode('utf-8'))

# Close the connection
client_socket.close()
