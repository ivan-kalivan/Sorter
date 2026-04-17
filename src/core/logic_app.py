import os
import shutil
from pathlib import Path

#Правила сортировки
rules = {
    'documents': ['.pdf', '.docx', '.txt', '.xlsx', '.doc', '.pptx', 'ppt', '.key', '.pages', '.numbers', '.rtf', '.rtfd', '.csv'],
    'images': ['.jpg', '.jpeg', '.png', '.webp', '.gif', '.tiff', '.bmp', '.avif'],
    'distributives': ['.exe', '.pkg', '.dmg', '.deb', '.msi'],
    'archives': ['.zip', '.rar', '.7z', '.tar', '.tar.gz', '.tgz'],
    'videos': ['.mp4', '.mov', '.mkv', '.avi', '.wmv', '.m4v', '.mpeg4', '.mpg', '.mpeg'],
    'audios': ['.mp3', '.wav', '.aac', 'flac']
}

#Сортировка