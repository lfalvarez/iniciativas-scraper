# Scraper de Iniciativas Populares de Norma para la Convención Constituyente
Este proyecto busca tener las Iniciativas Populares de Norma en un spreadsheet para poder estudiarlas.
Se ejecutará en un google actions todos los días.

![Apruebo](https://images.squarespace-cdn.com/content/v1/5c6d8645aadd344a28004478/1583788926277-MC6TRFK44PMA4UNSG2KI/Calca_Constituyente_2.png?format=2500w)

## Si necesitas instalarlo en tu local
Estoy usando python3.9 y scrapy para escrapear.
### 0) Instalar lo que necesites
```
pip install -r requirements.txt
```
### 1) Para ejecutar el scrapeo de los datos tienes que decirle
```
python scraper.py
```
Eso dejará el contenido escrapeado en un archivo llamado `file.csv`.
### Me dí cuenta que mucha gente quiere las iniciativas ordenadas por lo que el segundo paso es ordenarlas
```
python ordena_por_apoyos.py
```
Este paso dejará las propuestas ordenadas por cantidad de apoyos en un archivo llamado `ordenadas.csv`.

### Subir esto a google spreadsheets

Esto es más bien una nota para el yo del futuro, esto lo he necesitado antes.

```
export SHEET_ID='<EL_ID_DE_UN_SPREADSHEET>'
export SERVICE_ACCOUNT_CREDS='<LAS_CREDENCIALES_QUE_DA_GOOGLE_CLOUD>' ## Cómo obtener esto es capítulo aparte

python subidor_a_spreadsheets.py
```
