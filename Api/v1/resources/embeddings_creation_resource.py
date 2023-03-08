import falcon
import falcon.asgi
import json
from ..schemas import json_schema
from datetime import datetime as dt
import time
import os


from ..schemas.audio_diarization import *
from main import inference
import asyncio

# TEST CLASS
# this is only to test the API

class EmbeddingsCreator(object):
    def __init__(self):
        super().__init__()

    # @json_schema.validate(audio_diarization_schema_req_get, audio_diarization_schema_resp_get)
    async def on_get(self, req, res):
        print('incoming GET request')
        """Handles a test GET request."""
        file_path = f'Files/AudioFiles/{req.params["file_id"]}.wav'
        embeddings = inference(file_path)
        listed = embeddings.toList()
        res.status = falcon.HTTP_200  # This is the default status
        res.media = {"embeddings": listed}
        res.json = {"embeddings": listed}

    # @json_schema.validate(audio_diarization_schema_req, audio_diarization_schema_resp)
    async def on_post(self, req, res):
        print('incoming POST request')
        """Handles a test POST request."""
        file_id = f'{dt.now().minute}{dt.now().second}{dt.now().microsecond}'
        outfile_name = f"Files/AudioFiles/{file_id}.wav"
        url = req.params["url"]
        download = asyncio.create_task(run_dowloader(url, file_id))
        value = download

        res.status = falcon.HTTP_200  # This is the default status
        res.media = {"message": f"We're downloading the file, ID will be {outfile_name}"}
        res.json = {"message": f"We're downloading the file, ID will be {outfile_name}"}