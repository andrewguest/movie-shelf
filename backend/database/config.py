from deta import Deta
from dotenv import load_dotenv


load_dotenv()

deta = Deta()
movies_collection = deta.Base("movies")
tv_collection = deta.Base("tv")
