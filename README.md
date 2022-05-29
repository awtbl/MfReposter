# MfReposter
## Create mirror of channel in Telegram!
### Example

#### Original channel
<img src='.github/original_channel.png'>

### Mirror
<img src='.github/channel_mirror.png'>

### How to run?

#### Clone repo

```shell
git clone https://github.com/awtbl/MfReposter.git
```

#### Install dependencies
```shell
cd MfReposter/
pip install -r requirements.txt
```
### Also create a config file
```shell
touch config.ini
vim config.ini
```
### Example config
```ini
[scheduler]
; one check per minute
update_interval = 60 ; You can configure interval
[db]
url = sqlite://database.db ; Here I using SQLite as db, you can use for example MySQL
[pyrogram]
api_id = ; API_ID, obtain it from my.telegram.org
api_hash = ; api_hash, obtain it from my.telegram.org
[channels]
original = ; provide ID or USERNAME of Original channel
duplicate = ; provide ID or USERNAME of Channel which will be mirror

```

Copy & paste example to your config.ini and fill each field <br>
You can get <b>API_ID</b> and <b>API_HASH</b> from <a href='https://my.telegram.org'>here</a>!

## Run
```shell
python main.py
```

With ❤, Awaitable
