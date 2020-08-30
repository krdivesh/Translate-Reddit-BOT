import praw
import os
from googletrans import Translator

#changes current directory
os.chdir('/home/diveshcode/Reddit Bots/wordbot')

#   reddit API login
reddit = praw.Reddit("bot1", user_agent = 'word-bot by Divesh')

# calling Google Trasnlator
translator = Translator()



# the subreddits you want your bot to live on
subreddit = reddit.subreddit('BotTest_for_coders')

# phrase to activate the bot
keyphrase = '!translate '

# look for phrase and reply appropriately
for comment in subreddit.stream.comments():
    if keyphrase in comment.body:
        to_translate = comment.body.replace(keyphrase, '')
        try:  
            print('Handling' + comment.body)  
            welcome = "beep. boop. 🤖 I'm a bot that translate text to Hindi"
            msg = welcome  + '\n\n' + str(translator.translate(to_translate, dest='hi'))
            comment.reply(msg)
            print(msg)
        except:
            comment.reply(welcome + '\n' + 'I am not well rn. Try another time')
            print('Error')
