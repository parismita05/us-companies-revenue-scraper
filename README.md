# US Companies Revenue Scraper

This is a beginner-friendly web scraping project that extracts data from Wikipedia's page on the largest U.S. companies by revenue. The script uses **BeautifulSoup** and **Pandas** to:

- Scrape a table of the top 100 companies by revenue.
- Parse the HTML table and convert it into a structured pandas DataFrame.
- Export the data into a CSV file for further analysis.

## 🔧 Technologies Used
- Python 3
- BeautifulSoup
- Requests
- Pandas

## 📁 Files in this Repository
- `practice.py`: The main Python script for scraping and saving data.
- `company.csv`: The output CSV file containing company data (optional).

## 📌 Data Source
- Wikipedia: [List of largest companies in the United States by revenue](https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue)

## 🚀 How to Use
1. Clone this repository or download the script.
2. Run `practice.py` using Python.
3. The script will fetch and save the data as `company.csv`.

## 📈 Sample Output
| Rank | Name | Industry | Revenue | Employees | Headquarters |
|------|------|----------|---------|-----------|--------------|
| 1    | Walmart | Retail | $611.3B | 2,100,000 | Bentonville, AR |
| ...  | ...      | ...      | ...     | ...         | ...              |

---

Happy Scraping! 
