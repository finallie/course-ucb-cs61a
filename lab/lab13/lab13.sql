CREATE TABLE pizzas AS
  SELECT "Pizzahhh" AS name, 12 AS open, 15 AS close UNION
  SELECT "La Val's"        , 11        , 22          UNION
  SELECT "Sliver"          , 11        , 20          UNION
  SELECT "Cheeseboard"     , 16        , 23          UNION
  SELECT "Emilia's"        , 13        , 18;

CREATE TABLE meals AS
  SELECT "breakfast" AS meal, 11 AS time UNION
  SELECT "lunch"            , 13         UNION
  SELECT "dinner"           , 19         UNION
  SELECT "snack"            , 22;


-- Pizza places that open before 1pm in alphabetical order
CREATE TABLE opening AS
SELECT name from pizzas where open<13 order by name desc;


-- Two meals at the same place
CREATE TABLE double AS
SELECT a.meal||"|"||b.meal||"|"||p.name from meals a,meals b,pizzas p
where b.time-a.time>6 and p.open<=a.time and p.close>=b.time;

