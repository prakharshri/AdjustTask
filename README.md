# AdjustTask


# Pipeline

This repo contains the code for creating a data pipeline to get the amount of paid installs by country, which happened in May 2019:

* `instance_db.py` -- generates instance tables in PostgresSQL.
* `csv_data.py` -- reads the CSV files and inserts the csv files to them.
* `result.py` -- pulls from the database to get the amount of paid installs by country, which happened in May 2019.

# Installation

To get this repo running:

* Install Python 3.  You can find instructions [here](https://wiki.python.org/moin/BeginnersGuide/Download).
* Clone this repo with `git clone https://github.com/prakharshri/AdjustTask.git`
* Get into the folder with `cd adjust_task`
* Install the requirements with `pip3 install psycopg2`

# Usage

* Execute the three scripts mentioned above, in order.

You should see output from `result.py`.

