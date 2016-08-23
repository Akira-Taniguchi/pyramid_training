# -*- coding:utf-8 -*-
# from pyramid.config import Configurator
# from wsgiref.simple_server import make_server
# from pyramid.response import Response
#
#
# def hello_world(request):
#     return Response('Hello %(name)s!' % request.matchdict)
#
# if __name__ == '__main__':
#     config = Configurator()
#     config.add_route('hello', '/hello/{name}')
#     config.add_view(hello_world, route_name='hello')
#     app = config.make_wsgi_app()
#     server = make_server('0.0.0.0', 8080, app)
#     server.serve_forever()


# -*- coding:utf-8 -*-

from pyramid.config import Configurator
from wsgiref.simple_server import make_server
from pyramid.view import view_config


def hello_context(request):
    return {"name": "foo"}


@view_config(route_name="hello", renderer="hello.jinja2")
def hello_view(request):
    return {}


if __name__ == '__main__':
    # configuration settings
    settings = {"jinja2.directories": "."}  # ここtemplateを格納するディレクトリを指定する
    # configuration setup
    config = Configurator(settings=settings, root_factory=hello_context)
    config.include("pyramid_jinja2")
    config.add_route("hello", "/")
    config.scan()

    print "==="
    print config.get_settings()["jinja2.directories"]
    print "==="

    # serve app
    app = config.make_wsgi_app()
    print "localhost:4567"
    server = make_server('0.0.0.0', 4567, app)
    server.serve_forever()
