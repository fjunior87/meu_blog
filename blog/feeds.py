from django.contrib.syndication.feeds import Feed
from models import Artigo

class UltimosArtigos(Feed):
	title = 'Utlimos Artigos do blog do Alatazan'
	link = '/'
	
	def items(self):
		return Artigo.objects.all()
	
