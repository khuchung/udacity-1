import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'udacity1'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'KmuZT9wl0nbg3uXSm/nXPlR1qukzKyJMR7ID6hr9DYAXJqGCuXfsMHFILZmdJuHB8mT/2m26SOgX+ASth1EgTg=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'test1'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'udacity-1.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'test1'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'hungkm'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Admin_123'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    # SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    # mssql+pyodbc://user:password@host:port/databasename?driver=ODBC+Driver+17+for+SQL+Server
    # SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://hungkm:Admin_123@udacity-1.database.windows.net:1433/test1?driver=ODBC+Driver+17+for+SQL+Server'


    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = "dND8Q~Ykv6HPpIKffVDvxZBkBQ_qc76c5pe01a-."
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/FPTSoftware362"

    CLIENT_ID = "c8eae371-bc65-45ad-9a1d-4d31834fa38a"

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session
