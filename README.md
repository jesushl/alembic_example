# ALPHAVANTAGE Tool

This tool consume information from Alphavantage.co,  
and returns information about companies as 
symbol, industry, description, quartery earns and annualy earns
consumig data from two different endopoints related with Overview and Earnings

## Database 
```mermaid
    erDiagram
        CUSTOMER ||--o{ ORDER : places
        ORDER ||--|{ LINE-ITEM : contains
        CUSTOMER }|..|{ DELIVERY-ADDRESS : uses
        COUNTRY ||--|{ COMPANY
        SECTOR ||--|{ COMPANY
        ANNUAL_EARNING }|..|{ COMPANY
        QUARTERLY_EARNING }|..|{ COMPANY
```

documentation  in /docs endpoint 
