from ninja import Router
from MyStore.models import ColorLogo
from MyStore.schema import ColorLogoSchema
from typing import List


colorLogo__router = Router(tags=['colorLogo'])


@colorLogo__router.get("/get-colorLogo", response=List[ColorLogoSchema])
def get_all(request):
    colorLoge = ColorLogo.objects.all()
    return 200, colorLoge


