from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def drums(request):
    return render(request,'drums.html')
def bass(request):
    return render(request,'bass.html')
def vox(request):
    return render(request,'vox.html')