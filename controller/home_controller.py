from flask_openapi3 import Info, Tag

class HomeController():

    info = Info(title="APEF API", version="1.0.0")
    
    home_tag = Tag(name="Documentação", 
               description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
    
    def home(self):
        return '/openapi'