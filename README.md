# upnqr

[README is also available in English](./README-EN.md)

Python knjižnica za generiranje QR kod za Univerzalni Plačilni Nalog (UPN).

## Specifikacija

 - [Standard in pomožna dokumentacija (zip)](https://www.zbs-giz.si/wp-content/uploads/2021/07/objava_dokumentacije_UPN_QR-2016-12-15.zip)
 - [Seznam kod namenov (zip)](https://www.zbs-giz.si/wp-content/uploads/2021/07/Sifrant_kod_namenov_placil_javen.zip)
 - [Pravila za uporabo referenc SI (pdf)](https://www.zbs-giz.si/wp-content/uploads/2023/12/Pravila-za-oblikovanje-in-uporabo-standardiziranih-referenc-pri-opravljanju-placilnih-storitev-verzija-1.4.pdf)
 - [Združenje Bank Slovenije - Standardi in priročniki (splet)](https://www.zbs-giz.si/standardi-in-prirocniki/)

## Namestitev

```sh
pip install git+https://github.com/franga2000/upnqr.git#egg=upnqr
```

## Uporaba

Priprava podatkov:

```python
import upnqr

data = upnqr.Data(
 placnik = upnqr.Placnik(
        ime='Ime Plačnika',
        ulica='Plačnikova ulica 1',
        kraj='Kraj Plačnika'),
    prejemnik = upnqr.Prejemnik(
        ime='Ime Prejemnika',
        ulica='Prejemnikova ulica 1',
        kraj='Kraj Prejemnika',
        iban='SI56043020002997963'),
    znesek = 42.00,
    koda_namena = 'COST',
    namen_placila = 'Namen plačila',
    rok_placila = '2022-05-01',
    referenca = 'SI1212345678909'
)

qr = upnqr.make_from_data(data)
```

Izpis v različnih oblikah:

```python
# V rastrski obliki (slika)
img = upnqr.to_pil(qr)
img.save('out.png')

# V vektorski obliki (SVG)
svg = upnqr.to_svg(qr)
with open('out.svg', 'w') as f:
    f.write(svg)

# V vektorski obliki (SVG path - za vstavljanje v obstoječ SVG)
path_spec = upnqr.to_svg_path(qr)
path_el = f'<path d="{path_spec}" fill="#000000"/>'

# V besedilni obliki (npr. za izpis v terminalu, uporablja Unicode simbole za bela polja)
txt = to_text(qr)
print(txt)
```
