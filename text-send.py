from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACd96a890e0e24c2f333a00ece5a9c1849"
# Your Auth Token from twilio.com/console
auth_token  = "c*********************************"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+917992485XXX",
    from_="+13135286XXX",
    body="hi i m trying to send this message from pythom - shubham")

print(message.sid)