# werkplaats-3-inhaalopdracht-actiontypes


Stappenplan om de applicatie op te starten.

1. Zorg ervoor dat u zich in de map WebApp bevindt. Als u deze map nog niet hebt geopend, kunt u dat doen via uw bestandsbeheer of terminal.

2. Activeer de virtuele omgeving met het volgende commando:

        - Voor Windows PowerShell:

            - bash

            - .\venv\Scripts\activate


        - Voor Windows CMD:

            - cmd

            - venv\Scripts\activate


        - Voor macOS/Linux:

            - bash

            - source venv/bin/activate

3. Vereiste Pakketten Installeren:
    Installeer de benodigde Python-pakketten door het volgende commando uit te voeren:

    bash

    pip install -r requirements.txt

4. Applicatie starten

    Zodra de installatie van de vereisten voltooid is, start u de applicatie met:

    bash

    python app.py

Inloggen op de Applicatie:

Bij het opstarten van de applicatie ziet u een welkomstscherm. U heeft de mogelijkheid om in te loggen als docent of student:

    Inloggen als Docent:
        - Admin Docent: Gebruik het e-mailadres john.doe@hr.nl en het wachtwoord password123.
        - Niet-Admin Docent: Gebruik het e-mailadres jane.smith@hr.nl en het wachtwoord securepass456.

    Inloggen als Student:
        - Vul het studentnummer 2464483 in om in te loggen als student.