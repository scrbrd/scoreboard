""" Package: model.data

Provide access to the underlying database. Currently, the db
is neo4j and is accessed using Gremlin. 

Modules
    db
    data_errors

Exception
    |
    +-- DbInputError
    +-- DbReadError
    +-- DbWriteError
    +-- DbConnectionError 

"""

from data_errors import DbInputError, DbReadError, DbWriteError
from data_errors import DbConnectionError

