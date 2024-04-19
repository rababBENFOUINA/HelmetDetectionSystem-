import os
import cv2
import shutil
from concurrent.futures import ThreadPoolExecutor

def process_image(image_path):
    frame = cv2.imread(image_path)

    # Réduire la taille de l'image pour accélérer le processus
    resized_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    gray = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)

    # Détection des visages avec des paramètres plus stricts
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(20, 20))

    if len(faces) > 0:
        for i, (x, y, w, h) in enumerate(faces):
            margin = 50
            x_margin = max(0, x - margin)
            y_margin = max(0, y - margin)
            w_margin = w + 2 * margin
            h_margin = h + 2 * margin

            face_image = resized_frame[y_margin:y_margin + h_margin, x_margin:x_margin + w_margin]

            output_path = os.path.join(output_folder, f"{os.path.basename(image_path)}_face_{i}.png")
            cv2.imwrite(output_path, face_image, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])

# Chemin vers le répertoire contenant les images
image_folder = "C:\\Users\\HP\\Documents\\MIT\\Archi\\projet\\sss"

# Créer un dossier pour enregistrer les captures d'écran
output_folder = 'C:\\Users\\HP\\Documents\\MIT\\Archi\\projet\\captures_ecran'
os.makedirs(output_folder, exist_ok=True)

# Vider le contenu du répertoire "captures_ecran" s'il n'est pas vide
if os.listdir(output_folder):
    shutil.rmtree(output_folder)
    os.makedirs(output_folder)

# Charger le classificateur de visage Haarcascades
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Liste pour stocker le chemin de chaque image dans le répertoire
image_paths = [os.path.join(image_folder, img) for img in os.listdir(image_folder) if img.endswith(".png") or img.endswith(".jpg")]

# Utiliser ThreadPoolExecutor pour traiter les images en parallèle
with ThreadPoolExecutor() as executor:
    executor.map(process_image, image_paths)

print("Traitement terminé.")
