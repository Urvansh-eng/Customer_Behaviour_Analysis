# Customer Shopping Behavior Analysis

An end-to-end data analytics project that explores customer shopping behavior through data cleaning, SQL analysis, and interactive dashboarding — turning raw transactional data into actionable business insights.

## Overview

This project analyzes a retail customer shopping dataset to uncover patterns in spending, discounts, subscriptions, and product preferences. The workflow covers the full analytics pipeline: data cleaning in Python, storage and querying in a relational database, business-question-driven SQL analysis, and visualization through an interactive Power BI dashboard — supported by a summary report and presentation.

**Key business questions explored:**
- How does revenue differ between male and female customers?
- Which customers use discounts but still spend above average?
- What are the top-rated and most-discounted products?
- Does a subscription or repeat-purchase behavior correlate with higher spend?
- How can customers be segmented into New, Returning, and Loyal groups?
- Which age groups contribute the most revenue?

## Dataset

- **Source:** Customer shopping behavior dataset (`customer_shopping_behavior.csv`)
- **Granularity:** One row per customer transaction
- **Key fields:** customer ID, age, gender, category, item purchased, purchase amount, review rating, subscription status, discount applied, shipping type, frequency of purchases, previous purchases

## Tools & Technologies

| Category | Tools |
|---|---|
| Data Cleaning & EDA | Python (Pandas) |
| Database | MySQL (compatible with PostgreSQL / SQL Server) |
| Analysis | SQL (window functions, CTEs, aggregations) |
| Visualization | Power BI |
| Reporting | Written summary report |
| Presentation | Gamma (AI-assisted slide deck) |

## Project Workflow

1. **Data Loading & Exploration**
   Loaded the raw CSV into Python using Pandas and performed initial exploratory data analysis (`head()`, `info()`, `describe()`) to understand structure, data types, and missing values.

2. **Data Cleaning**
   - Filled missing `Review Rating` values using the median rating per category
   - Standardized column names (lowercase, underscores)
   - Renamed ambiguous columns (e.g., `purchase_amount_(usd)` → `purchased_amount`)
   - Created a derived `age_group` column using quartile-based binning (Young Adult, Adult, Mid-aged, Senior)
   - Converted `frequency_of_purchases` (e.g., "Weekly", "Monthly") into numeric day values for easier analysis
   - Removed the redundant `promo_code_used` column after confirming it duplicated `discount_applied`

3. **Loading into a Relational Database**
   Loaded the cleaned dataset into a MySQL database using SQLAlchemy, replacing the `customer` table on each run for reproducibility.

4. **SQL Analysis**
   Wrote and executed business-focused SQL queries covering revenue breakdowns, discount behavior, customer segmentation, product performance, and subscription trends — using aggregations, CASE statements, subqueries, CTEs, and window functions (`ROW_NUMBER()`).

5. **Dashboard Development**
   Built an interactive Power BI dashboard to visualize key metrics and trends identified in the SQL analysis.

6. **Reporting & Presentation**
   Summarized findings in a written report and created a stakeholder-ready presentation using Gamma.

## Dashboard

The Power BI dashboard (`Customer_behaviour.pbix`) visualizes:
- Revenue by gender and age group
- Discount usage and its impact on spend
- Top-performing products by rating and purchase volume
- Subscription vs. non-subscription spending comparison
- Customer segmentation (New / Returning / Loyal)

> Open the `.pbix` file in Power BI Desktop to explore the dashboard interactively.

## Results & Key Insights

- Revenue and spending patterns vary meaningfully across gender and age groups
- A notable share of discount-using customers still spend above the average purchase amount
- A small set of products consistently receive the highest review ratings and purchase volume
- Subscribed and repeat-purchase customers show distinct spending behavior compared to one-time buyers
- Customer segmentation reveals a clear split between new, returning, and loyal customer bases

*(Update this section with your specific figures and takeaways once queries are run.)*

## How to Run

1. **Clone the repository / download project files**

2. **Set up the environment**
   ```bash
   pip install pandas sqlalchemy pymysql
   ```

3. **Configure the database connection**
   Update the credentials in `Customer_Shopping_Behaviour_Cleaning.py`:
   ```python
   username = "your_username"
   password = "your_password"
   host = "127.0.0.1"
   port = "3306"
   database = "customer_behavior"
   ```

4. **Run the cleaning script**
   ```bash
   python Customer_Shopping_Behaviour_Cleaning.py
   ```
   This cleans the raw CSV and loads it into the `customer` table in your MySQL database.

5. **Run the SQL queries**
   Open `Customer_behaviour_sql_queries.sql` in your SQL client and execute the queries against the `customer_behavior` database.

6. **Open the dashboard**
   Open `Customer_behaviour.pbix` in Power BI Desktop and refresh the data connection to point to your database.

## Project Structure

```
├── Customer_Shopping_Behaviour_Cleaning.py   # Data cleaning & loading script
├── Customer_behaviour_sql_queries.sql        # Business-question SQL queries
├── Customer_behaviour.pbix                   # Power BI dashboard
├── Report.pdf                                # Written summary report
├── Presentation.pdf                          # Gamma-generated presentation
└── README.md                                 # Project documentation
```

## Author

**Urvansh**
Aspiring Data Analyst passionate about turning raw data into actionable insights.
📧 urvansh11350@gmail.com
🔗 LinkedIn: [linkedin.com/in/urvansh-kumar-2b01a532b](https://linkedin.com/in/urvansh-kumar-2b01a532b)
💻 GitHub: [github.com/Urvansh-eng](https://github.com/Urvansh-eng)

---
⭐ If you found this project useful, feel free to star the repository!
