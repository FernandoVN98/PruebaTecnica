CREATE (TheMatrix:Movie {id:0, title:'The Matrix',genre:'Sci-Fi', released:1999})
CREATE (FightClub:Movie {id:1, title:'Fight Club',genre:'Action', released:1999})
CREATE (TheGodfather:Movie {id:2, title:'The Godfather',genre:'Crime', released:1972})
CREATE (TheGodfather2:Movie {id:3, title:'The Godfather II',genre:'Crime', released:1999})
CREATE (TheGodfather3:Movie {id:4, title:'The Godfather III',genre:'Crime', released:1999})
CREATE (TheDarkKnight:Movie {id:5, title:'The Dark Knight',genre:'Action', released:2007})
CREATE (BatmanBegins:Movie {id:6, title:'Batman Begins',genre:'Action', released:2005})
CREATE (BenjaminButton:Movie {id:7, title:'The Curious Case of Benjamin Button',genre:'Drama', released:2008})
CREATE (IBastards:Movie {id:8, title:'Inglourious Basterds',genre:'Action', released:2009})
CREATE (PulpFiction:Movie {id:9, title:'Pulp Fiction ',genre:'Drama', released:2009})

CREATE (Keanu:Actor {id:0, name:'Keanu Reeves', born:1964})
CREATE (BradPitt:Actor {id:1, name:'Brad Pitt', born:1963})
CREATE (MarlonBrando:Actor {id:2, name:'Marlon Brando', born:1924})
CREATE (AlPacino:Actor {id:3, name:'Al Pacino', born:1940})
CREATE (JaredLeto:Actor {id:4, name:'Jared Leto', born:1971})
CREATE (ChrisBale:Actor {id:5, name:'Christian Bale', born:1964})
CREATE (UmaThurman:Actor {id:6, name:'Uma Thurman', born:1970})

CREATE (FFCoppola:Director {id:0, name:'Francis Ford Coppola', born:1939})
CREATE (DavidFincher:Director {id:1,name:'David Fincher', born:1962})
CREATE (AndyW:Director {id:2,name:'Andy Wachowski', born:1967})
CREATE (LanaW:Director {id:3,name:'Lana Wachowski', born:1965})
CREATE (ChrisNolan:Director {id:4,name:'Christopher Nolan', born:1970})
CREATE (Tarantino:Director {id:5,name:'Quentin Tarantino', born:1963})

CREATE (Hollywood:Industry {id:0, name:'Hollywood', money:'550 mill€'})
CREATE (Paris:Industry {id:1, name:'Paris', money:'100 mill€'})
CREATE (Beijing:Industry {id:2, name:'Beijing', money:'300 mill€'})



CREATE (Usuario1:User {id:0,name:'Fer1', born:1998})
CREATE (Usuario2:User {id:1,name:'Fer2', born:1988})
CREATE (Usuario3:User {id:2,name:'Fer3', born:1968})
CREATE (Usuario4:User {id:3,name:'Fer4', born:1968})

CREATE
  (TheMatrix)-[:WASPRODUCEDBY]->(Hollywood)
CREATE
  (TheGodfather)-[:WASPRODUCEDBY]->(Hollywood)
CREATE
  (TheGodfather2)-[:WASPRODUCEDBY]->(Hollywood)
CREATE
  (TheGodfather3)-[:WASPRODUCEDBY]->(Hollywood)
CREATE
  (TheMatrix)-[:WASPRODUCEDBY]->(Paris)
CREATE
  (TheGodfather)-[:WASPRODUCEDBY]->(Beijing)
CREATE
  (FightClub)-[:WASPRODUCEDBY]->(Paris)
CREATE
  (TheDarkKnight)-[:WASPRODUCEDBY]->(Paris)
CREATE
  (BatmanBegins)-[:WASPRODUCEDBY]->(Paris)
CREATE
  (BenjaminButton)-[:WASPRODUCEDBY]->(Paris)
CREATE
  (TheDarkKnight)-[:WASPRODUCEDBY]->(Beijing)
CREATE
  (IBastards)-[:WASPRODUCEDBY]->(Beijing)
