from django.shortcuts import render
from django.views.generic import TemplateView
class HomePageView(TemplateView):
    template_name = 'home.html'

def search(request):
    """
    Search users page
    :param request:
    :return:
    """
    users = list(UserProfile.objects.all())
    for user in users:
        if user.username == request.user.username:
            users.remove(user)
            break
    if request.method == "POST":
        print("SEARCHING!!")
        query = request.POST.get("search")
        user_ls = []
        for user in users:
            if query in user.name or query in user.username:
                user_ls.append(user)
        return render(request, "chat/search.html", {'users': user_ls, })

    try:
        users = users[:10]
    except:
        users = users[:]
    id = getUserId(request.user.username)
    friends = getFriendsList(id)
    return render(request, "chat/search.html", {'users': users, 'friends': friends})
