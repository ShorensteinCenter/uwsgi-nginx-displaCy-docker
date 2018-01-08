import falcon


class HelloWorldResource:

    def on_get(self, request, response):

        response.media = ('Hello World from Falcon in a uWSGI Nginx Docker' +
                          ' container with Python 3.6')


app = falcon.API()
app.add_route('/', HelloWorldResource())