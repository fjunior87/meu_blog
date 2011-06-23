from django.shortcuts import render_to_response
from models import Artigo
# Create your views here.
def artigo(request, artigo_id):
	artigo = Artigo.objects.get(id=artigo_id)
	return render_to_response('blog/artigo.html',locals())