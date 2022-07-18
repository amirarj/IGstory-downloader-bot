# IGstory-downloader-bot
a Telegram bot for downloading Instagram stories

## Installation

first of all clone the project

```bash
git clone https://github.com/amirarj/IGstory-downloader-bot.git
```
install all of the packages in requirements.txt file 
```bash
pip install -r requirements.txt
```
edit `config.py` file with your Instsgram request header and Telegram Bot Token
```python
Cookie = ''
UserAgent = ''
XCSRFToken = ''
XIGAppID = ''
XIGWWWClaim = ''

# Telegram Config
BOT_TOKEN = ''
```

you can get Instsgram request header when you login via web 

![Capture1](https://user-images.githubusercontent.com/53288604/179472487-cc72865e-2320-41cd-926b-98322df1793f.png)

## Usage
```python
python main.py
```
start the bot with `/start` and then send a Instagram username.
