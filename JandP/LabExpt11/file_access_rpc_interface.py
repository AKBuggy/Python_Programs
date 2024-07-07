from xmlrpc.server import SimpleXMLRPCServer
from LabExpt11.file_access_client import FileAccessRPCInterface


class FileAccessServer(FileAccessRPCInterface):
    def read_file(self, filename):
        with open(filename, 'r') as file:
            return file.read()

    def write_file(self, filename, content):
        with open(filename, 'w') as file:
            file.write(content)
        return True

    def delete_file(self, filename):
        import os
        if os.path.exists(filename):
            os.remove(filename)
            return True
        else:
            return False


server = SimpleXMLRPCServer(('localhost', 8000))
server.register_instance(FileAccessServer())
server.serve_forever()
