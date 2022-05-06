INSERT INTO categorie (id, niveau, genre) VALUES (1, 'S', 'M');
INSERT INTO categorie (id, niveau, genre) VALUES (2, 'S', 'F');
INSERT INTO categorie (id, niveau, genre) VALUES (3, 'P', 'M');
INSERT INTO categorie (id, niveau, genre) VALUES (4, 'P', 'F');
INSERT INTO categorie (id, niveau, genre) VALUES (5, 'T', 'M');
INSERT INTO categorie (id, niveau, genre) VALUES (6, 'T', 'F');
UPDATE categorie SET niveau = 'S', genre = 'M' WHERE id = 1;