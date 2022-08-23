# Telegram to Telegram Forwarder

A userbot to scrap your Favourite Telegram chats, groups or channels to your single specific Telegram Chat(Channel/Group also).

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/prabesharyal/Tg-Many-To-One/tree/main/)

# Table of Contents
 1. [Introduction](#1)
    1. [About User Bot](#1.1)
	2. [Working Principle](#1.2)
 2. [Knowing All Variables](#2)
	1. [API Codes](#2.1)
    2. [Channel ID](#2.2)
	3. [Other Notable Variables](#2.3)
 4. [Requirements](#3)
    1. [Python](#3.1)
		1. [PIPs](#3.1.1)
 5. [Deploy](#4)
 6. [License](#lic)


# Read this throughly before deploying the bot: <a name="1"></a>

## What is this bot about?<a name="1.1"></a>
This bot is make specifically for one purpose. That is to monitor many Telegram Channels and send to you in one Telegram chat of any form removing hashtags and mentions.

## How does this bot work?<a name="1.2"></a>
> **This bot works in various steps as :**
> - It listens for new posts in your Telegram Channels.
> - Tries to clean captions (beta stage).
> - Send Caption, Media or both.
> - Also, it sends an empty sticker to distinguish between posts.
		
# Get Variables <a name="2"></a>

## API_ID and API_Hash <a name="2.1"></a>
 - You can get Telegram API Codes from [Official Telegram API dashboard](https://my.telegram.org) .
 
## Getting Channel ID <a name="2.2"></a>
### **Private Channels/Groups**
- Send a Message to channel and copy link of that Telegram Channel Post.
> - Then your link looks like this : `https://t.me/c/1617181920/369`
> - Note that long number of 10 digits and add -100 in beginning and it must look like: `-1001617181920`
> - This is your Channel ID (including `-` sign.)

### **Public Channels/Person/Groups**
- Send a Message `/info @ChannelName` to [GroupHelpBot](https://t.me/GroupHelpBot) and copy link of that Telegram Channel Post.
> _Note_ : For pivate chats with no username, mention the person in group or send `/info` command from that respective account to [GroupHelpBot](https://t.me/GroupHelpBot) .
 
## Other Variables <a name="2.3"></a>
There are some other variables which you need to note about.
### Session String
- Generate Session String in a file using the code below:
> 
```from telethon.sync import TelegramClient
from telethon.sessions import StringSession

api_id = 0000
api_hash = 'sdfghklasaaddadadasd'

with TelegramClient(StringSession(), api_id, api_hash) as client:
    session= client.session.save()
    print(session)
    r = open("new_session_file.session","w")
    r.write(session)
    r.close()
	
```

### Variables as configured in bot. <a name="environ"></a>
- `BOT_API_TOKEN` - Enter Bot API Token which you get from Botfather in Telegram.
- `from_ids` - Enter [Channel ID](#2.2) of your Telegram Channel from where you want to watch posts. Can be multiple channels, groups, chats in list form separated by comma.
- `to_id` - Enter a Chat ID of where you'll get all posts/messages.
- `every_post_caption` - Enter a Caption for every posts you sent to Telegram in image. Can be your channel username or some emoji.

# Required Softwares and Languages <a name="3"></a>

## Python <a name="3.1"></a>
> Download Python From here :
> - [Python Latest Version](https://www.python.org/downloads/)

> *While installing, tick install **path / environment** variables whatever is given*

### Python Snippets <a name="3.1.1"></a>
- **Install required python modules using commands below:**
> - `pip install telethon`

- __Install all above modules using :__
> - `pip install -r requirements.txt`


# Deploying the bot <a name="4"></a>

## Deploying Locally
- Install Python, PIPs using [above methods](#3)
- Download all files in this repo.
- Replace variables at the top of `bot.py` file with your ones, removing `os.environ.get('name')` commands.

> Type ***any one*** of the following command on terminal to run bot:
> - `py bot.py`
> - `python bot.py`
> - `python3 bot.py`

## Deploying to HEROKU :
Press the button below or at the top of this readme and insert necessary [environment variables](#environ) and you're done.
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/prabesharyal/Tg-Many-To-One/tree/main/)

# License <a name="lic"></a>
> Distributed Under GPL or MIT License by [@PrabeshAryalNP](https://t.me/prabesharyalnp) on [social](https://twitter.com/prabesharyalnp) or [@PrabeshAryal](https://github.com/prabesharyal) on code sites.
		
