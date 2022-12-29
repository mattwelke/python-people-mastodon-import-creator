# python-people-mastodon-import-creator

A Python script that reads the latest version of the [Python People Gist](https://gist.github.com/samuelcolvin/1743d8919acb465c1fbbcea2c3cdaf3e), finds who on it is on Mastodon, and uses that to create a CSV file that can be imported into a Mastodon instance.

Inspired by the ]Java Champions import](https://javachampions.org/resources/mastodon.csv).

Creates a file that looks like this:

```csv
Account address,Show boosts,Notify on new posts,Languages
@dabeaz@mastodon.social,true,false,
@tiangolo@fosstodon.org,true,false,
@mitsuhiko@hachyderm.io,true,false,
...
```

## Running

Ensure you have Python 3 with pip installed.

Clone the repo.

Create a virtual env and activate it. For example:

```bash
python -m venv .venv
source .venv/bin/activate
```

3) Use `pip` to install dependencies into the virtual env:

```bash
pip install -r requirements.txt
```

4) Run the script with the virtual env's Python:

```bash
python main.py
```

Example output (many names omitted for brevity):

```
Fetched list of Python people (161 people in total).
Filtered out Python people who are not on Mastodon (46 are on Mastodon).
Creating CSV import file at python_people_mastodon_import.csv.
Added David Beazley (@dabeaz@mastodon.social).
Added Sebastián Ramírez (@tiangolo@fosstodon.org).
Added Armin Ronacher (@mitsuhiko@hachyderm.io).
...
Done
```

5) Use your Mastodon instance's import UI to import the file. If your goal is to follow people you aren't already following, and you're okay with the import turning off notifications for people you may already be following, do it like this:

![image](https://user-images.githubusercontent.com/7719209/209893094-bbd2a87f-7bf9-449c-a51d-01d37ef858c4.png)

## Notes, getting help, and contributing

Python isn't one of my daily languages. This code might be fragile or otherwise weird. PRs are welcome!

If you have trouble running it or you have a feature request, feel free to open an issue.

To contribute, fork the repo and create a PR with your change. If a test suite using an automated testing framework for Python does not already exist when you open the PR, add a test suite using a popular framework (ex. pytest ). Add a test in the suite alongside your change in the PR.

## Trademarks

[Mastodon is a registered trademark of Mastodon gGmbH.](https://joinmastodon.org/trademark)

[Java is a registered trademark of Oracle and/or its affiliates.](https://www.oracle.com/legal/trademarks.html)
