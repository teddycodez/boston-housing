from django.shortcuts import render
from housing.boston import regg

def index(res):
    if res.method=="POST":
        print("J")
        rec = []
        for i in res.POST.keys():
            if i!="csrfmiddlewaretoken":
                rec.append(int(res.POST.get(i)))
        result = regg(rec)
        return render(res, "index.html", {"prediciton":result, "result":True})
    return render(res, "index.html")

def evolution(res):
    return render(res, "index.html")
