import win32com.client as win32
from datetime import datetime as dt
from os import chdir, path, getlogin
from pathlib import Path

"""
this script allows you to get all the file you have been receiving through email,
you can add more folder, subject and file_name to be added.
"""

userid = getlogin()
chdir(f'C:\\Users\\{userid}')

today =  dt.now().strftime('%m-%d-%y')

outlook = win32\
    .Dispatch('Outlook.Application')\
    .GetNameSpace('MAPI')
inbox = outlook.GetDefaultFolder(6)
messages = inbox.Items

email_file = [
    {
        'folder_name':'provide folder name to be create here',
        'subject':'provide subject here',
        'file_name':'provide file name here',
        'file_extension':'.xlsx'
    }
] #You can add information to exctrar more file with the current folder and information.

for file in email_file:
    try:
        folder = file['folder_name']
        subject = file['subject']
        file_name = file['file_name']
        file_extension = file['file_extension']
        output_dir = Path.cwd() / 'name the folder as you wish here example: reports from email' / folder
        output_dir.mkdir(parents=True, exist_ok=True)

        for message in messages:
            if str(message.Subject).startswith(f'{subject}'):
                email_date = message.senton.date().dt.strftime('%m-%d-%y')
                output_file = f'{file_name} - {email_date}{file_extension}'
                attachments = message.Attachments
                if path.isfile(output_dir / output_file):
                    print(f'{output_file} exists')
                    pass
                else:
                    for attachment in attachments:
                        if str(attachment).endswith(f'{file_extension}'):
                            attachment.SaveAsFile(output_dir / output_file)
                            print(f'{output_file} was created')
    except:
        pass