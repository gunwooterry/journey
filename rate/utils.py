from .models import UserProfile, Tag


def recommend(user):
    rec_num = 3     # how many recommendations
    userprofile = UserProfile.objects.get(user=user)
    pref_list = userprofile.preferences.all()
    tag_counter = [0]*Tag.objects.all().count()
    for pref in pref_list:
        for tag in pref.destination.tags.all():
            tag_counter[tag.tag_id-1] += pref.score
    not_visited = [pref.destination for pref in userprofile.preferences.filter(score=0)]
    rec_list = sort_dest(not_visited, tag_counter)[:rec_num]
    return rec_list


def sort_dest(dest_list, tag_counter):
    dest_counter = [[dest, 0] for dest in dest_list]
    for dest_pair in dest_counter:
        for tag in dest_pair[0].tags.all():
            dest_pair[1] += tag_counter[tag.tag_id-1]
    dest_counter.sort(reverse=True, key=lambda x: x[1])
    return [dest_pair[0] for dest_pair in dest_counter]
