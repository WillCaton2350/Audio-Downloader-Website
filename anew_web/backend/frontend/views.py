from django.shortcuts import render
from django.http import HttpResponse
import os

def index(request):
    return render(request,'index.html')
def drums(request):
    return render(request,'drums.html')
def bass(request):
    return render(request,'bass.html')
def vox(request):
    return render(request,'vox.html')
def about(request):
    return render(request,'about.html')
def policy(request):
    return render(request,'policy.html')
def play_audio(request):
    try:
        audio_file_path = '/Users/administrator/Desktop/Projects/djangoProjects/anew_web/backend/frontend/static/mp3/brake_neck_drumloop.mp3'
        command = f"afplay {audio_file_path}" 
        os.system(command)
        return HttpResponse('{"status": "success"}', content_type="application/json")
    except Exception as e:
        error_message = str(e)
        return HttpResponse(f'{{"status": "error", "message": "{error_message}"}}', content_type="application/json")
def play_laidback(request):
    try:
        audio_file_path = '/Users/administrator/Desktop/Projects/djangoProjects/anew_web/backend/frontend/static/mp3/laidback_drum_and_bass_beat_40bpm.mp3'
        command = f"afplay {audio_file_path}" 
        os.system(command)
        return HttpResponse('{"status": "success"}', content_type="application/json")
    except Exception as e:
        error_message = str(e)
        return HttpResponse(f'{{"status": "error", "message": "{error_message}"}}', content_type="application/json")
def pandas(request):
    try:
        audio_file_path = '/Users/administrator/Desktop/Projects/djangoProjects/anew_web/backend/frontend/static/mp3/Pandos.mp3'
        command = f"afplay {audio_file_path}" 
        os.system(command)
        return HttpResponse('{"status": "success"}', content_type="application/json")
    except Exception as e:
        error_message = str(e)
        return HttpResponse(f'{{"status": "error", "message": "{error_message}"}}', content_type="application/json")
def afrobeat(request):
    try:
        audio_file_path = '/Users/administrator/Desktop/Projects/djangoProjects/anew_web/backend/frontend/static/mp3/Soubbin.mp3'
        command = f"afplay {audio_file_path}" 
        os.system(command)
        return HttpResponse('{"status": "success"}', content_type="application/json")
    except Exception as e:
        error_message = str(e)
        return HttpResponse(f'{{"status": "error", "message": "{error_message}"}}', content_type="application/json")
def tera(request):
    try:
        audio_file_path = '/Users/administrator/Desktop/Projects/djangoProjects/anew_web/backend/frontend/static/mp3/Tera.mp3'
        command = f"afplay {audio_file_path}" 
        os.system(command)
        return HttpResponse('{"status": "success"}', content_type="application/json")
    except Exception as e:
        error_message = str(e)
        return HttpResponse(f'{{"status": "error", "message": "{error_message}"}}', content_type="application/json")
def Beregin(request):
    try:
        audio_file_path = '/Users/administrator/Desktop/Projects/djangoProjects/anew_web/backend/frontend/static/mp3/Beregin.mp3'
        command = f"afplay {audio_file_path}" 
        os.system(command)
        return HttpResponse('{"status": "success"}', content_type="application/json")
    except Exception as e:
        error_message = str(e)
        return HttpResponse(f'{{"status": "error", "message": "{error_message}"}}', content_type="application/json")