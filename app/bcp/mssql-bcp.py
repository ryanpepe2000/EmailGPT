import bcp
import pathlib


conn = bcp.Connection("mssql", "localhost",52100,"username","password")
my_bcp = bcp.BCP(conn)

data = bcp.DataFile(pathlib.Path("file.csv"),"|")
