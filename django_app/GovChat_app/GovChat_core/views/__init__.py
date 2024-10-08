from GovChat_app.GovChat_core.dash_apps import report_app
from GovChat_app.GovChat_core.views.auth_views import sign_in_link_sent_view, sign_in_view, signed_out_view
from GovChat_app.GovChat_core.views.chat_views import ChatsTitleView, ChatsView
from GovChat_app.GovChat_core.views.citation_views import CitationsView
from GovChat_app.GovChat_core.views.demographics_views import CheckDemographicsView, DemographicsView
from GovChat_app.GovChat_core.views.document_views import (
    DocumentView,
    UploadView,
    file_status_api_view,
    remove_doc_view,
)
from GovChat_app.GovChat_core.views.info_views import accessibility_statement_view, privacy_notice_view, support_view
from GovChat_app.GovChat_core.views.misc_views import SecurityTxtRedirectView, health, homepage_view
from GovChat_app.GovChat_core.views.ratings_views import RatingsView

__all__ = [
    "ChatsTitleView",
    "ChatsView",
    "CheckDemographicsView",
    "CitationsView",
    "DemographicsView",
    "DocumentView",
    "RatingsView",
    "SecurityTxtRedirectView",
    "UploadView",
    "file_status_api_view",
    "health",
    "homepage_view",
    "remove_doc_view",
    "privacy_notice_view",
    "accessibility_statement_view",
    "support_view",
    "sign_in_view",
    "sign_in_link_sent_view",
    "signed_out_view",
    "report_app",
]
