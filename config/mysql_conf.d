[mysqld]
skip-character-set-client-handshake
character-set-server=utf8
collation-server=utf8_general_ci
init-connect = SET NAMES utf8
[client]
default-character-set=utf8
