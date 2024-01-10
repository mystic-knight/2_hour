
from twilio.rest import Client
from configs.env import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER

twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_otp_via_twilio(to_phone_number: str):
    otp = '32212'
    message = twilio_client.messages.create(
        body=f"Your OTP is: {otp}",
        from_=TWILIO_PHONE_NUMBER,
        to=to_phone_number
    )
    return message.sid


def request_otp(to_phone_number):
    response = {}
    send_otp_via_twilio(to_phone_number)
    return response



# payload 
# {phone_number: "6260857553"}
# phone_number
# : 
# "6260857553"

# response 
# instance_id
# : 
# "26ee90b8-eb5c-4c77-a435-235ee5c6"
# is_logged_in
# : 
# false
# phone_number
# : 
# "6260857553"
# request_id
# : 
# "b3M.U4EnDIOToU"
# resend_otp_wait_time
# : 
# 60