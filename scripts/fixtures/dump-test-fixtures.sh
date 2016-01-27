# Should be run from project directory

# Depending on virtualenv, use one of these two:
#./manage.py dumpdata quickpages --format=yaml $all >conf/env/src/django-quickpages/quickpages/fixtures/quickpages.yaml
./manage.py dumpdata quickpages --format=yaml $all >conf/src/django-quickpages/quickpages/fixtures/quickpages.yaml


# MANI:  THESE ARE IN VARIOUS STAGES OF TESTING - LEFT HERE TO SEE WHAT I'VE DONE SO FAR - JOE

./manage.py dumpdata home.featuredimage      --pks=53685,53686,56721 --format=yaml >apps/home/fixtures/home.yaml
./manage.py dumpdata auth.user               --pks=2,3,4,42,43         --format=yaml >apps/customers/fixtures/users.yaml
./manage.py dumpdata customers.customer      --pks=2,54987,55132,54730 --format=yaml >apps/customers/fixtures/customers.yaml
./manage.py dumpdata customers.customerimage --pks=53336,53337,53338 --format=yaml >>apps/customers/fixtures/customers.yaml
./manage.py dumpdata customers.testimonial   --pks=53380,53381,53382 --format=yaml >>apps/customers/fixtures/customers.yaml
./manage.py dumpdata customers.address       --pks=54276,54731,54732 --format=yaml >>apps/customers/fixtures/customers.yaml

./manage.py dumpdata quotes.quote            --pks=1,55143,55149     --format=yaml $all >apps/quotes/fixtures/quotes.yaml
./manage.py dumpdata quotes.quotelineitem    --pks=1,55144,55150     --format=yaml $all >>apps/quotes/fixtures/quotes.yaml

./manage.py generate_fixtures products.models.Product 2 >apps/products/fixtures/products.yaml
./manage.py generate_fixtures products.models.Product 55174 >>apps/products/fixtures/products.yaml
echo >>apps/products/fixtures/products.yaml


# - - - new things tried:

./manage.py dumpdata auth.user               --pks=2,50,123,153 --natural-primary --format=yaml >apps/customers/fixtures/customers.yaml
./manage.py dumpdata customers.customer      --pks=2,54987,55132,54730 --natural-primary --natural-foreign --format=yaml >>apps/customers/fixtures/customers.yaml


./manage.py dumpdata auth.user               --pks=2,3,4,42,43,50,123,153 --format=yaml >>apps/customers/fixtures/customers.yaml



./manage.py dumpdata customers.customer      --pks=54730 --natural-foreign --format=yaml >apps/customers/fixtures/customers.yaml
./manage.py dumpdata customers.customerimage --pks=53336,53337,53338 --format=yaml >>apps/customers/fixtures/customers.yaml
./manage.py dumpdata customers.testimonial   --pks=53380,53381,53382 --format=yaml >>apps/customers/fixtures/customers.yaml
./manage.py dumpdata customers.address       --pks=54276,54731,54732 --format=yaml >>apps/customers/fixtures/customers.yaml

orders - old!
  custs 2 3 4

./manage.py generate_fixtures orders.models.Order 57138 >>apps/orders/fixtures/orders.yaml
# includes 56122 spotterrf - 57138 is a recent order fm them
