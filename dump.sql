BEGIN TRANSACTION;
CREATE TABLE PhoneBook(Name text, PhoneNum text);
INSERT INTO "PhoneBook" VALUES('derick','010-1111');
INSERT INTO "PhoneBook" VALUES('gildong','010-222');
INSERT INTO "PhoneBook" VALUES('tom','010-123');
INSERT INTO "PhoneBook" VALUES('dsp','010-456');
COMMIT;
