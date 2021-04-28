# Lava.sh: memes have never been so annoying

<img src="https://raw.githubusercontent.com/mandarin10101/Lava.sh/main/logo.png" width="500" height="250">

this is a telegram client that automates replies to pictures and videos that come to your chats.

it is ready to run on your machine / for deploying on heroku, so you just need to:

1. set it up to respond to your meme loving buddies.
2. forget about it but your friend will think you're acting for real.

your steps to make it work:

1. create telegram client app on https://my.telegram.org (just 2-3 clicks) and copy *api_id* and *api_hash.*

2. install *telethon* and *requests* libraries for python.

3. clone repository.

4. run `setup.sh`.

5. edit *config.json*:

   ```
   {
       "client_api_id": 0123456, (𝗽𝗮𝘀𝘁𝗲 𝗮𝗽𝗶_𝗶𝗱 𝗵𝗲𝗿𝗲)
       "client_api_hash": "𝘅𝘅𝘅𝘅𝘅𝘅𝘅𝘅_𝘆𝗼𝘂𝗿_𝗮𝗽𝗶_𝗵𝗮𝘀𝗵_𝘅𝘅𝘅𝘅𝘅𝘅𝘅𝘅𝘅",
       "session_name": "𝘆𝗼𝘂_𝗻𝗮𝗺𝗲_𝗶𝘁",
       "response_delay": [
           240,            (𝗱𝗲𝗹𝗮𝘆 𝗯𝗲𝗳𝗼𝗿𝗲 𝗿𝗲𝘀𝗽𝗼𝗻𝘀𝗲 𝗶𝗻 𝘀𝗲𝗰𝗼𝗻𝗱𝘀: 𝗳𝗿𝗼𝗺)
           1800            (𝘁𝗼)
       ],
       "sleep_time": [
           23,             (𝘁𝗵𝗲 𝗮𝗽𝗽𝗹𝗶𝗰𝗮𝘁𝗶𝗼𝗻 𝗴𝗼𝗲𝘀 𝘁𝗼 𝘀𝗹𝗲𝗲𝗽, 𝗷𝘂𝘀𝘁 𝗹𝗶𝗸𝗲 𝘆𝗼𝘂: 𝗳𝗿𝗼𝗺)
           10              (𝘂𝗽 𝘁𝗼, 𝗶𝗻𝗰𝗹𝘂𝗱𝗶𝗻𝗴)
       ],
       "targets": [
           "John Doe",     (𝗲𝗻𝘂𝗺𝗲𝗿𝗮𝘁𝗶𝗼𝗻 𝗼𝗳 𝘂𝘀𝗲𝗿𝗻𝗮𝗺𝗲𝘀 𝘁𝗼 𝘄𝗵𝗼𝗺 𝘄𝗲 𝘄𝗶𝗹𝗹 𝗿𝗲𝗽𝗹𝘆,)
           "Skrillex"      (𝗮𝘀 𝘁𝗵𝗲𝘆 𝗮𝗿𝗲 𝗱𝗶𝘀𝗽𝗹𝗮𝘆𝗲𝗱 𝗶𝗻 𝘆𝗼𝘂𝗿 𝗰𝗵𝗮𝘁𝘀, 𝗼𝗿 𝘁𝗵𝗲𝗶𝗿 𝗶𝗱𝘀)
       ],
       "messages": [
           "LOL",          (𝗵𝗲𝗿𝗲 𝘄𝗲 𝘄𝗿𝗶𝘁𝗲 𝗺𝗲𝘀𝘀𝗮𝗴𝗲𝘀 𝘁𝗵𝗮𝘁 𝘄𝗶𝗹𝗹 𝗯𝗲 𝘀𝗲𝗻𝘁)
           "Oh my dude",   (𝗶𝗻 𝗿𝗮𝗻𝗱𝗼𝗺 𝗼𝗿𝗱𝗲𝗿 𝘄𝗶𝘁𝗵𝗼𝘂𝘁 𝗿𝗲𝗽𝗲𝗮𝘁𝘀)
           ")))",
           "🤔🤔🤔",
           "That's real shit",
           "Damn boy"
       ]
   }
   ```

   

6. run ```python auth.py``` to sign in to telegram. this step will create *<session_name>.session* which will be helpful to work on heroku (you can't sign in to telegram on heroku server – telegram won't send the login code but you can do it on your machine before deploying, *.session* file saves the authorization).

7. run `python client.py`. client is now online.

Deploying on heroku:

8. create new python app on https://heroku.com
9. push all files (including *<session_name>.session*, *Procfile*, *requirements.txt* and *runtime.txt* !) to heroku in any available way (heroku git or github).
10. run worker in console on heroku: `heroku ps:scale worker=1`
11. nice work, mate.
