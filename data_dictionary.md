# Data Dictionary

## Dataset 01: Fund Master

| Column | Data Type | Description |
|----------|----------|----------|
| amfi_code | INTEGER | Unique AMFI scheme identifier |
| fund_house | TEXT | Mutual fund company |
| scheme_name | TEXT | Name of scheme |
| category | TEXT | Scheme category |

---

## Dataset 02: NAV History

| Column | Data Type | Description |
|----------|----------|----------|
| amfi_code | INTEGER | Scheme identifier |
| date | DATE | NAV date |
| nav | REAL | Net Asset Value |