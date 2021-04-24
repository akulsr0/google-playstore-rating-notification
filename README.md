# Google Playstore Rating Notifications

## Get Google Playstore Rating Updates on SMS

## Requirements

You need to have a Twilio account.

- Account SID
- Auth Token
- Sender Number
- Target Number

```python
pip install -r requirements.txt
```

## Configuration

- In `ratings.py`, change `app_url` to your Google Playstore app url.
  
- Add Twilio config to `.env.dev`, copy all, create a new `.env` file, paste there.
  
- In `sms.py`, change `sms_text` as your desired output message.

- ```python
  python main.py
  ```
  