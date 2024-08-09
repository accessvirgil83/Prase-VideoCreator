import platform
import os
import requests
import zipfile
import tarfile
import shutil

def download_ffmpeg():
    system = platform.system()
    arch = platform.architecture()[0]

    # Сформировать URL для загрузки
    if system == "Windows":
        if arch == "64bit":
            url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
        else:
            url = "https://github.com/sudo-nautilus/FFmpeg-Builds-Win32/releases/download/latest/ffmpeg-master-latest-win32-gpl.zip"
    elif system == "Darwin":  # macOS
        url = "https://ffmpeg.zeranoe.com/builds/macosx/static/ffmpeg-latest-macosx-static.zip"
    elif system == "Linux":
        if arch == "64bit":
            url = "https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-$(uname -m).tar.xz"
        else:
            print("Не поддерживается 32-битная версия Linux.")
            return
    else:
        print("Операционная система не поддерживается. обратитесь за подробностями на официальный сайт ffmpeg")
        return

    # Загрузка FFmpeg
    print(f"Загрузка FFmpeg с {url}...")
    response = requests.get(url)
    
    # Проверяем успешность загрузки
    if response.status_code != 200:
        print("Ошибка загрузки FFmpeg.")
        return

    # Сохранение загруженного файла
    filename = url.split("/")[-1]
    with open(filename, "wb") as file:
        file.write(response.content)

    print(f"FFmpeg загружен как {filename}.")

    # Распаковка, если это zip или tar
    if filename.endswith(".zip"):
        print("Распаковка ZIP файла...")
        with zipfile.ZipFile(filename, 'r') as zip_ref:
            zip_ref.extractall(".")
    elif filename.endswith(".tar.xz"):
        print("Распаковка TAR.XZ файла...")
        with tarfile.open(filename, 'r:xz') as tar_ref:
            tar_ref.extractall(".")

    print("FFmpeg загружен и распакован.")


if __name__ == "__main__":
    download_ffmpeg()
    shutil.copyfile('ffmpeg-7.0.2-essentials_build/bin/ffmpeg.exe ffmpeg.exe')