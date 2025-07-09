from neomodel import config, db # type: ignore

config.DATABASE_URL = "bolt://neo4j:test1234@127.0.0.1:7687"

db.set_connection(config.DATABASE_URL)