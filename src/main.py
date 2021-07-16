import tekore as tk
import os

client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")


app_token = tk.request_client_token(client_id, client_secret)
spotify = tk.Spotify(app_token)
