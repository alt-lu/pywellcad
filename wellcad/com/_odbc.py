from ._noneable_wrapper import NoneableWrapper

class Odbc(NoneableWrapper):
    def interpret_sql(self, sql_statement):
        """Executes the sql statement provided as argument.

        A full description of the method and its parameters is given
        in the Automation Module chapter of the WellCAD help
        documentation. 

        Arguments:
            sql_statement -- String containing the sql statement.

        """

        self._dispatch.InterpretSQLStatement(sql_statement)
