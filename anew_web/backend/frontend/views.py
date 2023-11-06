from .States.data import audio_path_pan, audio_path_ber
from .States.data import audio_path_ter, audio_path_sob
from .States.data import audio_path_lbdb, audio_path
from django.http import HttpResponse
from django.shortcuts import render
import os

def index(request):
    return render(
    request,'index.html')
def play_audio(request):
    try:
        audio_file_path = audio_path
        command = f"afplay {audio_file_path}" 
        os.system(command)
        return HttpResponse('{"status": "success"}', content_type="application/json")
    except Exception as e:
        error_message = str(e)
        return HttpResponse(f'{{"status": "error", "message": "{error_message}"}}', content_type="application/json")
def drums(request):
    return render(
    request,'drums.html')
def play_laidback(request):
    try:
        audio_file_path = audio_path_lbdb
        command = f"afplay {audio_file_path}" 
        os.system(command)
        return HttpResponse('{"status": "success"}', content_type="application/json")
    except Exception as e:
        error_message = str(e)
        return HttpResponse(f'{{"status": "error", "message": "{error_message}"}}', content_type="application/json")
def bass(request):
    return render(
    request,'bass.html')
def pandas(request):
    try:
        audio_file_path = audio_path_pan
        command = f"afplay {audio_file_path}" 
        os.system(command)
        return HttpResponse('{"status": "success"}', content_type="application/json")
    except Exception as e:
        error_message = str(e)
        return HttpResponse(f'{{"status": "error", "message": "{error_message}"}}', content_type="application/json")
def vox(request):
    return render(
    request,'vox.html')
def afrobeat(request):
    try:
        audio_file_path = audio_path_sob
        command = f"afplay {audio_file_path}" 
        os.system(command)
        return HttpResponse('{"status": "success"}', content_type="application/json")
    except Exception as e:
        error_message = str(e)
        return HttpResponse(f'{{"status": "error", "message": "{error_message}"}}', content_type="application/json")
def about(request):
    return render(
    request,'about.html')
def tera(request):
    try:
        audio_file_path = audio_path_ter
        command = f"afplay {audio_file_path}" 
        os.system(command)
        return HttpResponse('{"status": "success"}', content_type="application/json")
    except Exception as e:
        error_message = str(e)
        return HttpResponse(f'{{"status": "error", "message": "{error_message}"}}', content_type="application/json")
def about(request):
    return render(
    request,'about.html')
def Beregin(request):
    try:
        audio_file_path = audio_path_ber
        command = f"afplay {audio_file_path}" 
        os.system(command)
        return HttpResponse('{"status": "success"}', content_type="application/json")
    except Exception as e:
        error_message = str(e)
        return HttpResponse(f'{{"status": "error", "message": "{error_message}"}}', content_type="application/json")
def policy(request):
    return render(
    request,'policy.html')