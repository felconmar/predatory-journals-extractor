# Predatory Journals Historic Data

This project captures snapshots from the website [predatoryjournals.org](https://predatoryjournals.org), maintaining a historical record of entities identified as predatory journals and publishers. The data is updated regularly and can be explored through an interactive table on the project's GitHub Page.

You can access the historical data captured by this project on the live GitHub Page available [**here**](https://felconmar.github.io/predatory-journals-extractor/).

-----

## How It Works

The project uses a Python script (`predatory_journal_scrapper.py`) to scrape data from the source. The entire process is automated using GitHub Actions to ensure the data remains current.

1.  **Data Scraping**: A Python script periodically downloads the lists of predatory journals and publishers. The source provides this data in an Excel format.
2.  **Data Processing**: The script extracts the names and associated URLs for each entry.
3.  **Archiving**: It compares the newly downloaded list with the existing data stored in CSV files (`predatory_journal.csv` and `predatory_publisher.csv`).
      * If a journal or publisher is new, it is added to the list with the current date.
      * If an entry already exists, its original "Since" date is preserved, ensuring a consistent historical record of when it first appeared.
4.  **Web Interface**: The `index.html` file uses JavaScript to load the CSV data into a searchable, sortable, and downloadable table on the GitHub Pages site. Users can toggle between the journal and publisher lists.

## Data Fields

The archived CSV files contain the following columns:

  * **Journal / Publisher**: The name of the journal or publisher.
  * **Link**: A direct URL to the entity's website.
  * **Since**: The date when the scraper first recorded the entry. This date remains fixed to mark its first appearance in the dataset.

## Source and Acknowledgements

  * This project relies entirely on the data made publicly available by **[predatoryjournals.org](https://www.predatoryjournals.org)**.
  * The front-end table display is powered by the [CSV to HTML Table](https://github.com/derekeder/csv-to-html-table) library by [Derek Eder](http://derekeder.com).

## License

This is a free and open-source project. The code is distributed under the GNU General Public License. This means you have the freedom to use, modify, and distribute the code, but you must also make your source code available under the same GPL license if you distribute a modified version.
