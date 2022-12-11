import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
# Create your models here.
"""
User
    - id 
    - name
    - email
    - password
    
#################

Product
    - id
    - name
    - banner
    - description
    - category (fk)
    - colors (fk)
    - price
    - stock
    - is available (bool) (if false, puts out of stock label)
    - show/hide (bool) 
    - created (date)
    - updated (date)
    - images (fk)
    
###################
    

"""

