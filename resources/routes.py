from .databasecrud import dbApi

def initialize_routes(api):
    api.add_resource(dbApi, '/api/dtr')
    # api.add_resource(MovieApi, '/api/movies/<id>')
