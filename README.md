# E - commerce Management 

## 🔧 Requirements

- Python 3.8+
- Django 5+
- djangorestframework
- djangorestframework-simplejwt
  
## Feature

- This is a Django project using Django REST Framework (DRF) with:
- Custom User Model (email as username)
- Profile API
- JWT Authentication (SimpleJWT)
- Email verification
- Password reset using Django's built-in tools
- Create models for Product and Category.
- Enable listing, filtering, and pagination by category.
- Implement search functionality for products using Django or DRF capabilities.
- Set up Stripe to handle payments.
- stripe success & cancel url

  ## API End-Point
- Admin panel
- email: admin@gmail.com , Pass : 123
- http://localhost:8000/admin (Admin api)
- http://localhost:8000/myappp/profile (Authenticated profile Details )
- http://localhost:8000/myapp/token/   ( Access & Refresh Token )
- http://localhost:8000/myapp/token/refresh ( Refresh Token )
- http://localhost:8000/myapp/password-reset/  ( Password reset api)
- http://localhost:8000/myapp/reset/<uidb64>/<token>/ ( password reset token )
- http://localhost:8000/myapp/reset/done/  (Reset Completed )
- http://localhost:8000/product/products/  ( show all products)
- http://localhost:8000/product/products/ 
