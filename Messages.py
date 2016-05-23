import vk, time


def getPhoto(owner)

#моя страница 244728879

att = ""
session = vk.Session(access_token="b7690ac26382a9b074c4eb953e39a9ef0fb42c0e441df4813046ce1fbbae4d209b55f0af0f895844e8a6d")
api = vk.API(session)
friends = list(api.friends.get(user_id = 244728879)).copy()

#album = api.photos.createAlbum(title = 'friends')
print(api.photos.getAlbums(owner_id = 202205518, need_system = 1))
for i in api.photos.get(owner_id = 202205518, album_id = -6, rev=1):
    print(i)

'''for i in friends:
    time.sleep(0.5)
    if 'deactivated' in dict(api.users.get(user_ids = i)[0]).keys():
        time.sleep(0.5)
        if api.users.get(user_ids = i)[0]['deactivated'] == 'banned' or api.users.get(user_ids = i)[0]['deactivated'] == 'deleted':
            friends.pop(friends.index(i))

for i in friends:
    print(api.users.get(user_ids = i, fields = ['photo_max']))
    time.sleep(0.34)

for i in friends:
    print(api.users.get(user_ids = i, fields = ['photo_max'])[0]['photo_max'])
    time.sleep(0.34)'''
