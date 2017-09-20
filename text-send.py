from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC********************************"
# Your Auth Token from twilio.com/console
auth_token  = "c*********************************"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+917992485XXX",
    from_="+13135286XXX",
    body="write your message here - shubham")

print(message.sid)