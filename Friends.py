import vk, time


def getPhoto(owner):
    return api.photos.get(owner_id = owner, album_id = -6, rev=1)[0]['pid']

#моя страница 244728879

att = ""
s = ""
session = vk.Session(access_token="")
api = vk.API(session)
friends = list(api.friends.get(user_id = 244728879)).copy()

#album = api.photos.createAlbum(title = 'friends')
print(api.photos.getAlbums(owner_id = 202205518, need_system = 1))
print(getPhoto(202205518))

for i in friends:
    time.sleep(0.6)
    if 'deactivated' in dict(api.users.get(user_ids = i)[0]).keys():
        time.sleep(0.6)
        if api.users.get(user_ids = i)[0]['deactivated'] == 'banned' or api.users.get(user_ids = i)[0]['deactivated'] == 'deleted':
            friends.pop(friends.index(i))

for i in friends:
    print(str(i) + ": ", end='')
    try:
        print(getPhoto(i))
        att += 'photo' + str(i) + '_' + str(getPhoto(i)) + ','
    except Exception:
        print(420488639)
        att += 'photo244728879_420488639' + ','
    time.sleep(0.34)

for i in friends:
    s += api.users.get(user_ids=i)[0]['first_name'] + " "
    time.sleep(0.4)
    s += api.users.get(user_ids=i)[0]['last_name']
    time.sleep(0.4)
    s += "\n"

att = att[0:-1]
attL = str(att).split(',')
print(attL)

sL = s.split("\n")
print(sL)

b = 10 - (len(sL) % 10)

for i in range ((len(sL)+b)//10):
    api.wall.post(owner_id = 244728879 ,friends_only = 0, message = sL[0:10], v='5.35', attachments = attL[0:10])
    sL = sL[10:]
    attL = attL[10:]



