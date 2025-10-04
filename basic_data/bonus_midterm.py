#1/
import pandas as pd
import sqlite3
conn = sqlite3.connect("../databases/databases/Chinook_Sqlite.sqlite")

def top_invoices_in_range(conn, a, b, N):
    query = f"""
        SELECT InvoiceId, Total
        FROM Invoice
        WHERE Total BETWEEN {a} AND {b}
        ORDER BY Total DESC
        LIMIT {N};
    """
    return pd.read_sql(query, conn)
#2/
def top_customers_by_invoice_count(conn, N):
    query = f"""
        SELECT c.CustomerId, c.FirstName || ' ' || c.LastName AS CustomerName, COUNT(i.InvoiceId) AS InvoiceCount
        FROM Customer c
        JOIN Invoice i ON c.CustomerId = i.CustomerId
        GROUP BY c.CustomerId
        ORDER BY InvoiceCount DESC
        LIMIT {N};
    """
    return pd.read_sql(query, conn)
#3/
def top_customers_by_total_value(conn, N):
    query = f"""
        SELECT c.CustomerId, c.FirstName || ' ' || c.LastName AS CustomerName, SUM(i.Total) AS TotalSpent
        FROM Customer c
        JOIN Invoice i ON c.CustomerId = i.CustomerId
        GROUP BY c.CustomerId
        ORDER BY TotalSpent DESC
        LIMIT {N};
    """
    return pd.read_sql(query, conn)
#Test
print("TOP 5 hóa đơn từ 5 đến 20$:")
print(top_invoices_in_range(conn, 5, 20, 5))

print("\nTOP 5 khách hàng có nhiều invoice nhất:")
print(top_customers_by_invoice_count(conn, 5))

print("\nTOP 5 khách hàng chi tiêu cao nhất:")
print(top_customers_by_total_value(conn, 5))
