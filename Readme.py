import requests

class YaUploader:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            "Content-Type": "application/json",
            "Authorization": f"OAuth {self.token}"
        }

    def get_upload_link(self, file_path):
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(url, headers=headers, params=params)
        print(response.json())
        return response.json()

    def upload(self, file_path, filename):
        href = self.get_upload_link(file_path=file_path).get("href", "")
        response = requests.put(href, data=open(filename, "rb"))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")


if __name__ == "__main__":
    path_to_file = ...
    token = ...
    uploader = YaUploader(token)
    uploader.upload(path_to_file, path_to_file)