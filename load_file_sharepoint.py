from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.user_credential import UserCredential

"""
Using this method you can upload any file to sharepoint without linking you onedrive just provide the require information
"""

class upload_file_sharepoint:
    def __init__(self, user, password, url, folder, target_folder, file_to_upload) -> None:
        self.sharepoint_user = user
        self.sharepoint_password = password
        self.sharepoint_site = url
        conn = ClientContext(self.sharepoint_site).with_credentials(UserCredential(f'{self.sharepoint_user}',f'{self.sharepoint_password}'))
        self.folder = folder
        self.target_folder = target_folder
        self.root_folder = conn.web.get_folder_by_server_relative_url(self.target_folder)
        self.file_name = file_to_upload
        with open(self.file_name, 'rb') as file:
            self.file_contents = file.read()
            self.root_folder.upload_file(self.file_name, self.file_contents).execute_query()
            pass