CREATE
  (PulpFiction)-[:WASPRODUCEDBY]->(Beijing)


CREATE
  (Keanu)-[:ACTED_IN {roles:['Neo']}]->(TheMatrix),
  (AndyW)-[:DIRECTED]->(TheMatrix),
  (LanaW)-[:DIRECTED]->(TheMatrix)
CREATE
  (BradPitt)-[:ACTED_IN {roles:['Tyler Durden']}]->(FightClub),
  (JaredLeto)-[:ACTED_IN {roles:['Angel Face']}]->(FightClub),
  (DavidFincher)-[:DIRECTED]->(FightClub)
CREATE
  (MarlonBrando)-[:ACTED_IN {roles:['Vito Corleone']}]->(TheGodfather),
  (AlPacino)-[:ACTED_IN {roles:['"Mike" Corleone']}]->(TheGodfather),
  (FFCoppola)-[:DIRECTED]->(TheGodfather)
CREATE
  (AlPacino)-[:ACTED_IN {roles:['"Mike" Corleone']}]->(TheGodfather2),
  (FFCoppola)-[:DIRECTED]->(TheGodfather2)
CREATE
  (AlPacino)-[:ACTED_IN {roles:['"Mike" Corleone']}]->(TheGodfather3),
  (FFCoppola)-[:DIRECTED]->(TheGodfather3)
CREATE
  (ChrisBale)-[:ACTED_IN {roles:['Batman']}]->(TheDarkKnight),
  (ChrisNolan)-[:DIRECTED]->(TheDarkKnight)
CREATE
  (ChrisBale)-[:ACTED_IN {roles:['Batman']}]->(BatmanBegins),
  (ChrisNolan)-[:DIRECTED]->(BatmanBegins)
CREATE
  (BradPitt)-[:ACTED_IN {roles:['Benjamin Button']}]->(BenjaminButton),
  (DavidFincher)-[:DIRECTED]->(BenjaminButton)
CREATE
  (BradPitt)-[:ACTED_IN {roles:['El apache']}]->(IBastards),
  (Tarantino)-[:DIRECTED]->(IBastards)
CREATE
  (UmaThurman)-[:ACTED_IN {roles:['Mia Wallace']}]->(PulpFiction),
  (Tarantino)-[:DIRECTED]->(PulpFiction)
CREATE
  (Usuario1)-[:HASPUNCTUATED {score:0.5}]->(PulpFiction)
CREATE
  (Usuario1)-[:HASPUNCTUATED {score:1.6}]->(BatmanBegins)
CREATE
  (Usuario1)-[:HASPUNCTUATED {score:3.2}]->(TheDarkKnight)
CREATE
  (Usuario1)-[:HASPUNCTUATED {score:3.1}]->(IBastards)
CREATE
  (Usuario1)-[:HASPUNCTUATED {score:5.0}]->(TheGodfather)
CREATE
  (Usuario1)-[:HASPUNCTUATED {score:4.8}]->(TheGodfather2)
CREATE
  (Usuario1)-[:HASPUNCTUATED {score:4.2}]->(TheGodfather3)
CREATE
  (Usuario2)-[:HASPUNCTUATED {score:5.0}]->(PulpFiction)
CREATE
  (Usuario2)-[:HASPUNCTUATED {score:0.0}]->(BatmanBegins)
CREATE
  (Usuario2)-[:HASPUNCTUATED {score:0.0}]->(TheGodfather)
CREATE
  (Usuario3)-[:HASPUNCTUATED {score:1.0}]->(PulpFiction)
CREATE
  (Usuario3)-[:HASPUNCTUATED {score:1.0}]->(TheGodfather)
CREATE
  (Usuario3)-[:HASPUNCTUATED {score:5.0}]->(BatmanBegins)
CREATE
  (Usuario4)-[:HASPUNCTUATED {score:0.0}]->(PulpFiction)
CREATE
  (Usuario4)-[:HASPUNCTUATED {score:5.0}]->(BatmanBegins)
CREATE
  (Usuario4)-[:HASPUNCTUATED {score:1.0}]->(TheGodfather)
  
  
  
  
  
  
  
  
  
