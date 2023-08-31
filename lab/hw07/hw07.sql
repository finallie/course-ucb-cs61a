CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT dc.name from parents p,dogs dp,dogs dc
  WHERE p.parent = dp.name AND p.child = dc.name
  order by dp.height desc;


-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT d.name||"|"||s.size,d.name as name,s.size as size from dogs d,sizes s
  WHERE d.height > s.min AND d.height <= s.max;


-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT a.name||" plus "||b.name as names,a.size as size from size_of_dogs a, size_of_dogs b,parents p1,parents p2
  where a.size=b.size and a.name<b.name
  and p1.child=a.name and p2.child=b.name and p1.parent=p2.parent
    order by size;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT "The two siblings, "||names||" have the same size: "||size from siblings;


-- Height range for each fur type where all of the heights differ by no more than 30% from the average height
CREATE TABLE low_variance AS
  SELECT fur||"|"||(max-min) from (SELECT fur,avg(height) as avg,max(height) as max,min(height) as min from dogs group by fur) a
  where (SELECT count(*) from dogs where fur=a.fur and (height<0.7*avg or height>1.3*avg)) = 0
  order by fur
  ;

