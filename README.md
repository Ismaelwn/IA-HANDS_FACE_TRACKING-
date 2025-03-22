# HAND_EYE_TRACKER

## Description

**HAND_EYE_TRACKER** est une application de vision par ordinateur utilisant **OpenCV** et **MediaPipe** pour détecter et suivre :
- Les mains et leurs mouvements.
- Les visages et la distance entre les yeux.

L'application utilise la webcam en temps réel pour identifier les landmarks des mains et du visage, permettant ainsi des interactions basées sur les gestes.

## Installation

1. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/Ismaelwn/IA-HANDS_FACE_TRACKING.git
   ```
2. **Installer les dépendances** :
   ```bash
   pip install opencv-python mediapipe
   ```
3. **Exécuter le programme** :
   ```bash
   python hand_eye_tracker.py
   ```

## Fonctionnalités

- Détection des mains avec **MediaPipe Hands**.
- Détection des visages avec **MediaPipe FaceMesh**.
- Calcul de la distance entre le pouce et l'index.
- Calcul de la distance entre les yeux.
- Affichage des résultats en temps réel avec OpenCV.
- Possibilité de quitter l'application avec la touche `q`.

## Utilisation

1. Lancer le programme.
2. La webcam s'ouvre et détecte automatiquement le visage et les mains.
3. Les distances entre les doigts et les yeux sont affichées en temps réel.
4. Appuyer sur `q` pour quitter.

