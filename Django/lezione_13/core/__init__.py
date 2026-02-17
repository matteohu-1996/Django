import pymysql

pymysql.version_info = (2, 2, 1, "final", 0)
pymysql.install_as_MySQLdb() # fa sembrare a django che pymysql sia
# MyDQLClient, un altro driver per la connessione al DBMS, che è scritto in C++
# Non usiamo mysqlclient perchè richiede una configurazione più estesa e
# complessa.

try:
    from django.db.backends.mysql.base import DatabaseWrapper
    DatabaseWrapper.check_database_version_supported = lambda self: None
except ImportError:
    pass