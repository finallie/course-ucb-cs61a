.read data.sql


CREATE TABLE bluedog AS
  SELECT color||"|"||pet from students where color="blue" and pet="dog";

CREATE TABLE bluedog_songs AS
  SELECT color||"|"||pet||"|"||song from students where color="blue" and pet="dog";


CREATE TABLE matchmaker AS
  SELECT s1.pet||"|"||s1.song||"|"||s1.color||"|"||s2.color
  from students as s1, students as s2 where s1.song=s2.song and s1.pet=s2.pet and s1.time<s2.time ;


CREATE TABLE sevens AS
  SELECT s.seven from students s , numbers n where s.time=n.time and s.number=7 and n.'7'="True";


CREATE TABLE smallest_int_having AS
  SELECT 
  min(time)||"|"||smallest
  from students s
  group by smallest
  having count(*)=1;

