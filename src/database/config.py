from neomodel import db, config # type: ignore

config.DATABASE_URL = "bolt://neo4j:test1234@127.0.0.1:7687"

try:
    results, _ = db.cypher_query("RETURN 1")
    print("SUCCESS", results)
except Exception as e:
    print("ERROR", e)