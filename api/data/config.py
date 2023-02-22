from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов

# DB_URI = env.str('DB_URI')
# HOST = env.str('HOST')
# DATABASE = env.str('DATABASE')
# USER = env.str('USER')
# PASSWORD = env.str('PASSWORD')
# MONGO_P = env.str('MONGO_P')
# MONGO_U = env.str('MONGO_U')
