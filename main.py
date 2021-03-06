import win32com.client as win32
import datetime

date = datetime.datetime.today()
date = date.strftime("%m/%d/%y")
# Add who you want to send the email to
to_email = "example@outlook.com"

# Add your subject line and body of the message here
subject = "CS3339 - YOUR NAME - I participated in class today on " + date
message = "I participated in class today.\n \n Best regards, \n YOUR NAME"

# Function that sends the email
def sendEmail(to_email, subject, message):
    try:
        print("start try")
        outlook = win32.Dispatch('outlook.application')
        print("connected to outlook")
        mail = outlook.CreateItem(0)
        print("outlook created item")
        mail.To = to_email
        mail.Subject = subject
        mail.Body = message
        print("sending...")
        mail.Send()
        print("sent")
        return True
    except Exception as e:
        print("tried")
        print("Error: " + str(e))
        return False


sendEmail(to_email, subject, message)