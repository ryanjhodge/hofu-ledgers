#
# DUMP FILE
#
# Database is ported from MS Access
#------------------------------------------------------------------
# Created using "MS Access to MySQL" form http://www.bullzip.com
# Program Version 5.1.242
#
# OPTIONS:
#   sourcefilename=C:\Users\Ryan\Desktop\Hopewell\Hopewell Database_RJH.mdb
#   sourceusername=
#   sourcepassword=
#   sourcesystemdatabase=
#   destinationdatabase=hofuHistoric
#   storageengine=MyISAM
#   dropdatabase=0
#   createtables=1
#   unicode=1
#   autocommit=1
#   transferdefaultvalues=1
#   transferindexes=0
#   transferautonumbers=1
#   transferrecords=1
#   columnlist=1
#   tableprefix=
#   negativeboolean=0
#   ignorelargeblobs=0
#   memotype=LONGTEXT
#

CREATE DATABASE IF NOT EXISTS `hofuHistoric`;
USE `hofuHistoric`;

#
# Table structure for table 'LABORDYN'
#

DROP TABLE IF EXISTS `LABORDYN`;

CREATE TABLE `LABORDYN` (
  `ID` INTEGER NOT NULL AUTO_INCREMENT, 
  `LASTNAME` VARCHAR(60), 
  `FIRSTNAME` VARCHAR(50), 
  `GENDER` VARCHAR(1), 
  `RACE` VARCHAR(1), 
  `OCCUP1` VARCHAR(60), 
  `OCCUP2` VARCHAR(60), 
  `OCCUP3` VARCHAR(60), 
  `OCCUP4` VARCHAR(60), 
  `OCCUP5` VARCHAR(30), 
  `TENUREFROM` DATE, 
  `TENURETO` DATE, 
  `TENUREFR2` DATE, 
  `TENURETO2` DATE, 
  `TENUREFR3` DATE, 
  `TENURETO3` DATE, 
  `TENURETO3a` DATE, 
  `SOURCES` VARCHAR(255), 
  `NOTES` LONGTEXT, 
  `BEGIN` VARCHAR(50), 
  `END` VARCHAR(50), 
  INDEX (`ID`)
) ENGINE=myisam DEFAULT CHARSET=utf8;
