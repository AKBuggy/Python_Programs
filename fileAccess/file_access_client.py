import xmlrpc.client

proxy = xmlrpc.client.ServerProxy('http://localhost:8000/')

# Example usage
content = proxy.read_file('example.txt')
print("Content of example.txt:", content)

result = proxy.write_file('new_file.txt', 'Hello, world!')
print("Write operation result:", result)

result = proxy.delete_file('new_file.txt')
print("Delete operation result:", result)
