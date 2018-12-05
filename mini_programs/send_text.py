from twilio import rest

account_sid = "enter your sid"
auth_token="enter your token"
client=rest.TwilioRestClient(account_sid,auth_token)

message=client.sms.messages.create(
	body="Hey this is Pinaki",
	to="twilio account number",
	from_="number")

print message.sid
