import ytmusicapi
class authenticate:
    def __init__(self):
        pass
    def get_json(self):
        with open("headers.txt", "r") as file:
            headers = file.read()

        ytmusicapi.setup(filepath="browser.json", headers_raw=headers)
