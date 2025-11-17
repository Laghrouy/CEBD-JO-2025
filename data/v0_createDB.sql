CREATE TABLE V0_LesSportifsEQ
(
  numSp NUMBER(4),
  nomSp VARCHAR2(20),
  prenomSp VARCHAR2(20),
  pays VARCHAR2(20),
  categorieSp VARCHAR2(10),
  dateNaisSp DATE,
  numEq NUMBER(4),
  CONSTRAINT SP_CK1 CHECK(numSp > 0),
  CONSTRAINT SP_CK2 CHECK(categorieSp IN ('feminin','masculin')),
  CONSTRAINT SP_CK3 CHECK(numEq > 0)
);

CREATE TABLE V0_LesEpreuves
(
  numEp NUMBER(3),
  nomEp VARCHAR2(20),
  formeEp VARCHAR2(13),
  nomDi VARCHAR2(25),
  categorieEp VARCHAR2(10),
  nbSportifsEp NUMBER(2),
  dateEp DATE,
  CONSTRAINT EP_PK PRIMARY KEY (numEp),
  CONSTRAINT EP_CK1 CHECK (formeEp IN ('individuelle','par equipe','par couple')),
  CONSTRAINT EP_CK2 CHECK (categorieEp IN ('feminin','masculin','mixte')),
  CONSTRAINT EP_CK3 CHECK (numEp > 0),
  CONSTRAINT EP_CK4 CHECK (nbSportifsEp > 0)
);

-- Nouvelles tables pour la BD v0

-- Nombre d'inscriptions par épreuve
CREATE TABLE V0_LesInscriptions (
  numIn NUMBER(4),
  numEp NUMBER(3),
  CONSTRAINT IN_PK PRIMARY KEY (numIn),
  CONSTRAINT IN_FK1 FOREIGN KEY (numEp) REFERENCES V0_LesEpreuves(numEp),
  CONSTRAINT IN_CK1 CHECK (numIn > 0),
  CONSTRAINT IN_CK2 CHECK (numEp > 0)
);

-- Médailles par épreuve
CREATE TABLE V0_LesResultats (
  numEp NUMBER(3),
  gold NUMBER(4),
  silver NUMBER(4),
  bronze NUMBER(4),
  CONSTRAINT RE_PK PRIMARY KEY (numEp),
  CONSTRAINT RE_FK1 FOREIGN KEY (numEp) REFERENCES V0_LesEpreuves(numEp),
  CONSTRAINT RE_CK1 CHECK (gold >= 0),
  CONSTRAINT RE_CK2 CHECK (silver >= 0),
  CONSTRAINT RE_CK3 CHECK (bronze >= 0)
);
