#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

connection = sqlite3.connect('Users.db')

cursor = connection.cursor()

cursor.execute("""

CREATE TABLE [Users] (
	[user_id] integer PRIMARY KEY AUTOINCREMENT NOT NULL,
	[Name] TEXT COLLATE NOCASE,
	[last_option] integer COLLATE NOCASE,
	[Loc_Meterologia] TEXT COLLATE NOCASE,
	[Ids_jornais] TEXT COLLATE NOCASE
);

""")

ccc = cursor.fetchall()
print(ccc)

connection.commit()

cursor.execute("""

PRAGMA table_info(Users);

""")
ccc = cursor.fetchall()
print(ccc)


