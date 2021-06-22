import os
from posixpath import relpath
import dropbox
from dropbox.files import WriteMode
class TransferData:
    def __init__(self, access_token):
        self.access_token=access_token
    def upload_files(self, file_from, file_to):
        dbx=dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):
            for filename in files:
                local_path=os.path.join(root, filename)
                relative_path=os.path.relpath(local_path, file_from)
                dropbox_path=os.path.join(file_to, relative_path)
                with open(local_path, 'rb') as f:
                    dbx.file_upload(f.read(), dropbox_path, mode=WriteMode('overWrite'))
def main():
    access_token='sl.AzL7zBq61KyBGlGzMARp6hYnSscyecGRqA89d96qXvjz_ZhEvxW17rnvn2HwlOv6u35-UVXj3J722ffA00SjRmwN45YkhMV47GCrcN8pCz0EPxjeCnPHZA6SDG70GiFoS2pxIVg'
    transferData=TransferData(access_token)
    file_from=str(input("Enter the folder Path to transfer :-"))
    file_to=input("enter the full path to upload to dropbox :-")
    transferData.upload_files(file_from, file_to)
    print("File has been moved")
main()