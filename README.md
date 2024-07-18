# CareerCrawler

A web scraper app built using Flask that scrapes job listings from Lever and Greenhouse.

## Features

* Scrape job listings from Lever and Greenhouse
* Display job titles, company names, and locations
* Search for jobs by title and location

## Usage

1. Clone the repository: `git clone https://github.com/dakshgajjar/careercrawler.git`
2. Install the dependencies: `pip install -r requirements.txt`
3. Run the app: `python app.py`
4. Open the app in your web browser: `http://localhost:5000`

## Configuration

The app uses two environment variables:

* `FLASK_APP`: Set to `app:app` to specify the app instance.
* `DEBUG`: Set to `True` to enable debug mode.

## Templates

* `some.html`: The main template for displaying job listings.

## Dependencies

The app requires the following dependencies:

* `requests`
* `beautifulsoup4`
* `flask`

## Deployment

[https://career-crawler.vercel.app/](https://career-crawler.vercel.app/)

## Known Issues

* The app may not work correctly if the job listings are blocked by the target websites.
* The app may not handle errors correctly if the target websites change their HTML structure.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you'd like to contribute to the app.

## License

The app is licensed under the MIT License. 
