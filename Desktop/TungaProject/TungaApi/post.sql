BEGIN;
--
-- Create model Note
--
CREATE TABLE "OnlineNotes_note" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(200) NOT NULL, "story" text NOT NULL, "created_at" datetime NOT NULL);
--
-- Create model Comment
--
CREATE TABLE "OnlineNotes_comment" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "content" text NOT NULL, "created_at" datetime NOT NULL, "note_id" bigint NOT NULL REFERENCES "OnlineNotes_note" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "OnlineNotes_comment_note_id_74a22147" ON "OnlineNotes_comment" ("note_id");
COMMIT;
