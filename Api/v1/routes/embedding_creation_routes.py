from main import app
from ..resources.embeddings_creation_resource import  *

app.add_route('/create_embeddings', EmbeddingsCreator())
