# jmbg-validator
(README in English available below)

Program validira i ispisuje osnovne podatke o [JMBGu](https://sh.wikipedia.org/wiki/Jedinstveni_mati%C4%8Dni_broj_gra%C4%91ana).

## Privatnost
Program **ne čuva** JMBG ni u kakvoj bazi niti ga šalje trećim stranama.

## Instalacija
```
pip install jmbg-validator
```

Dolazi sa alatom za komandnu liniju (CLI) po imenu `jmbg-validator` i Python modulom `jmbg_validator`

## Upotreba
Matični broj `1234567890123` nije validan i koristi se samo kao primer.

### U komandnoj liniji (CLI)
Alat za komandnu liniju se može koristiti na sledeći način:
```
$ jmbg-validator 1234567890123
Pol                     Validan         Datum rođenja           Region
Muški                   Da              11.12.1989.             Vojvodina, Novi Sad

$ jmbg-validator 1234567890123 -o json
{"pol": "ženski", "datum_rodjenja": "06.09.1992.", "validan": true, "region": "Bosna i Hercegovina, Tuzla"}
```

Pregled svih dostupnih opcija:
```
usage: jmbg-validator [-h] [--output {table,text,json}] jmbg

Validira i ispisuje osnovne podatke o JMBGu

positional arguments:
  jmbg                  13 karaktera JMBGa

optional arguments:
  -h, --help            show this help message and exit
  --output {table,text,json}, -o {table,text,json}
```

### Kao Python modul

```
>>> from jmbg_validator import validate
>>> validate("1234567890123")
JMBG(pol='muški', datum_rodjenja='11.12.1989.', validan=True, region='Vojvodina, Novi Sad')
>>> print(validate("1234567890123"))
Pol: Muški, Validan: Da, Datum rođenja: 11.12.1989., Region: Vojvodina, Novi Sad
>>> validate("1234567890123")
>>> rezultat = JMBG(pol='muški', datum_rodjenja='11.12.1989.', validan=True, region='Vojvodina, Novi Sad')
>>> rezultat.validan
True
```

## Za developere
```
$ python -m venv venv
$ source venv/bin/activate
$ pip install -e .
$ pip install -r dev_requirements.txt
```

### Testiranje
```
$ python -m unittest discover
....................................................................
----------------------------------------------------------------------
Ran 68 tests in 0.001s

OK
```

## Licenca

[Mozilla Public License 2.0](https://www.mozilla.org/en-US/MPL/2.0/)
ili
[ukratko](https://www.tldrlegal.com/l/mpl-2.0)

---

# jmbg-validator

This program validates and displays basic [UMCN](https://en.wikipedia.org/wiki/Unique_Master_Citizen_Number) data. UMCN
was/still is in use in former Yugoslav republics as a way to uniquely identify citizens.

## Privacy
This program **does not** store the UMCN and it **does not** share it with 3rd parties.

## Installation
```
pip install jmbg-validator
```

Comes with a CLI tool `jmbg-validator` and a Python module named `jmbg_validator`

## Usage
UMCN `1234567890123` used below is not valid and is used for demonstration purposes only.

### As a CLI tool
CLI tool can be used in this way:
```
$ jmbg-validator 1234567890123
Pol                     Validan         Datum rođenja           Region
Muški                   Da              11.12.1989.             Vojvodina, Novi Sad

$ jmbg-validator 1234567890123 -o json
{"pol": "ženski", "datum_rodjenja": "06.09.1992.", "validan": true, "region": "Bosna i Hercegovina, Tuzla"}
```

Overview of available arguments:
```
usage: jmbg-validator [-h] [--output {table,text,json}] jmbg

Validira i ispisuje osnovne podatke o JMBGu

positional arguments:
  jmbg                  13 karaktera JMBGa

optional arguments:
  -h, --help            show this help message and exit
  --output {table,text,json}, -o {table,text,json}
```

### As a Python module

```
>>> from jmbg_validator import validate
>>> validate("1234567890123")
JMBG(pol='muški', datum_rodjenja='11.12.1989.', validan=True, region='Vojvodina, Novi Sad')
>>> print(validate("1234567890123"))
Pol: Muški, Validan: Da, Datum rođenja: 11.12.1989., Region: Vojvodina, Novi Sad
>>> validate("1234567890123")
>>> rezultat = JMBG(pol='muški', datum_rodjenja='11.12.1989.', validan=True, region='Vojvodina, Novi Sad')
>>> rezultat.validan
True
```

## For developers
```
$ python -m venv venv
$ source venv/bin/activate
$ pip install -e .
$ pip install -r dev_requirements.txt
```

### Running tests
```
$ python -m unittest discover
....................................................................
----------------------------------------------------------------------
Ran 68 tests in 0.001s

OK
```

## License

[Mozilla Public License 2.0](https://www.mozilla.org/en-US/MPL/2.0/)
or
[in short](https://www.tldrlegal.com/l/mpl-2.0)