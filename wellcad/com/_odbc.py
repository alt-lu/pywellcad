from ._dispatch_wrapper import DispatchWrapper

class Odbc(DispatchWrapper):
    """ An ODBC object allows interaction with databases from within WellCAD.

    Example
    -------
    >>> odbc = borehole.odbc
    >>> odbc.interpret_sql_statement('$dsn = OpenDatabase(Test, Admin)')
    >>> odbc.interpret_sql_statement('$log = SELECT Depth, Value FROM tblGamma')
    """

    def interpret_sql_statement(self, statement):
        """Executes the SQL statement provided

        A user manual documenting the syntax of the SQL statements that can be
        used can be obtained by contacting support@alt.lu.

        Parameters
        ----------
        statement : str
            The SQL statement to execute.

        Returns
        -------
        bool
            Whether the statement executed successfully.
        """
        return self._dispatch.InterpretSQLStatement(statement)
