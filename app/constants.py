PROJECT_DESCRIPTION = """This application is an API  works to provide information about companies,
                                                        as name, description, country, sector and lates annual earnings per share and latest 
                                                        quarterly earnings per share
                                                        """

ALPHAVANTAGE_API_URL="https://www.alphavantage.co/query?function={function}&symbol={symbol}&apikey={ALPHAVANTAGE_KEY}"

EARNINGS_FUNCTION = "EARNINGS"
OVERVIEW_FUNCTION = "OVERVIEW"

annual_earnings = "annualEarnings"
quarterly_earnings = "quarterlyEarnings"