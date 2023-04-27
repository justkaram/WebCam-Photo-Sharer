from filestack import Client


class FileShare:

    def __init__(self, file_path, api_key='AqiHXdRzhT0aW9n3FOeVDz'):
        self.file_path = file_path
        self.api_key = api_key

    def get_link(self):
        client = Client(apikey=self.api_key)
        link = client.upload(filepath=self.file_path)
        return link.url
