from dataclasses import dataclass, asdict
from json import dumps


@dataclass
class JMBG:
    pol: str
    datum_rodjenja: str
    validan: str
    region: str

    def __str__(self):
        return self.to_text_simple()

    def to_json(self) -> str:
        return dumps(asdict(self))

    def to_text_simple(self) -> str:
        return f"Pol: {self.pol.capitalize()}, Validan: {'Da' if self.validan else 'Ne'}," \
               f" Datum rođenja: {self.datum_rodjenja}, Region: {self.region}"

    def to_text_table(self) -> str:
        return f"Pol\t\t\tValidan\t\tDatum rođenja\t\tRegion\n" \
               f"{self.pol.capitalize()}\t\t\t{'Da' if self.validan else 'Ne'}\t\t{self.datum_rodjenja}\t\t{self.region}"

    def to_lambda(self) -> dict:
        return {
            "isBase64Encoded": False,
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": self.to_json(),
        }
