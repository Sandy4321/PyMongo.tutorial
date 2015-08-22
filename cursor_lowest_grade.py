import pymongo
import sys

# establish a connection to the db
connection = pymongo.MongoClient("mongodb://localhost")
# get a handle to the g database
db = connection.students
grades = db.grades

def remove_score(_id):

    try:
        doc = grades.find_one( { '_id' : _id } )
        print "removing score ", doc['score'], " for student ", doc['student_id']
        grades.remove( { "_id" : _id } )

    except Exception as e:
        print "Unexpected error: ", type(e), e
        raise

def remove_lowest():

    cursor = grades.find( { 'type' : 'homework' } ).sort( [ ( 'student_id', pymongo.ASCENDING ), ( 'score', pymongo.ASCENDING ) ] )

    student_id = -1;

    for item in cursor:

        if (item['student_id'] != student_id):
            remove_score(item['_id'])
        student_id = item['student_id']


remove_lowest()
