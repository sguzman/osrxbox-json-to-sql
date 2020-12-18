import datetime
import json

from typing import Optional


class Equipment


class Item:
    def __init__(self,
                idd: int,
                name: str,
                incomplete: bool,
                members: bool,
                tradeable: bool,
                tradeable_on_ge: bool,
                stackable: bool,
                stacked: Optional[bool],
                noted: bool,
                noteable: bool,
                linked_id_item: int,
                linked_id_noted: Optional[int],
                linked_id_placeholder: Optional[int],
                placeholder: bool,
                equipable: bool,
                equipable_by_player: bool,
                equipable_weapon: bool,
                cost: int,
                lowalch: Optional[int],
                highalch: Optional[int],
                weight: float,
                buy_limit: Optional[int],
                quest_item: bool,
                release_date: datetime.datetime,
                duplicate: bool,
                examine: str,
                icon: bytes,
                wiki_name: str,
                wiki_url: str,
                equipment: Optional[Equipment],
                weapon: Optional[Weapons]):
        ...


if __name__ == '__main__':
    with open('./items-complete.json') as f:
        data = json.load(f)
        for key, value in data.items():
            print(key, value)
