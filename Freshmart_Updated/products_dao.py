
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="ROOT123",
        database="grocery_inventory"
    )

def get_all_products():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    cursor.close()
    conn.close()
    return products

def add_product(name, quantity, price_per_unit):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, quantity, price_per_unit) VALUES (%s, %s, %s)",
                   (name, quantity, price_per_unit))
    conn.commit()
    cursor.close()
    conn.close()

def update_product(id, name, quantity, price_per_unit):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET name=%s, quantity=%s, price_per_unit=%s WHERE id=%s",
                   (name, quantity, price_per_unit, id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_product(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()

def get_low_stock_products(threshold=5):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products WHERE quantity < %s", (threshold,))
    low_stock = cursor.fetchall()
    cursor.close()
    conn.close()
    return low_stock
