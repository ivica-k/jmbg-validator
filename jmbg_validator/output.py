from dataclasses import dataclass, asdict
from json import dumps


@dataclass
class JMBG:
    pol: str
    datum_rodjenja: str
    validan: str
    region: str

    def __str__(self):
        return self.to_text()

    def to_json(self) -> bytes:
        return dumps(asdict(self), ensure_ascii=False).encode("utf-8")

    def to_text(self) -> str:
        return (
            f"Pol: {self.pol.capitalize()}, Validan: {'Da' if self.validan else 'Ne'},"
            f" Datum rođenja: {self.datum_rodjenja}, Region: {self.region}"
        )

    def to_table(self) -> str:
        return (
            f"Pol\t\t\tValidan\t\tDatum rođenja\t\tRegion\n"
            f"{self.pol.capitalize()}\t\t\t{'Da' if self.validan else 'Ne'}\t\t{self.datum_rodjenja}\t\t{self.region}"
        )
