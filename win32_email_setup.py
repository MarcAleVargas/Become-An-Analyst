import win32com.client as win32
from os import *

"""
this script will help you to send email/reply and add more than 2 files-dashboards created with pandas-matplotlib
you have to make sure to append the name of each file and dashoard to the list declare below
then set the email as needed.
"""

class setting_email():
    def __init__(self) -> None:
         self.userid = getlogin() #get compute user 
         pass
    
    def send_email(self):

        self.file_create = [] #list of file name to attach
        self.dashboard_create = [] # list of dashboard to add in the email body
        self.outlook = win32.Dispatch('Outlook.Application') #open outlook
        self.mapi = self.outlook.GetNameSpace('MAPI') #get message api
        self.email = self.outlook.CreateItem(0) #create the object/email
        self.email.bodyformat = 1 #give the desire format in this case we are using 1
        for self.visual in self.dashboard_create: #by using this loop you will add to outlook the visual needed
            self.chart = self.email.Attachments.Add(f"C:\\Users\\{self.userid}\\{self.visual}") #location of the visual with the given name
            self.chart.PropertyAccessor.SetProperty("http://schemas.microsoft.com/mapi/proptag/0x3712001F", f"{self.visual}") #location of the visual inside outlook
        self.visual_add = [f"<img src ='cid:{self.dashboard}'/>" for self.dashboard in self.dashboard_create] #generate a list formatted with htlm
        self.visual_add = str(self.visual_add).replace("[","").replace("]","").replace('"',"").replace(",","") #remove unnecesary symbols
        self.email.To = ''
        self.email.Cc = ''
        self.email.Bcc = ''
        self.email.Subject = ''
        self.email.htmlBody = f"""
        write your html here:
        <p>{self.visual_add}</p>
        """ #paste your html structure with the message you want to send
        for self.files in self.file_create: #by using this loop you will attach every files are inside the list.
            chdir(f'C:\\Users\\{self.userid}') #remember to keep this line of code or the code will breake change directory method is being used set this where your files are.
            self.email.Attachments.Add(path.join(getcwd(), f'{self.files}')) #adding the files
        #self.email.Send() or self.email.Display()

    def reply_email(self):
        self.outlook = win32.Dispatch('Outlook.Application').GetNameSpace('MAPI') 
        self.folders = self.outlook.GetDefaultFolder(6)
        def reply(email:object):
                self.reply = email.Reply()
                self.reply.bodyformat = 1
                self.reply.Subject = f''
                self.reply.To = ''
                self.reply.Bcc = ''
                self.message = ''
                self.reply.HTMLBody = f'{self.message}{self.reply.HTMLBody}' #combine last reply with your need message
                self.reply.Attachments.Add(path.join(getcwd(), f'{self.files}'))
                #self.email.Send() or self.email.Display()

        self.found = False
        for self.inbox in self.folders.Items:
                if self.inbox.Subject == '': #desire subject to look up
                        self.message = self.inbox 
                        self.found = True
        reply(self.message) #this method helps you to keep the last email sent with the desire subject

        if not self.found:
            self.outlook = win32.Dispatch('Outlook.Application').GetNameSpace('MAPI')
            self.email = self.outlook.CreateItem(0)
            self.email.bodyformat = 1
            self.email.Subject = ''
            self.email.To = ''
            self.email.Bcc = ''
            self.email.HTMLBody = ''
            self.email.Attachments.Add(path.join(getcwd(), f'{self.files}'))
            #self.email.Send() or self.email.Display()