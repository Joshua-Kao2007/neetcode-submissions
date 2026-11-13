CREATE TABLE pokemon_types (
    id INTEGER PRIMARY KEY,
    name TEXT,
    weakness TEXT
);

CREATE TABLE pokemon (
    id INTEGER PRIMARY KEY,
    name TEXT,
    type_id INTEGER REFERENCES pokemon_types(id)
);

INSERT INTO pokemon_types (id, name, weakness) VALUES
(1, 'Fire', 'Water'),
(2, 'Water', 'Grass'),
(3, 'Grass', 'Fire'),
(4, 'Electric', 'Ground');

INSERT INTO pokemon (id, name, type_id) VALUES
(4, 'Charmander', 1),
(7, 'Squirtle', 2),
(3, 'Bulbasaur', 3);
-- Do not modify above this line. --

SELECT ptype.name AS type, p.name AS pokemon, ptype.weakness
FROM pokemon_types as ptype
LEFT JOIN pokemon as p
    ON p.type_id = ptype.id
ORDER BY type ASC;

-- TYPE POKEMON WEAKNESS
-- 1    Charmander Water
-- 2    Squirtle.  Grass
-- 3 



