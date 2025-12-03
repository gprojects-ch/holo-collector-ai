Ich habe das so verstanden:
1. Phase
    - habe 864 vershiedene Bilder mit verschiedene Posen von Minifiguren gemacht
    - Alle haben das Label "Minifigur"

So versteht das Yolo Model, dass alle diese Bilder Minifiguren darstellen.

2. Phase
    - brauche von jeder Figur 2-4 Bilder von ca 1454 MInifiguren, front, back und eventuell seite da manchmal print
    - Dabei wird jede Figur einer Klasse zugeordnet
    - Hoth, Luke Skywalker, Darth Vader, Stormtrooper, etc.
    - Hier figuren nur noch stehend

3. Phase
    - Hier parts erkennen
    - z.B. Kopf, Torso, Beine, Zubehör (Blaster, Lichtschwert, etc)
    - dabei gibt es die Klassen welche auch in der DB sind
    - Ein Fullbody Bild der Figur und dann verschiedene Retangle, weiss nicht ob mir hier das Model helfen kann, denke nicht> manuell retangle pflegen
  
4. Phase
   - Hier geht es nur um beschädigte elemente(parts)
   - Bilder von einzelnen oder Fullbody und dann retangle mit Klasse?
   - was sonst noch?

das würde dann für mich das bedeuten:
LABLES BAUM [Basis, klassentyp, Klassenpart, Klassendefekt]
Minifigur
Minifigur>Darth_Vader
Minifigur>Darth_Vader>head_x1,helm_x1,torso_x1,legs_x1
Minifigur>Boba_Fett
Minifigur>Boba_Fett>head_x2,helm_x2,torso_x2,legs_x2

Einzelteile detection von schäden ist mir noch unklar wie das gehen soll, einzelne teile fotografieren oder besser Fullbody und dann da einzelne retangle setzten, noch keine ahnung was besser ist oder wie das funktionier.

Nun zu meiner grossen Frage! Wohin kommt nun die sw_nummer soll das aus der db berechnet werden wenn ich es wie oben mache, oder eben die sw_nummer zuweisen und trainieren? Ist diese Strategie oben korrekt komplett falsch oder unbrauchbar, was kann ich verbessern.

Bitte sei streng beim feedback auf diese Strategie und wie es besser gemacht werden kann, also eben richtig machen ohne mir irgendetwas zu erzählen. es ist wichtig das diese KI für minifiguren richtig funktioniert ansonsten werde ich meine Konkurent nie abhängen und zusätzlich habe ich das richtig gelernt.

Noch eine Frage wie Viele Bilder brauche ich von jeder figur genau ist es immer noch wichtich 40 -60 Biler von jeder zu haben in den Phasen nach 1?



build docker:
TRAINER
training>Docker>
docker build -t holo-collector-yolo-cpu:0.0.1 .
INTERFERENZ
root
docker build -t ghcr.io/gprojects-ch/holo-collector-ai-cpu .