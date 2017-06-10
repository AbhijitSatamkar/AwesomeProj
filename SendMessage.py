from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC35624b67db66a2df32bcda22ff171d7e"
# Your Auth Token from twilio.com/console
auth_token  = "37a8fd6680ca41b2158ed72c9dee4776"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+31623472901",
    from_="+3197004499127",
    body="Hello Sweetheart, This message is for you!! Good Night!! Love U!!")

print(message.sid)