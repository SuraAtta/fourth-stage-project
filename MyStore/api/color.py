from ninja import Router
from MyStore.models import Color
from MyStore.schema import ColorSchema
from typing import List


color__router = Router(tags=['color'])


@color__router.get("/get-all-colors", response=List[ColorSchema])
def get_all(request):
    colors = Color.objects.all()
    return 200, colors

