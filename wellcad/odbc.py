class Odbc:

    def __init__(self, odbc_dispatch):
        """Creates the odbc object.
        
        Use the get_odbc method in the borehole object to retrieve
        an object for the ODBC module.
        """

        if not odbc_dispatch:
            raise TypeError("No ODBC COM object supplied.")
        
        self.dispatch = odbc_dispatch

    def interpret_sql(self, sql_statement):
        """Executes the sql statement provided as argument.

        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            sql_statement -- String containing the sql statement.

        """

        self.dispatch.InterpretSQLStatement(sql_statement)
