Steps 
1. Create Station ID List: Read names of all files available at dwd open data,
    extract the station IDs, write to list
2. Use the Station-ID-List to download all related zip files
3. Extract the zip Files
4. Create the Stations-File with geographical meta data in order to locate stations
5. remove stations with ffaulty data
6. clean data by replacing missing values with mean
7. create labels
8. Optional: visualise stations in basemap



Parameter
Die Parameterportfolios der einzelnen Stationen sind unterschiedlich umfangreich. Insgesamt stehen in
produkt*.txt folgende Parameter zur Verfügung:

STATIONS_ID     Stationsidentifikationsnummer
MESS_DATUM      Datum   yyyymmdd
QN_3            Qualitätsniveau der nachfolgenden Spalten
                code siehe Absatz "Qualitätsinformation"
FX              Tagesmaximum Windspitze             m/s
FM              Tagesmittel Windgeschwindigkeit     m/s
QN_4            Qualitätsniveau der nachfolgenden Spalten
RSK             tägliche Niederschlagshöhe mm
RSKF            Niederschlagsform   kein Niederschlag       0
                                    nur Regen (vor 1979)    1
                                    nicht bekannt           4
                                    nur Regen (ab 1979)     6
                                    nur Schnee              7
                                    Regen und Schnee (oder
                                    Schneeregen)            8
SDK             tägliche Sonnenscheindauer  h
SHK_TAG         Tageswert Schneehöhe cm
NM              Tagesmittel des Bedeckungsgrades 1/8
VPM             Tagesmittel des Dampfdruckes hPa
PM              Tagesmittel des Luftdrucks hPa

TMK             Tagesmittel der Temperatur °C
UPM             Tagesmittel der Relativen Feuchte %
TXK             Tagesmaximum der Lufttemperatur in 2m Höhe °C
TNK             Tagesminimum der Lufttemperatur in 2m Höhe °C
TGK             Minimum der Lufttemperatur am Erdboden in 5cm Höhe °C
eor             Ende data record
Fehlwerte sind mit -999 gekennzeichnet. Das Zeitintervall der täglichen Niederschlagshöhe ist als 6 Uhr bis 6
Uhr Folgetag definiert  

PREPARATION OF TRAINING DATA
Folgende Daten werden für den Datensatz verwendet
FEATURES
- Mittlere Tagestemperatur
- Maximale Tagestemperatur
- Minimale Tagestemperatur
- Niederschlagshöhe
- Niederschlagsform
- Luftfeuchtigkeit
- Mittlerer Dampfdruck
LABELS
1 | TEMPERATUR <= 0
2 | TEMPERATUR > 0 bis <= 10
3 | TEMPERATUR > 10 bis <= 20
4 | TEMPERATUR > 20 bis <= 30
5 | TEMPERATUR > 30
6 | NIEDERSCHLAG = 0
7 | NIEDERSCHLAG >= 0 <= 10
8 | NIEDERSCHLAG > 10 <= 100 
9 | NIEDERSCHLAG > 10 <= 20 

