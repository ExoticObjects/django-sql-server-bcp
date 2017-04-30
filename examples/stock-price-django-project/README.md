# Example Usage

- Set your database settings in `main/settings.py`
- Create a virtualenv and install dependencies `pip install -r requirements.txt`
- Run `python manage.py migrate`
- Run command to test bulk import of StockPrice records `python manage.py bulk_save_stockprices`

Output should resemble this:

```
>>> python manage.py bulk_save_stockprices
Starting copy...

499 rows copied.
Network packet size (bytes): 4096
Clock Time (ms.) Total     : 10     Average : (49900.0 rows per sec.)

```