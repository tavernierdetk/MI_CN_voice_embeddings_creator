import falcon
import falcon.asgi
import requests
import os
from datetime import datetime as dt
import json

from Api.middleware.cors import *
# from pydub import AudioSegment
from pyannote.audio import Model
from pyannote.audio import Inference


embeddings_creation_pipeline = Model.from_pretrained("pyannote/embedding", use_auth_token="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")
inference = Inference(embeddings_creation_pipeline, window="whole")

import re

app = falcon.asgi.App(
    middleware=[CorsMiddleware()]
)

from Api.routes import *

print('['+ dt.now().strftime('%Y-%m-%d %H:%M:%S') +']' + ' Routes loaded ! ✅')
print('['+ dt.now().strftime('%Y-%m-%d %H:%M:%S') +']' + ' This server is ready !')
