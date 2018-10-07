# fb-mess

## About

### Bot Types

#### Spam Bot

No one listening to you? They'll see your message now.

Details on how to use this can be found [here](#) 

**It is your responsibility not to get banned**

## Setup

### fbchat

This project relies entirely on the [fbchat](https://pypi.org/project/fbchat/) package for [Python](https://www.python.org/).

This can be installed globally or within a virtual environment using

`pip install fbchat`


### Facebook Messenger Login Credentials

The best way to handle login credentials for the *Facebook Messenger* account being made into a bot is to use environment variables.

This can be done on Linux using the following commands:

`export fb_user="<Facebook Username/Email>"`

`export fb_pass="<Facebook password>"`

This ensures that any credentials are kept out of the codebase and is as secure as the local machine it is running on.

The credentials can be accessed from within your code using the following snippet:

```python
import os

user = os.environ.get('fb_user')
passw = os.environ.get('fb_pass')
```

## Usage

### SpamBot

Example usage of the SpamBot is shown below:

```python
import bots
bot = bots.SpamBot(os.environ.get('fb_user'), os.environ.get('fb_pass'))
bot.setChat('<chat_ID>')
bot.setMessage("<Message>")
bot.start()
```

CTRL+C will stop it once running

## Todo

## Changelog
