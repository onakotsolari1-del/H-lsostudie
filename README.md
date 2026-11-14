# Hälsostudie - Del 1
**Kurs:** Pythonprogrammering och statistisk dataanalys  
**Student:** Ona Kotsolari  
**Python-version:** Python 3.13.15  

## Introduktion
Du är dataanalytiker på ett forskningsinstitut. Du har fått tillgång till data från en hälsostudie med information om deltagarnas ålder, kön, vikt, längd, blodtryck, kolesterolnivå, rökvanor och om de har en viss sjukdom.

Din uppgift är att analysera datan i Python och presentera dina resultat i en Jupyter Notebook (`halsostudie.ipynb`).

### Dataset (CSV): `health_study_dataset.csv`
Kolumner:
* `age` (år)
* `sex` (M/F)
* `height` (cm)
* `weight` (kg)
* `systolic_bp` (mmHg)
* `cholesterol` (mmol/L)
* `smoker` (Yes/No)
* `disease` (0/1)

---

## Del 1 - Grundläggande analys och statistik

### För G ska du göra:
1. **Beskrivande analys:**
   * Räkna ut medel, median, min och max för: `age`, `weight`, `height`, `systolic_bp`, `cholesterol`.
2. **Visualiseringar:**
   * Skapa minst 3 olika grafer (t.ex. histogram över blodtryck, boxplot över vikt per kön, stapeldiagram över andelen rökare).
3. **Simulering kopplad till caset (använd numpy.random + seed):**
   * Beräkna andelen personer i datasetet som har sjukdomen.
   * Använd numpy för att simulera 1000 slumpade personer med samma sannolikhet för sjukdom.
   * Jämför den simulerade andelen med den verkliga andelen i datasetet.
4. **Konfidensintervall:**
   * Beräkna ett konfidensintervall för medelvärdet av `systolic_bp` (t.ex. med normalapproximation eller bootstrap).
5. **Hypotesprövning:**
   * Testa hypotesen: *"Rökare har högre medel-blodtryck än icke-rökare."*
   * Förklara kort resultatet i en markdown-ruta.

### För VG ska du även göra:
* Beräkna konfidensintervallet med **två olika metoder** (t.ex. normalapproximation och bootstrap) och jämför resultaten.
* Gör en simulering för att undersöka hur säkert ditt hypotestest är (**power**).
* Motivera dina metodval i markdown och hänvisa till dokumentation eller annan källa.

---

## Reproducerbarhet & Struktur
* Kör **Restart & Run All** innan inläμning (notebooken ska gå från topp till botten utan fel).
* Läs data med en relativ sökväg (`data/health_study_dataset.csv`).
* Sätt en slump-seed i början: `import numpy as np; np.random.seed(42)`.
* `.venv` är undantaget via `.gitignore`.
