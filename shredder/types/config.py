from dataclasses import dataclass

@dataclass
class TableConfig:
    tablename: str
    truncation_percentage: int
    holdout_predecate: str | None = None
    write_preservation_id_to_disk: bool = False
    


@dataclass
class Config:
    root_tables: list[TableConfig]

