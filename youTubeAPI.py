
from googleapiclient.discovery import build

youTubeAPIKey = "AIzaSyBSqET3ABa66Z6ebXBhQ23dlnBphctlaoQ"

youtube = build("youtube", "v3", developerKey = youTubeAPIKey)