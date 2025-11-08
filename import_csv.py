import pandas as pd
from sqlalchemy import create_engine
import os

CSV_FILE = 'amazon_co-ecommerce_sample.csv'
TABLE_NAME = 'amazon'

# Create a NEW database for your data (not superset.db)
DB_FILE = 'amazon_data.db'

try:
    print(f"Reading {CSV_FILE}...")
    df = pd.read_csv(CSV_FILE)
    
    print(f"\nRows: {len(df)}, Columns: {len(df.columns)}")
    print(f"Columns: {list(df.columns)}")
    
    # Create connection to NEW database
    db_path = os.path.join(os.path.dirname(__file__), DB_FILE)
    engine = create_engine(f'sqlite:///{db_path}')
    
    print(f"\nCreating database: {DB_FILE}")
    print(f"Creating table: {TABLE_NAME}")
    
    # Upload to database
    df.to_sql(TABLE_NAME, engine, if_exists='replace', index=False)
    
    print(f"\n✓ SUCCESS!")
    print(f"✓ Database created: {db_path}")
    print(f"✓ Table '{TABLE_NAME}' created with {len(df)} rows")
    
    # Verify
    test_df = pd.read_sql(f"SELECT * FROM {TABLE_NAME} LIMIT 5", engine)
    print(f"\nFirst 5 rows from database:")
    print(test_df)
    
    print(f"\n{'='*60}")
    print(f"NEXT STEPS IN SUPERSET:")
    print(f"{'='*60}")
    print(f"1. Go to: http://localhost:8088")
    print(f"2. Click: Data → Database Connections → + Database")
    print(f"3. Select: SQLite")
    print(f"4. Connection String:")
    print(f"   sqlite:///{db_path}")
    print(f"5. Database name: Amazon_Database")
    print(f"6. Check: 'Allow file uploads to database'")
    print(f"7. Click: Connect")
    print(f"\n8. Then: Data → Datasets → + Dataset")
    print(f"9. Select database: Amazon_Database")
    print(f"10. Select table: {TABLE_NAME}")
    
except Exception as e:
    print(f"❌ ERROR: {str(e)}")
    import traceback
    traceback.print_exc()