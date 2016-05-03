def wsgi_application(environ, start_response)
    status = ‘200 OK’
    response_headers = [(‘Content-Type’, ‘text/plain’)]
    start_response(status, response_headers) 
    options = ‘\r\n’.join(environ[‘QUERY_SRTING’].split(«&»))
    return [options]