import os
from django.conf import settings

from private_storage.views import PrivateStorageView
from private_storage.storage.files import PrivateFileSystemStorage


class PrivateStreamformStorageView(PrivateStorageView):
    storage = PrivateFileSystemStorage(
        location=os.path.join(settings.BASE_DIR, 'media/streamforms/'),
        base_url='/media/streamforms/'
    )
