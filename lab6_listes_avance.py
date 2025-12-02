notes = []

total = 0
nb_notes =len (notes)

if not notes:
    print("Aucune note à traiter.")
    exit()
for note in notes:
    total += note  
moyenne = total / nb_notes
print(f"Moyenne : {moyenne:.2f}")

notes_bonus = [min(note + 1, 20) for note in notes]
print("Notes après bonus :", notes_bonus)

seuil = 12
rattrapage =9
notes_valides = [note for note in notes if note >= seuil]
notes_rattrape=[note for note in notes if note>=rattrapage and note <seuil]
echec =[note for note in notes if note< rattrapage]
print(f"Notes ≥ {seuil} :", notes_valides)
print (f"notes rattraper sont : {notes_rattrape}")
print (f"notes echec sont : {echec}")

top3 = sorted(notes, reverse=True)[:3]
print (f"les trois  meilleures notes sont : {top3}")

moyenne_initiale = sum(notes) / nb_notes
moyenne_bonus = sum(notes_bonus) / len(notes_bonus)
notes_normalisees = [(note / 20) * 100 for note in notes]

lignes = []
lignes.append("=== Rapport des notes ===")
lignes.append(f"Nombre d'étudiants : {nb_notes}")
lignes.append(f"Notes originales : {notes}")
lignes.append(f"Notes après bonus : {notes_bonus}")
lignes.append(f"les trois bonus  Notes  : {top3}")
lignes.append(f"Moyenne initiale : {moyenne_initiale:.2f}")
lignes.append(f"Moyenne après bonus : {moyenne_bonus:.2f}")
lignes.append(f"Notes ≥ {seuil} : {notes_valides} (soit {len(notes_valides)} étudiants)")
lignes.append(f"notes rattraper sont : : {notes_rattrape} (soit {len(notes_valides)} étudiants)")
lignes.append(f"notes echec sont : {echec} (soit {len(notes_valides)} étudiants)")
lignes.append("Détails par étudiant :")
lignes.append(f"notes_normalisees est  : {notes_normalisees}")

for index, note in enumerate(notes, start=1):
    bonus = notes_bonus[index - 1]
    lignes.append(f"  Étudiant {index:02d} — note {note:>5.2f} → bonus {bonus:>5.2f}")

rapport = "\n".join(lignes)
print(rapport)

with open("rapport_notes.txt", "w", encoding="utf-8") as f:
    f.write(rapport)