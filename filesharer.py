class FileSharer():

    def __init__(self, file_path, api_key='AM6VC2tlMQ8G9cYDgOrX4z'):
        self.api_key = api_key
        self.file_path = file_path

    def share(self):
        client = Client(self.api_key)

        new_filelink = client.upload(filepath=self.file_path)

        return new_filelink.url