from .models import UserProfile, Tag
from random import randint


def recommend(user):
    rec_num = 2     # how many recommendations
    userprofile = UserProfile.objects.get(user=user)
    pref_list = userprofile.preferences.all()
    tag_counter = [0]*Tag.objects.all().count()
    for pref in pref_list:
        for tag in pref.destination.tags.all():
            tag_counter[tag.tag_id-1] += pref.score
    top_tags = [Tag.objects.get(tag_id=x+1) for x in top_k_index(tag_counter, rec_num)]
    rec_list = []
    for tag in top_tags:
        dest_set = tag.destination_set.all()
        rec = dest_set[randint(0, dest_set.count()-1)]
        rec_list.append(rec)
    return rec_list


def top_k_index(lst, k):
    result = list(range(len(lst)))
    result.sort(key=lambda x: lst[x])
    return result[:k]
