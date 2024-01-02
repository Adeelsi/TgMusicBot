import os
import logging
from dotenv import load_dotenv

if os.path.exists('config.env'):
    load_dotenv('config.env', override=True)


class Config:
    def __init__(self) -> None:
        self.SESSION: str = os.environ.get('SESSION'," File "main.py", line 13, in <module>
    with app:
  File "/opt/virtualenvs/python3/lib/python3.8/site-packages/pyrogram/client.py", line 251, in __enter__
    return self.start()
  File "/opt/virtualenvs/python3/lib/python3.8/site-packages/pyrogram/sync.py", line 51, in async_to_sync_wrap
    return loop.run_until_complete(coroutine)
  File "/usr/lib/python3.8/asyncio/base_events.py", line 616, in run_until_complete
    return future.result()
  File "/opt/virtualenvs/python3/lib/python3.8/site-packages/pyrogram/methods/utilities/start.py", line 52, in start
    is_authorized = await self.connect()
  File "/opt/virtualenvs/python3/lib/python3.8/site-packages/pyrogram/methods/auth/connect.py", line 39, in connect
    await self.load_session()
  File "/opt/virtualenvs/python3/lib/python3.8/site-packages/pyrogram/client.py", line 692, in load_session
    await Auth(
  File "/opt/virtualenvs/python3/lib/python3.8/site-packages/pyrogram/session/auth.py", line 254, in create
    raise e
  File "/opt/virtualenvs/python3/lib/python3.8/site-packages/pyrogram/session/auth.py", line 89, in create
    res_pq = await self.send(raw.functions.ReqPqMulti(nonce=nonce))
  File "/opt/virtualenvs/python3/lib/python3.8/site-packages/pyrogram/session/auth.py", line 67, in send
    return self.unpack(response)
  File "/opt/virtualenvs/python3/lib/python3.8/site-packages/pyrogram/session/auth.py", line 60, in unpack
    return TLObject.read(b)
  File "/opt/virtualenvs/python3/lib/python3.8/site-packages/pyrogram/raw/core/tl_object.py", line 33, in read
    return cast(TLObject, objects[int.from_bytes(b.read(4), "little")]).read(b, *args)")
        self.API_ID: str = os.environ.get('API_ID',"14520922")
        self.API_HASH: str = os.environ.get('API_HASH', "703d38a27d19074a1f39ca0165ef9e1e")
        self.SUDO: list = [int(id) for id in os.environ.get(
            'SUDO', ' ').split() if id.isnumeric()]
        if not self.SESSION or not self.API_ID or not self.API_ID:
            print('Error: SESSION, API_ID and API_HASH is required.'
                  'Please check your config.env file.')
            quit(0)
        self.SPOTIFY: bool = False
        self.SPOTIFY_CLIENT_ID: str = os.environ.get('SPOTIFY_CLIENT_ID', None)
        self.SPOTIFY_CLIENT_SECRET: str = os.environ.get(
            'SPOTIFY_CLIENT_SECRET', None)
        _log_level = os.environ.get('LOG_LEVEL', 'error').lower()
        if _log_level == 'error':
            self.LOG_LEVEL = logging.ERROR
        elif _log_level == 'info':
            self.LOG_LEVEL = logging.INFO
        elif _log_level == 'debug':
            self.LOG_LEVEL = logging.DEBUG
        else:
            self.LOG_LEVEL = logging.ERROR
        self.PREFIXES: list = os.environ.get('PREFIX', '!').split()
        self.DEFAULT_LANG: str = os.environ.get('DEFAULT_LANG', 'tr').lower()
        self.DEFAULT_STREAM_MODE: str = 'audio' if (os.environ.get(
            'DEFAULT_STREAM_MODE', 'audio').lower() == 'audio') else 'video'


config = Config()
