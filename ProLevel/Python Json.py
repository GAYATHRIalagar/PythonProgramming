{
  "id":{CHANNEL_ID},
  "kind": "youtube#channel",
  "etag": etag,
  "contentDetails":{
    "relatedPlaylists":{
      "likes":{LIKES_PLAYLIST_ID},
      "favorites":{FAVORITES_PLAYLIST_ID},
      "uploads":{UPLOADS_PLAYLIST_ID},
      "watchHistory":{WATCHHISTORY_PLAYLIST_ID},
      "watchLater":{WATCHLATER_PLAYLIST_ID}
   },
    "googlePlusUserId": string
 },
}
import json 
parsed_json= json.loads(json_str)
print(parsed_json['likes'])
Json_Str_data= {"id":{CHANNEL_ID},
  "kind": "youtube#channel",
  "etag": etag,
  "contentDetails":{
    "relatedPlaylists":{
      "likes":{LIKES_PLAYLIST_ID},
      "favorites":{FAVORITES_PLAYLIST_ID},
      "uploads":{UPLOADS_PLAYLIST_ID},
      "watchHistory":{WATCHHISTORY_PLAYLIST_ID},
      "watchLater":{WATCHLATER_PLAYLIST_ID}, 'titles': ['fields', 'creator'],}
print(json.dumps(Json_Str_data)) 
import json from pprint 
import pprint with open('data.json') as data_file: 
data=json.load(data_file) 
pprint(data)
