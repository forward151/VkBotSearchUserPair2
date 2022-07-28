import vk_api

token = 'vk1.a.ngDTFlA7gvQJaAuobj1fAqLgZjapvMn6T60ts8ubHuXdPzNkK5F7uOJ3HU5vG5fDGS09i1emess3LbRYw624ed23n78vR3ZsX1qpaFeCW66GwLDMbVdhvhumZbaedS7g7nUVq8A5rfvpv7fSvC1Av_gnX0M45tm7uY1JKs3SD04CqBhtIlIFw7pOknLLO6-O'
vk = vk_api.VkApi(token='vk1.a.Le8eoPhT-wx8W9qgcQpg7vY-ws2bdVA8IiBNeWPabzUSUG1J2N2yvkpnZ_SoLRqad4AZBExppgamd-dY0XbA2mSy-Ri89jtsCgSsfa0dlKspHtPMnt0OQe6GeMRRHee1gVKV7bmFGPDxOXx_hT0_ndHxoLzR-eWVEoDaNXs2HTt8cYg9CNzKDWc-UKlxgiuh')
vk_session = vk.get_api()

result = vk_session.users.search(from_group=1, sort=0, count=10, fields='deactivated, is_closed, counters, sex', hometown='Москва',
                                      sex=1, status=5, age_from=20, age_to=20, has_photo=1)

for i in result['items']:
    if not i['is_closed']:
        nums = vk_session.users.get(user_ids=i['id'], fields='counters')[0]['counters']
        id = vk_session.users.get(user_ids=i['id'], fields='counters')[0]['id']
        photo_amount = nums['photos']
        if photo_amount >= 3:
            code = i['track_code']
            print(i)
            print(nums)
            name = i['first_name']
            surname = i['last_name']
            photos = vk_session.photos.getProfile(owner_id=id)['items']
            list_of_photos = []
            result = []
            for i in photos:
                list_of_photos.append(i['id'])
            print(list_of_photos)
            for i in list_of_photos:
                information = vk_session.photos.getById(photos=f'{id}_{i}', extended=1)
                print(information)
                amout_of_likes = information[0]['likes']
                link = information[0]['orig_photo']['url']
                print(amout_of_likes)
                result.append({'photo_id': i, 'user_id': id, 'likes': amout_of_likes['count'], 'link': link})

            result.sort(key=lambda i: i['likes'], reverse=True)
            result.sort(key=lambda i: i['likes'], reverse=True)
            result = result[0:3]
            print(result)
            photo_string = f'photo-{result[0]["user_id"]}_{result[0]["photo_id"]},photo-{result[1]["user_id"]}_{result[1]["photo_id"]},photo-{result[2]["user_id"]}_{result[2]["photo_id"]}'
            print(name, surname, photo_string)
            break
