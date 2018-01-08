import falcon


class HelloWorldResource:

    def on_get(self, request, response):

        response.media = ('Hello World from Falcon in a uWSGI Nginx Docker' +
                          ' container with Python 3.6')


class StaticResource:

    def on_get(self, request, response):

        response.status = falcon.HTTP_200
        response.content_type = 'text/html'
        with open('static/index.html', 'r') as f:
            response.body = f.read()


app = falcon.API()
app.add_route('/', StaticResource())
app.add_route('/hello', HelloWorldResource())