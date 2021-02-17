# jmbg-validator

Program validira i ispisuje osnovne podatke o [JMBGu](https://sh.wikipedia.org/wiki/Jedinstveni_mati%C4%8Dni_broj_gra%C4%91ana).

## Privatnost
Program **ne čuva** JMBG ni u kakvoj bazi niti ga šalje trećim stranama.

## Instalacija
```
pip install jmbg-validator
```

Dolazi sa alatom za komandnu liniju po imenu `jmbg-validator` i Python modulom `jmbg_validator`

## Upotreba
Matični broj "1234567890123" nije validan i koristi se samo kao primer.

### Komandna linija
Alat za komandnu liniju se može koristiti na sledeći način:
```
$ jmbg-validator 1234567890123
Pol                     Validan         Datum rođenja           Region
Muški                   Da              11.12.1989.             Vojvodina, Novi Sad
```

Pregled svih opcija:
```
usage: jmbg-validator [-h] [--output {table,simple,json,lambda}] jmbg

Validira i ispisuje osnovne podatke o JMBGu

positional arguments:
  jmbg                  13 karaktera JMBGa

optional arguments:
  -h, --help            show this help message and exit
  --output {table,simple,json,lambda}, -o {table,simple,json,lambda}

```

### Modul

```
>>> from jmbg_validator import validate
>>> validate("1234567890123")
JMBG(pol='muški', datum_rodjenja='11.12.1989.', validan=True, region='Vojvodina, Novi Sad')
>>> print(validate("1234567890123"))
Pol: Muški, Validan: Da, Datum rođenja: 11.12.1989., Region: Vojvodina, Novi Sad
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

