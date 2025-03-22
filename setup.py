import cv2
import mediapipe as mp
import math

# Initialiser MediaPipe Hands et FaceMesh
mp_hands = mp.solutions.hands
mp_face_mesh = mp.solutions.face_mesh
mp_draw = mp.solutions.drawing_utils

# Détection des mains et du visage avec des paramètres améliorés
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Fonction pour calculer la distance entre deux points
def calculate_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

# Ouvrir une seule fois la caméra
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Erreur : Impossible d'ouvrir la caméra")
    exit()

while True:
    # Lire l'image depuis la caméra
    ret, frame = cap.read()
    if not ret:
        print("Erreur de lecture de la caméra")
        break

    # Convertir l'image en RGB (nécessaire pour MediaPipe)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Détection des mains
    hand_results = hands.process(rgb_frame)

    # Détection du visage
    face_results = face_mesh.process(rgb_frame)

    # Traitement des mains détectées
    if hand_results.multi_hand_landmarks:
        for landmarks in hand_results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

            # Extraire les coordonnées des doigts (ex: index et pouce)
            x1, y1 = int(landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * frame.shape[1]), int(landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * frame.shape[0])
            x2, y2 = int(landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x * frame.shape[1]), int(landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y * frame.shape[0])

            # Calculer et afficher la distance entre index et pouce
            distance = calculate_distance((x1, y1), (x2, y2))
            cv2.putText(frame, f"Main: {int(distance)} px", (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Traitement du visage détecté
    if face_results.multi_face_landmarks:
        for face_landmarks in face_results.multi_face_landmarks:
            mp_draw.draw_landmarks(frame, face_landmarks, mp_face_mesh.FACEMESH_TESSELATION)

            # Indices des yeux (coins externes)
            left_eye = 33
            right_eye = 263

            # Extraire les coordonnées des yeux
            x1, y1 = int(face_landmarks.landmark[left_eye].x * frame.shape[1]), int(face_landmarks.landmark[left_eye].y * frame.shape[0])
            x2, y2 = int(face_landmarks.landmark[right_eye].x * frame.shape[1]), int(face_landmarks.landmark[right_eye].y * frame.shape[0])

            # Calculer et afficher la distance entre les yeux
            distance = calculate_distance((x1, y1), (x2, y2))
            cv2.putText(frame, f"Visage: {int(distance)} px", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Afficher l'image avec les résultats
    cv2.imshow("Détection Mains et Visage", frame)

    # Quitter avec 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer la caméra et fermer les fenêtres
cap.release()
cv2.destroyAllWindows()
