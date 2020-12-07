from mongoengine import connect

def global_init():
    DB_URI = "mongodb+srv://recipe-gen:Password@recipegeneratorcluster.janaq.mongodb.net/test?retryWrites=true&w=majority"

    connect(alias="core",host=DB_URI )

    