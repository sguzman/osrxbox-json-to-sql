import datetime
import json

from typing import Optional


class Weapons:
    def __init__(self,
                 attack_speed: int,
                 weapon_type: str,
                 ):
        self.attack_speed = attack_speed
        self.weapon_type = weapon_type

    def __str__(self):
        return f'Weapons(attack_speed={self.attack_speed}, weapon_type={self.weapon_type})'


class Equipment:
    def __init__(self,
                 attack_stab: int,
                 attack_slash: int,
                 attack_crush: int,
                 attack_magic: int,
                 attack_ranged: int,
                 defence_stab: int,
                 defence_slash: int,
                 defence_crush: int,
                 defence_magic: int,
                 defence_ranged: int,
                 melee_strength: int,
                 ranged_strength: int,
                 magic_damage: int,
                 prayer: int,
                 slot: str,
                 ):
        self.attack_stab = attack_stab
        self.attack_slash = attack_slash
        self.attack_crush = attack_crush
        self.attack_magic = attack_magic
        self.attack_ranged = attack_ranged
        self.defence_stab = defence_stab
        self.defence_slash = defence_slash
        self.defence_crush = defence_crush
        self.defence_magic = defence_magic
        self.defence_ranged = defence_ranged
        self.melee_strength = melee_strength
        self.ranged_strength = ranged_strength
        self.magic_damage = magic_damage
        self.prayer = prayer
        self.slot = slot

    def __str__(self):
        return f'Equipment(attack_stab={self.attack_stab}, attack_slash={self.attack_slash}, attack_crush={self.attack_crush}, attack_magic={self.attack_magic}, attack_ranged={self.attack_ranged}, defence_stab={self.defence_stab}, defence_slash={self.defence_slash}, defence_crush={self.defence_crush}, defence_magic={self.defence_magic}, defence_ranged={self.defence_ranged}, melee_strength={self.melee_strength}, ranged_strength={self.ranged_strength}, magic_damage={self.magic_damage})'


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
                weapon: Optional[Weapons]
                 ):
        self.idd = idd
        self.name = name,
        self.incomplete = incomplete,
        self.members = members,
        self.tradeable = tradeable,
        self.tradeable_on_ge = tradeable_on_ge,
        self.stackable = stackable,
        self.stacked = stacked,
        self.noted = noted,
        self.noteable = noteable,
        self.linked_id_item = linked_id_item,
        self.linked_id_noted = linked_id_noted,
        self.linked_id_placeholder = linked_id_placeholder,
        self.placeholder = placeholder,
        self.equipable = equipable,
        self.equipable_by_player = equipable_by_player,
        self.equipable_weapon = equipable_weapon,
        self.cost = cost,
        self.lowalch = lowalch,
        self.highalch = highalch,
        self.weight = weight,
        self.buy_limit = buy_limit,
        self.quest_item = quest_item,
        self.release_date = release_date,
        self.duplicate = duplicate,
        self.examine = examine,
        self.icon = icon,
        self.wiki_name = wiki_name,
        self.wiki_url = wiki_url,
        self.equipment = equipment,
        self.weapon = weapon

    def __str__(self):
        return f'Item(idd={self.idd},name={self.name}, incomplete={self.incomplete}, members={self.members}, tradeable={self.tradeable}, tradeable_on_ge={self.tradeable_on_ge}, stackable={self.stackable}, stacked={self.stacked}, noted={self.noted}, noteable={self.noteable}, linked_id_item={self.linked_id_item}, linked_id_noted={self.linked_id_noted}, linked_id_placeholder={self.linked_id_placeholder}, placeholder={self.placeholder}, equipable={self.equipable}, equipable_by_player={self.equipable_by_player}, equipable_weapon={self.equipable_weapon}, cost={self.cost}, lowalch={self.lowalch}, highalch={self.highalch}, weight={self.weight}, buy_limit={self.buy_limit}, quest_item={self.quest_item}, release_date={self.release_date}, duplicate={self.duplicate}, examine={self.examine}, icon={self.icon}, wiki_name={self.wiki_name}, wiki_url={self.wiki_url}, {str(self.equipment)}, {str(self.weapon)})'


if __name__ == '__main__':
    with open('./items-complete.json') as f:
        data = json.load(f)
        for key, value in data.items():
            eqp = value['equipment']
            if eqp is not None:
                obj = eqp
                eqp = Equipment(
                    attack_stab=int(obj['attack_stab']),
                    attack_slash=int(obj['attack_slash']),
                    attack_crush=int(obj['attack_crush']),
                    attack_magic=int(obj['attack_magic']),
                    attack_ranged=int(obj['attack_ranged']),
                    defence_stab=int(obj['defence_stab']),
                    defence_slash=int(obj['defence_slash']),
                    defence_crush=int(obj['defence_crush']),
                    defence_magic=int(obj['defence_magic']),
                    defence_ranged=int(obj['defence_ranged']),
                    melee_strength=int(obj['melee_strength']),
                    ranged_strength=int(obj['ranged_strength']),
                    magic_damage=int(obj['magic_damage']),
                    prayer=int(obj['prayer']),
                    slot=obj['slot']
                )

            wep = value['weapon']
            if wep is not None:
                obj = wep
                wep = Weapons(
                    attack_speed=int(obj['attack_speed']),
                    weapon_type=obj['weapon_type']
                )

            item = Item(
                idd=value['id'],
                name=value['name'],
                incomplete=value['incomplete'],
                members=value['members'],
                tradeable=value['tradeable'],
                tradeable_on_ge=value['tradeable_on_ge'],
                stackable=value['stackable'],
                stacked=value['stacked'],
                noted=value['noted'],
                noteable=value['noteable'],
                linked_id_item=value['linked_id_item'],
                linked_id_noted=value['linked_id_noted'],
                linked_id_placeholder=value['linked_id_placeholder'],
                placeholder=value['placeholder'],
                equipable=value['equipable'],
                equipable_by_player=value['equipable_by_player'],
                equipable_weapon=value['equipable_weapon'],
                cost=value['cost'],
                lowalch=value['lowalch'],
                highalch=value['highalch'],
                weight=value['weight'],
                buy_limit=value['buy_limit'],
                quest_item=value['quest_item'],
                release_date=value['release_date'],
                duplicate=value['duplicate'],
                examine=value['examine'],
                icon=value['icon'],
                wiki_name=value['wiki_name'],
                wiki_url=value['wiki_url'],
                equipment=eqp,
                weapon=wep,
            )

            print(item)
