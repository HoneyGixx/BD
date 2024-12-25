/*Created: 04.09.2024
Modified: 05.09.2024Model: Microsoft SQL Server 2019
Database: MS SQL Server 2019*/

-- Create tables section -------------------------------------------------
-- Table Ngram
CREATE TABLE [Ngram]
( [IDWord] Int IDENTITY NOT NULL,
 [Word] Nchar(254) NULL, [IDText] Int NOT NULL
)
go
-- Add keys for table Ngram
ALTER TABLE [Ngram] ADD CONSTRAINT [PK_Ngram] PRIMARY KEY ([IDWord],[IDText])
go
-- Table Lem
CREATE TABLE [Lem](
 [IDLem] Int IDENTITY NOT NULL, [Lem] Char(254) NULL,
 [PoS] Char(254) NULL, [IDWord] Int NOT NULL,
 [IDText] Int NOT NULL)
go
-- Add keys for table Lem
ALTER TABLE [Lem] ADD CONSTRAINT [PK_Lem] PRIMARY KEY ([IDLem],[IDWord],[IDText])
go
-- Table Text
CREATE TABLE [Text]
( [IDText] Int IDENTITY NOT NULL,
 [Text] Text NULL, [Phrase] Nchar(254) NULL
)
go
-- Add keys for table Text
ALTER TABLE [Text] ADD CONSTRAINT [PK_Text] PRIMARY KEY ([IDText])
go
-- Create foreign keys (relationships) section ------------------------------------------------- 
ALTER TABLE [Ngram] ADD CONSTRAINT [textGram] FOREIGN KEY ([IDText]) REFERENCES [Text] ([IDText]) ON UPDATE NO ACTION ON DELETE NO ACTION
go

ALTER TABLE [Lem] ADD CONSTRAINT [NgrLem] FOREIGN KEY ([IDWord], [IDText]) REFERENCES [Ngram] ([IDWord], [IDText]) ON UPDATE NO ACTION ON DELETE NO ACTION
go

SELECT * from Text

SELECT * from Ngram

SELECT * from Lem