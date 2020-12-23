create table items
(
	id int not null,
	name text not null,
	incomplete bool not null,
	members bool not null,
	tradeable bool not null,
	tradeable_on_ge bool not null,
	stackable bool not null,
	stacked int,
	noted bool not null,
	noteable bool not null,
	linked_id_item int,
	linked_id_noted int,
	linked_id_placeholder int,
	equipable bool not null,
	equipable_by_player bool not null,
	equipable_weapon bool not null,
	cost int not null,
	lowalch int,
	highalch int,
	weight float,
	buy_limit int,
	quest_item bool not null,
	release_date date,
	duplicate bool not null,
	examine text,
	icon bytea,
	wiki_name text,
	wiki_url text not null,
	attack_stab int,
    attack_slash int,
    attack_crush int,
    attack_magic int,
    attack_ranged int,
    defence_stab int,
    defence_slash int,
    defence_crush int,
    defence_magic int,
    defence_ranged int,
    melee_strength int,
    ranged_strength int,
    magic_damage int,
    prayer int,
    slot text,
    attack_speed int,
    weapon_type text
);

create unique index items_id_uindex
	on items (id);

alter table items
	add constraint items_pk
		primary key (id);

