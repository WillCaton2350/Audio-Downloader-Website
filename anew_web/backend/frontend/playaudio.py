import subprocess

audio_file_path = '/Users/administrator/Desktop/Projects/djangoProjects/anew_web/backend/frontend/media/wav/brake_neck_drumloop.wav'

subprocess.run(["afplay", audio_file_path])
