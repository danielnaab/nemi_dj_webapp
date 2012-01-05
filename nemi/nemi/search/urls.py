
''' This module contains the url conf for the nemi search pages.
'''

from django.conf.urls.defaults import patterns, url
import views;

urlpatterns = patterns("", 
        url(r'^general_search/$',
            views.GeneralSearchView.as_view(),
            name='search-general'),
        url(r'^general_search_tsv/$',
            views.GeneralSearchView.as_view(),
            {'export' : 'tsv'},
            name='search-general_export_tsv'),
        url(r'^general_search_xls/$',
            views.GeneralSearchView.as_view(),
            {'export' : 'xls'},
            name='search-general_export_xls'),
        url(r'^method_summary/(?P<method_id>\d+)/$',
            views.MethodSummaryView.as_view(),
            name='search-method_summary'),
        url(r'^method_analyte_export/(?P<method_id>\w+)/$',
            views.ExportMethodAnalyte.as_view(),
            name='search-method_analyte_export'),
        url(r'^analyte_search/$', 
            views.AnalyteSearchView.as_view(),
            name='search-analyte_search'),
        url(r'^analyte_search_tsv/$',
            views.AnalyteSearchView.as_view(),
            {'export' : 'tsv'},
            name='search-analyte_export_tsv'),
        url(r'^analyte_search_xls/$',
            views.AnalyteSearchView.as_view(),
            {'export' : 'xls'},
            name='search-analyte_export_xls'),
        url(r'^analyte_select/$',
            views.AnalyteSelectView.as_view(),
            name='search-analyte_select'),
        url(r'^keyword_search/$',
            views.KeywordSearchView.as_view(),
            name='search-keyword'),
        )