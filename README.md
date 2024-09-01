# werkplaats-3-inhaalopdracht-actiontypes


## Stappenplan om de applicatie op te starten:

1. Zorg ervoor dat u zich in de map WebApp bevindt. Als u deze map nog niet hebt geopend, kunt u dat doen via uw bestandsbeheer of terminal.

2. Maak een virtuele omgeving aan met het volgende commando:

    - `python -m venv venv`

    - Voor instalaties met python 2 moet het python 3 commando gebruikt

        - `python3 -m venv venv`

3. Activeer de virtuele omgeving met het volgende commando:

    - Voor Windows PowerShell:

        - `.\venv\Scripts\activate`


    - Voor Windows CMD:

        - `venv\Scripts\activate`


    - Voor macOS/Linux:

        - `source venv/Scripts/activate`

4. Vereiste Pakketten Installeren:
    Installeer de benodigde Python-pakketten door het volgende commando uit te voeren:

   - `pip install -r requirements.txt`

5. Start de MySql docker containter met het volgende commando

    - `docker run --name actiontypes_wp3 -e MYSQL_ROOT_PASSWORD=actiontypes_wp3 -d -p 3307:3306 mysql:8`

6. Als de docker aanstaat, voeg dan de databasestructuur en data voor in de database toe. Dit kunt u doen door de volgende commando's te runnen:
    - `python  ./database_scripts/build_database.py`
    - `python  ./database_scripts/import_database.py`


6. Applicatie starten

    Zodra de installatie van de vereisten voltooid is, start u de applicatie met:

    - `python app.py`

## Inloggen op de Applicatie:

Bij het opstarten van de applicatie ziet u een welkomstscherm. U heeft de mogelijkheid om in te loggen als docent of student:

    Inloggen als Docent:
        - Admin Docent: Gebruik het e-mailadres john.doe@hr.nl en het wachtwoord password123.
        - Niet-Admin Docent: Gebruik het e-mailadres jane.smith@hr.nl en het wachtwoord securepass456.

    Inloggen als Student:
        - Vul het studentnummer 2464483 in om in te loggen als student.