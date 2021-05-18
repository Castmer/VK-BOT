
import vk, time

def getPhoto(owner):
    return  'photo' +str(owner) + '_' + str(api.photos.get(owner_id = owner, album_id = -6, rev=1)[0]['pid'])

#моя страница 244728879

s = ""
att = ""
session = vk.Session(access_token="")
api = vk.API(session)

for i in range (1,len(api.users.getNearby(latitude = 55, longitude  = 36, radius = 4, fields = ['photo_id']))):
    print(api.users.getNearby(accuracy = 5, latitude = 55, longitude  = 36, radius = 4, fields = ['photo_id'])[i])
    time.sleep(0.70)

for i in range (1,len(api.users.getNearby(latitude = 55, longitude  = 36, radius = 4, fields = ['photo_id']))):
    att+=str(getPhoto(api.users.getNearby(accuracy = 5, latitude = 55, longitude  = 36, radius = 4)[i]['uid'])) + ','
    time.sleep(0.70)
    s+=api.users.getNearby(accuracy = 5, latitude = 55, longitude  = 36, radius = 4)[i]['first_name'] + " "
    time.sleep(0.70)
    s+=api.users.getNearby(accuracy = 5, latitude = 55, longitude  = 36, radius = 4)[i]['last_name']
    time.sleep(0.70)
    s+="\n"

print(att)

api.wall.post(owner_id = 244728879 ,friends_only = 0, message = "Относительно рядом со мной \n " + s, v='5.35', attachments = att)
#print(api.photos.get(owner_ids = 244728879, album_id = -15, v='5.52'))
