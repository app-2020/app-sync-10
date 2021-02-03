-- SCHEMA

CREATE TABLE "users" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"username"	TEXT NOT NULL UNIQUE,
	"email"	TEXT NOT NULL UNIQUE
)

CREATE TABLE "tweets" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"user_id"	INTEGER,
	"tweet"	TEXT NOT NULL,
	FOREIGN KEY("user_id") REFERENCES "users"("id") ON DELETE SET NULL
)

-- DATA

insert into users(username, email)
values("pepegar", "pepe@ie.edu");

insert into users(username, email)
values("other", "someone@else.com");

insert into users(username, email)
values("last", "last@else.com");

insert into tweets(tweet, user_id)
values
  ("This is my first tweet", 1),
  ("OMG, I'm tweeting!", 1);
