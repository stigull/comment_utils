#coding: utf-8

from django.contrib.comments.views.comments import post_comment as django_post_comment
import django.db.models as models
from django.template.loader import render_to_string

from utils.djangoutils import JSONResponse

def no_comment(request):
    return JSONResponse(object = {})

def post_comment(request):
    jsonobject = {}
    if request.method == "POST":
        data = request.POST.copy()
        verification_code = data.get("verification")
        object_pk = data.get("object_pk")
        verified = False
        try:
            #Uppfaert. Spurning geymd i stigull/templates/comments/forms.html
            if verification_code == 'geirfugl':
                verified = True
        except:
            verified = False
        
        if not verified:
            jsonobject['succeeded'] = False
            return JSONResponse(object = jsonobject)
        
        django_post_comment(request) #TODO: Better validation!
        
        ctype = data.get("content_type")
        
        if ctype is None or object_pk is None:
            jsonobject['succeeded'] = False
        else:
            try:
                model = models.get_model(*ctype.split(".", 1))
                object = model._default_manager.get(pk=object_pk)
            except TypeError:
                jsonobject['succeeded'] = False
            else:
                jsonobject['succeeded'] = True
                jsonobject['comments'] = render_to_string('comments/list_of_comments.html', {'object': object, 'user': request.user })
    else:
        jsonobject['succeeded'] = False
    
    return JSONResponse(object = jsonobject)
