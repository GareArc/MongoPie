import os
from dotenv import load_dotenv
load_dotenv(dotenv_path=".env")
    
def pytest_sessionstart(session):
    """
    Called after the Session object has been created and
    before performing collection and entering the run test loop.
    """
    print("Connecting to database...")
    from mongopie.client import MongoPieClient
    # Connect to database
    MongoPieClient.connect(
        'db',
        uri=os.getenv('MONGODB_URI', 'mongodb://localhost:27017/'), 
    )
    print("Connected to database!")
    
    