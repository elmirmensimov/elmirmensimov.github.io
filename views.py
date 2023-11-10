from django.shortcuts import render, redirect

def login(request):
    # login işlemlerinin yapıldığı kodlar burada yazılır
    return render(request, 'home/login.html', context={})

def user_order_track(request, pid):
    order = Booking.objects.get(id=pid)
    orderstatus = ORDERSTATUS
    return render(request, "user-order-track.html", locals())
