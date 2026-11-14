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
   * Testa hypotesen: *"Rökare har högre medel-blodtryck än icke-rökare."
   * Använd en av metoderna vi gått igenom (t.ex. bootstrap eller enkel t-test-funktion).
   * Förklara kort resultatet i en markdown-ruta.

### För VG ska du även göra:
* Beräkna konfidensintervallet med **två olika metoder** (t.ex. normalapproximation och bootstrap) och jämför resultaten.
* Gör en simulering för att undersöka hur säkert ditt hypotestest är (**power**).
* Motivera dina metodval i markdown och hänvisa till dokumentation eller annan källa.
---

## Del 2 – Fördjupning och pipeline

### För G ska du göra:
* **Strukturera koden:**
  * Flytta delar av din kod från del 1 till funktioner och moduler.
  * Skapa minst en klass (t.ex. `HealthAnalyzer`) som kan utföra någon del av analysen (t.ex. beräkna statistik eller rita grafer).
* **Linjär algebra i praktiken:**
  * Använd numpy eller scikit-learn för en analys som bygger på matriser/vektorer.
  * Exempel: En enkel linjär regression för att förutsäga blodtryck från ålder eller vikt, eller PCA för att hitta mönster i datan.
* **Utökad analys och visualisering:**
  * Lägg till minst en ny analys eller graf som ger en djupare förståelse (t.ex. relationen mellan blodtryck och ålder, eller sjukdomsförekomst per kön).
* **Dokumentation:**
  * Skriv docstrings till dina funktioner/klasser.
  * Använd markdown-rutor för att förklara vad du gör och varför.

### För VG ska du även göra (Del 2):
* Bygg en mer utvecklad klass som kan hantera flera olika analyser eller visualiseringar.
* Använd en mer avancerad metod (t.ex. multipel regression) eller en extra visualisering som tydligt förklarar resultatet.
* Motivera dina metodval i markdown och hänvisa till dokumentation eller annan källa.

---

## Betygsättning & Sammanfattning
* **G =** Du följer instruktionerna och visar att du behärskar alla moment vi gått igenom på kursen.
* **VG =** Du går längre än kursinnehållet, jämför metoder, gör extra simuleringar och motiverar dina val med väl underbyggda resonemang.

---

## Reproducerbarhet
* Kör **Restart & Run All** innan inlämning (notebooken ska gå från topp till botten utan fel).
* Läs data med en relativ sökväg (`data/health_study_dataset.csv`).
* Sätt en slump-seed i början: `import numpy as np; np.random.seed(42)`.
* Lägg till en `requirements.txt` genom att köra: `python -m pip freeze > requirements.txt` i terminalen.
* Skriv i README.md vilken Python-version du använder (t.ex. Python 3.13.15).
* *Kom ihåg att lägga `.venv` i `.gitignore` så att den inte råkar pushas upp på github.*
---

## Reproducerbarhet & Struktur
* Kör **Restart & Run All** innan inläμning (notebooken ska gå från topp till botten utan fel).
* Läs data med en relativ sökväg (`data/health_study_dataset.csv`).
* Sätt en slump-seed i början: `import numpy as np; np.random.seed(42)`.
* `.venv` är undantaget via `.gitignore`.
