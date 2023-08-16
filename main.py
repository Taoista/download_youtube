import os
import yt_dlp as youtube_dl

# Función para mostrar el progreso de la descarga
def show_progress_bar(d):
    if d['status'] == 'downloading':
        total_size = d.get('total_bytes')
        downloaded = d.get('downloaded_bytes')
        if total_size and downloaded:
            percentage = (downloaded / total_size) * 100
            print(f"Descargando: {percentage:.2f}% completado", end='\r')

# URL del video de YouTube
video_url = 'https://www.youtube.com/watch?v=vs9rORSG_gE'

# Directorio de descarga
download_directory = 'download_video'

# Crear la carpeta si no existe
if not os.path.exists(download_directory):
    os.makedirs(download_directory)

# Opciones para la descarga
ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',  # Elige el mejor formato disponible
    'progress_hooks': [show_progress_bar],  # Función para mostrar el progreso
    'outtmpl': os.path.join(download_directory, '%(title)s.%(ext)s'),  # Nombre del archivo de salida
}

# Descargar el video con yt-dlp
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])

print(f'\nEl video ha sido descargado en la carpeta "{download_directory}"')
