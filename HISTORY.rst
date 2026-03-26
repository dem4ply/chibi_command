=======
History
=======

********************
2.4.5 ( 2026-03-25 )
********************

* se cambio para que el comando ssh use -t para una pseudo terminal

********************
2.4.4 ( 2026-03-25 )
********************

* se cambio la estructura del comando ssh para poder encdenar multiples comandos con su
* se agrego el comando cd

********************
2.4.3 ( 2026-03-25 )
********************

* correcion cuando se manda su por ssh se agregaron las comillas para -c

********************
2.4.2 ( 2026-03-25 )
********************

* se agrego el argumento faltante para su -c en el comando sudo

********************
2.4.1 ( 2026-03-25 )
********************

* se agrega alternativa a sudo con su en el comando de ssh

********************
2.4.0 ( 2026-03-25 )
********************

* se agrego atajo para parchear popen
* se agrego parametro en las clases para agregar variables de ambiente cuando
	se ejecuta algun comando
* se agrego funcion para buscar paquetes con pacman

********************
2.3.2 ( 2026-03-24 )
********************

* se agrego la propiedad para asignar el identity file para ssh
* se agrego la propiedad de usuario y host para el comando ssh

********************
2.3.1 ( 2026-03-20 )
********************

* correcion en el nombre de la llave time o tiempo para el comando de ping

********************
2.3.0 ( 2026-03-20 )
********************

* se agrego la opcion de ignore-existing para rsync
* se agrego el comando e2label

********************
2.2.0 ( 2026-03-20 )
********************

* se agrego el comando lsblk en chibi_command.disk.lsblk

********************
2.1.1 ( 2025-05-22 )
********************

* usar el RPM.query() hace que el comando sea captivo

********************
2.1.0 ( 2025-05-21 )
********************

* se agrego el snippet para saber la ip local Ip.get_my_local_ip()
* se agregaron los argumentos para queries de changelog de rpm RPM.query().changelog().run( 'some.rpm' )

********************
2.0.0 ( 2025-05-15 )
********************

* se migro el uso de git a https://github.com/dem4ply/chibi_git

********************
1.1.3 ( 2025-03-12 )
********************

* se agrego repr a los results de los comandos
* correcion con el f string que faltaba en un logger debug

********************
1.1.0 ( 2024-10-18 )
********************

* comando ping

********************
1.0.0 ( 2024-10-18 )
********************

* se cambio el comportamiento para que tire una excepcion cada vez que un comando falla

********************
0.9.0 ( 2024-10-17 )
********************

* comando de ssh

********************
0.8.0 ( 2024-10-17 )
********************

* se agrego comandos para archlinux ( pacman y yay )

******************
0.6.0 (2020-02-19)
******************

* se agrego cp en chibi_command.commnon

******************
0.0.1 (2020-02-19)
******************

* First release on PyPI.
