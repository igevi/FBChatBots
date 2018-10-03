# fb-mess

## About

## Setup

### Facebook Messenger Login Credentials

The best way to handle login credentials for the *Facebook Messenger* account being made into a bot is to use environment variables.

This can be done on Linux using the following commands:

`export "fb_user"="<Facebook Username/Email>"`

`export "fb_pass"="<Facebook password>"`

This ensures that any credentials are kept out of the codebase and is as secure as the local machine it is running on.

The credentials can be accessed from within your code using the following snippet:

```python
import os

user = os.environ.get('fb_user')
passw = os.environ.get('fb_pass')
```

## Usage

## Todo

## Changelog
