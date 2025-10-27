import cv2
import numpy as np

# Fonction principale
def detect_red_objects():
    # Accéder à la caméra
    cap = cv2.VideoCapture(0)

    while True:
        # Lire une image de la caméra
        ret, frame = cap.read()
        if not ret:
            break

        # Convertir l'image en espace HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        #_________________ROUGE_____________________
        # # Définir les limites de la couleur rouge en HSV
        # lower_red1 = np.array([0, 120, 70])
        # upper_red1 = np.array([10, 255, 255])
        # lower_red2 = np.array([170, 120, 70])
        # upper_red2 = np.array([180, 255, 255])

        # # Seuil pour détecter la couleur rouge
        # mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
        # mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
        # mask = mask1 + mask2

        #_________________BLEU_____________________
        # Définir les limites pour la couleur bleue
        lower_blue = np.array([100, 150, 0])
        upper_blue = np.array([140, 255, 255])
        
        # Seuil pour détecter la couleur bleue
        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        #_________________VERT_____________________
        # Définir les limites pour la couleur verte
        # lower_green = np.array([36, 100, 100])
        # upper_green = np.array([70, 255, 255])
        
        # # Seuil pour détecter la couleur verte
        # mask = cv2.inRange(hsv, lower_green, upper_green)


        # Nettoyer l'image avec des opérations morphologiques
        kernel = np.ones((5, 5), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

        # Trouver les contours des objets rouges
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Annoter chaque objet rouge
        for i, contour in enumerate(contours):
            # Obtenir un rectangle englobant pour chaque contour
            x, y, w, h = cv2.boundingRect(contour)
            if cv2.contourArea(contour) > 500:  # Filtrer les petits objets
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                #cv2.putText(frame, f"red {i+1}", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                cv2.putText(frame, f"blue {i+1}", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
                #cv2.putText(frame, f"Green {i+1}", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        # Afficher l'image annotée
        #cv2.imshow('Red Object Detection', frame)
        cv2.imshow('Blue Object Detection', frame)
        #cv2.imshow('Green Object Detection', frame)

        # Quitter avec la touche 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Libérer les ressources
    cap.release()
    cv2.destroyAllWindows()

# Exécuter la fonction
detect_red_objects()

