CREATE TABLE user (
  uuid INT PRIMARY KEY,
  name TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  profile_pic TEXT NOT NULL,
  HOURS INT NOT NULL,
  EVENTS TEXT NOT NULL
);
