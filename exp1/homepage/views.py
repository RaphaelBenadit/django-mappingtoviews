from django.http import HttpResponse

def welcome_view(request):
    html_content = """
    <html>
        <head>
            <title>Welcome</title>
        </head>
        <body>
            <center><h1>Welcome to the Django website</h1>
            <h3>I am Raphael Benadit G,22UIT019,III year in the department of Information technology.</h3>
             <h3>I'm very excited to learn new skills in future.</h3> </center>
        </body>
    </html>
    """
    return HttpResponse(html_content)
