# upnqr

Python library for generating payment QR codes according to the Slovenian "UPN QR" standard.


## Specifications

 - [UPN QR Technical standard (English, pdf)](https://www.zbs-giz.si/wp-content/uploads/2021/10/EN_Tehnicni_standard_UPN_QR.pdf)
 - [Bank Association of Slovenia - Standards (English, web)](https://www.zbs-giz.si/en/standards/)
 - [Technical standard with additional files (Slovene, zip)](https://www.zbs-giz.si/wp-content/uploads/2021/07/objava_dokumentacije_UPN_QR-2016-12-15.zip)
 - [Payment reasons list (Slovene, zip)](https://www.zbs-giz.si/wp-content/uploads/2021/07/Sifrant_kod_namenov_placil_javen.zip)
 - [SI payment reference rules (Slovene, pdf)](https://www.zbs-giz.si/wp-content/uploads/2023/12/Pravila-za-oblikovanje-in-uporabo-standardiziranih-referenc-pri-opravljanju-placilnih-storitev-verzija-1.4.pdf)
 - [Bank Association of Slovenia - Standards (Slovene, web)](https://www.zbs-giz.si/standardi-in-prirocniki/)

## Usage

Data preparation:

```python
import upnqr

data = upnqr.Data(
    # Payer / payment sender information
    placnik = upnqr.Placnik(
        ime='Payer Name',
        ulica='Payer Address 1',
        kraj='Payer City'),
    # Payee / payment recipient information
    prejemnik = upnqr.Placnik(
        ime='Payee Name',
        ulica='Payee Address 1',
        kraj='Payee City',
        iban='SI56043020002997963'),
    # Amount (in EUR)
    znesek = 42.00,
    # Payment reason (see payment reasons list)
    koda_namena = 'COST',
    # Description
    namen_placila = 'Namen plačila',
    # Payment deadline
    rok_placila = '2022-05-01',
    # Payment reference (RF or SI - see reference payment rules)
    referenca = 'SI1212345678909'
)

qr = upnqr.make_from_data(data)
```

Generating 

```python
# Raster image
img = upnqr.to_pil(qr)
img.save('out.png')

# Vector image (SVG)
svg = upnqr.to_svg(qr)
with open('out.svg', 'w') as f:
    f.write(svg)

# Vector data (SVG path - for inserting into existing SVG images)
path_spec = upnqr.to_svg_path(qr)
path_el = f'<path d="{path_spec}" fill="#000000"/>'

# Text (for printing in the terminal, uses Unicode box characters for white pixels)
txt = to_text(qr)
print(txt)
```
