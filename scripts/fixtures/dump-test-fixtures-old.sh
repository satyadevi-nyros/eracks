# Should be run from project directory

#all='--all'
all=''

# Depending on virtualenv, use one of these two:
#./manage.py dumpdata quickpages --format=yaml $all >conf/env/src/django-quickpages/quickpages/fixtures/quickpages.yaml
./manage.py dumpdata quickpages --format=yaml $all >conf/src/django-quickpages/quickpages/fixtures/quickpages.yaml

./manage.py dumpdata bloglets   --format=yaml $all >apps/bloglets/fixtures/bloglets.yaml
./manage.py dumpdata home       --format=yaml $all >apps/home/fixtures/home.yaml
./manage.py dumpdata quotes     --format=yaml $all >apps/quotes/fixtures/quotes.yaml
./manage.py dumpdata auth.user  --format=yaml $all >apps/customers/fixtures/users.yaml
./manage.py dumpdata customers  --format=yaml $all >apps/customers/fixtures/customers.yaml
./manage.py dumpdata quotes     --format=yaml $all >apps/quotes/fixtures/quotes.yaml
./manage.py dumpdata products   --format=yaml $all >apps/products/fixtures/products_all.yaml

./manage.py generate_fixtures products.models.Product 2 >apps/products/fixtures/products.yaml

