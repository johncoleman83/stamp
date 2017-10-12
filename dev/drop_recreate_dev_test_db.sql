-- creates MySQL database stamp_dev_db only if not existing
-- and gives privileges to user stamp_dev on DB
DROP DATABASE IF EXISTS stamp_dev_db;
CREATE DATABASE IF NOT EXISTS stamp_dev_db;
GRANT ALL PRIVILEGES ON stamp_dev_db.*
      TO stamp_dev@localhost
      IDENTIFIED BY 'stamp_dev_pwd';
GRANT SELECT ON performance_schema.*
      TO stamp_dev@localhost
      IDENTIFIED BY 'stamp_dev_pwd';
