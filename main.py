# from twilio.rest import Client

# from datetime import datetime, timedelta

# import time

# #step-2 twilio credentials
# account_sid='AC0f342e99ce12b08d005c8a0a43ad3ecc'
# auth_token='198f9cc9654635aacd5c3de51bb7385b'

# client = Client(account_sid, auth_token)
# #step-3 degine send message function

# def send_whatsapp_message(recipient_number, message_body):
# try:
# message = client.messages.create(
# from_='whatsapp:+14155238886',
# body=message_body
# to=f'whatsapp:{recipient_number}'
# )
# print(f'Message sent successfully! Message SID{message.sid}')
# except Exception as e:
# print('An error occurred')


# #step-4 user input
# name = input('Enter the recipient name = ')
# recipient_number = input('Enter the recipient Whatsapp number with country code (e.g, +12345:)')
# message_body = input(f'enter the message you want to send to {name}: ')

# #step-5 parse date/time and calculate delay
# date_str = input('enter the date to send the message (YYYY-MM-DD):')
# time_str = input('enter the time to send the message (HH:MM in 24hour format): ')

# #datetime
# schedule_datetime = datetime.strptime(f'{date_str} {time_str}' ,"%H-%m-%d %H:%M") 
# current_datetime = datetime.now()

# #calculate delay
# time_difference = schedule_datetime - current_datetime
# delay_seconds = time_difference.total_seconds()

# if delay_seconds <= 0:
# print('The specified time is in the past. Please enter a future date and time: ')
# else:
# print(f'Message scheduled to be sent to {name} at {schedule_datetime}.')

# #wait until the scheduled time
# time.sleep(delay_seconds) #1000

# #send the message
# send whatsapp_message(recipient_number,message_body)


from twilio.rest import Client
from datetime import datetime, timedelta
import time

# Step 2: Twilio credentials
account_sid = 'AC0f342e99ce12b08d005c8a0a43ad3ecc'
auth_token = '198f9cc9654635aacd5c3de51bb7385b'
client = Client(account_sid, auth_token)

# Step 3: Define send message function
def send_whatsapp_message(recipient_number, message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',  # Use your Twilio WhatsApp number here
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print(f'Message sent successfully! Message SID: {message.sid}')
    except Exception as e:
        print(f'An error occurred: {e}')

# Step 4: User input
name = input('Enter the recipient name: ')
recipient_number = input('Enter the recipient WhatsApp number with country code (e.g., +1234567890): ')
message_body = input(f'Enter the message you want to send to {name}: ')

# Step 5: Parse date/time and calculate delay
date_str = input('Enter the date to send the message (YYYY-MM-DD): ')
time_str = input('Enter the time to send the message (HH:MM in 24-hour format): ')

try:
    schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
    current_datetime = datetime.now()

    # Calculate delay
    time_difference = schedule_datetime - current_datetime
    delay_seconds = time_difference.total_seconds()

    if delay_seconds <= 0:
        print('The specified time is in the past. Please enter a future date and time.')
    else:
        print(f'Message scheduled to be sent to {name} at {schedule_datetime}.')
        time.sleep(delay_seconds)
        send_whatsapp_message(recipient_number, message_body)

except ValueError as ve:
    print(f'Date/time format error: {ve}')
