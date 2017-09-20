## TEXT SENDER

Send _text_ directly from your computer to **mobile numbers** using twilio API

## INSTALL

Requires Python 3.6
```
    Install python 3.6
```
pip install **twilio** API
```
    pip install twilio
```
For detailed procedure to pip install click [here](installTWILIO.md)

> Signup in twillio (_two signup click [here](https://www.twilio.com/try-twilio?g=%2Fconsole&t=9cbd31d04513d0805f0a5ca84a516c9aa6948404067a42c755ccee381f63a89b)_) after signup you will get 

Your Account SID from twilio.com/console
```
account_sid = "A*********************************"
```
Your Auth Token from twilio.com/console
```
auth_token  = "c*********************************"
```
your twilio number
```angular2html
from_="+13135286XXX"
```
replace the above info from `text-send.py` with yours

```angular2html
    run text-send.py
```

## USAGE

> change the information with your details _ex:_
```
account_sid = "A*********************************"
auth_token  = "c*********************************"
from_="+13135286XXX"
 ```
> And the **phone number** you want to send text to _(without buying credits you can only send message **to registered mobile no.**)_
```
    to="+917992485XXX"
```
> Write the message you want to send in the body of `text-send.py`
```
body="you can write the message here - shubham")
```
> run the `text-send.py` 
 ```angular2html
the phone no. entered in to will recieve the message.
```
