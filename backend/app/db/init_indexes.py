from pymongo import ASCENDING

def create_indexes(db):
    # unique index on faculty_profiles.user_id
    db["faculty_profiles"].create_index([("user_id", ASCENDING)], unique=True)
