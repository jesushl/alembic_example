# ALPHAVANTAGE Tool

This tool consume information from Alphavantage.co,  
and returns information about companies as 
symbol, industry, description, quartery earns and annualy earns
consumig data from two different endopoints related with Overview and Earnings

## Database 
```mermaid
    erDiagram
        COUNTRY ||--|{ COMPANY:contains
        SECTOR ||--|{ COMPANY:contains
        ANNUAL_EARNING }|..|{ COMPANY: contains
        QUARTERLY_EARNING }|..|{ COMPANY: contains
```

documentation  in /docs endpoint 
