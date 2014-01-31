from pages.models import Page
from haystack import indexes

class PageIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True)
    title = indexes.EdgeNgramField()
    url = indexes.CharField(indexed=False, null=False)
    search_display = indexes.CharField(indexed=False)

    def get_model(self):
        return Page

    def index_queryset(self, using=None):
        return self.get_model().objects.exclude(can_read='NONE')

    def prepare_text(self, p):
        v = p.current_version()
        title = v.title
        wikitext = v.get_wikitext()
        return title + '\n' + wikitext

    def prepare_title(self, p):
        v = p.current_version()
        return v.title

    def prepare_search_display(self, p):
        v = p.current_version()
        return "%s: %s" % (p.offering.name(), v.title)

    def prepare_url(self, p):
        return p.get_absolute_url()
