
import vk, time


#моя страница 244728879

s = ""
att = ""
session = vk.Session(access_token="b7690ac26382a9b074c4eb953e39a9ef0fb42c0e441df4813046ce1fbbae4d209b55f0af0f895844e8a6d")
api = vk.API(session)

for i in range (1,len(api.users.getNearby(latitude = 55, longitude  = 36, radius = 4, fields = ['photo_id']))):
    print(api.users.getNearby(accuracy = 5, latitude = 55, longitude  = 36, radius = 4, fields = ['photo_id'])[i])
    time.sleep(0.70)

for i in range (1,len(api.users.getNearby(latitude = 55, longitude  = 36, radius = 4, fields = ['photo_id']))):
    att+='photo' + api.users.getNearby(latitude = 55, longitude  = 36, radius = 4, fields = ['photo_id'])[i]['photo_id'] + ','
    time.sleep(0.70)
    s+=api.users.getNearby(accuracy = 5, latitude = 55, longitude  = 36, radius = 4)[i]['first_name'] + " "
    time.sleep(0.70)
    s+=api.users.getNearby(accuracy = 5, latitude = 55, longitude  = 36, radius = 4)[i]['last_name']
    time.sleep(0.70)
    s+="\n"

print(att)

api.wall.post(owner_id = 244728879 ,friends_only = 0, message = "Относительно рядом со мной \n " + s, v='5.35', attachments = att)
#print(api.photos.get(owner_ids = 244728879, album_id = -15, v='5.52'))
print(api.users.get(user_ids = 244728879, fields = ['photo_id']))
