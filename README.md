# Ohtu miniprojekti  
[![CI](https://github.com/MatiasSinisalo/ohtu_mini_projekti/actions/workflows/main.yml/badge.svg)](https://github.com/MatiasSinisalo/ohtu_mini_projekti/actions/workflows/main.yml)

[![codecov](https://codecov.io/gh/MatiasSinisalo/ohtu_mini_projekti/branch/main/graph/badge.svg?token=XP59ESEXZK)](https://codecov.io/gh/MatiasSinisalo/ohtu_mini_projekti)

[Uusin release](https://github.com/MatiasSinisalo/ohtu_mini_projekti/releases
)  
## Dokumentointi  


### Definition of Done  
Testien haaraumakattavuus on 80% *(poisluettuna triviaali koodi)*.  
Robot framework testit on kirjoitettu ja menevät läpi.  
Toinen ohjelmoija on katsonut koodin läpi.  
Github-actions on hyväksynyt koodin.  

[Sprint Backlog](https://docs.google.com/spreadsheets/d/1HfphglHmrU-X_7p_Du5ujbIZPMRQSqTl8imJZZynUK0/edit#gid=0)

[Product Backlog](https://docs.google.com/spreadsheets/d/1R7Q2cNVjgsSZECTlZ_ocQv4pzd5d8XxJI1bs-lg3rlY/edit?usp=sharing)  

[Burndown](https://docs.google.com/spreadsheets/d/1ihpQ4rauSuqUK-_refRsCqEjCJql8XxM8My-ht1BwbY/edit?usp=sharing)  

[CI](https://github.com/MatiasSinisalo/ohtu_mini_projekti/actions/workflows/main.yml)

[Loppuraportti](https://docs.google.com/document/d/1UsmgCjaFYIQD6UBs5ONWaaJUl5HPwjg-VZoeClFq3E4)

### Asennusohjeet

Kloonaa repositorio koneellesi käskyllä

>**git clone https://github.com/MatiasSinisalo/ohtu_mini_projekti**

Tämän jälkeen siirry kloonin juurihakemistoon (kansio, josssa on tiedosto "app.py") ja anna käsky

>**poetry install**

Anna koneen asentaa riippuvuudet, tämän jälkeen siirry hakemistoon "src", sovellus käynnistyy seuraavallilla käskyillä

>**poetry shell**
>
>**flask run**


Sovellus käynnistyy osoitteessa http://127.0.0.1:5000
