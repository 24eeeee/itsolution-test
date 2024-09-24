import os.path
from datetime import datetime

from django.shortcuts import render
from django.http import FileResponse
from server.settings import BASE_DIR

from utils.video import get_video
from runstring_app.models import Request


def runtext(request):
    path = os.path.join(BASE_DIR, 'video_storage')
    message = request.GET['message']
    file_info = get_video(message, path)
    req = Request(
        message=message,
        timestamp=datetime.now()
    )
    req.save()
    return FileResponse(open(file_info['path'], "rb"), as_attachment=True)
