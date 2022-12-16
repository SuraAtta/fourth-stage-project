from ninja import Router
from MyStore.models import Category
from MyStore.schema import CategorySchema
from typing import List


category__router = Router(tags=['category'])


@category__router.get("/get-all-categories", response=List[CategorySchema])
def get_all(request):
    categories = Category.objects.all()
    return 200, categories


