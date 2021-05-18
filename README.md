# proyecto-py
simple user help
ES-Asistente al usuario con logeo y uso de BBDD para ingreso y eliminacion de notas posee un error al borrar las notas, para uso debe tener creacion de un servidor en BBDD llamado "master_python" libre criterio y modificacion del mismo, agradecimientos a victor robles web por enseñansa a travez de su curso master en python udemy.


EN-Assistant to the user with logging and use of DB to enter and delete notes has an error when deleting the notes, for use must have creation of a DB server called "master_python" free criteria and modification of it, thanks to victor robles web for He teaches through his master course in python udemy.

Creation/creacion:

database = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd="",
    database="master_python"
)
