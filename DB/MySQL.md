# MySQL
## Database 생성과 Table 생성

1. **Database**
   1. `SHOW DATABASES;` : 데이터베이스의 목록을 보여줌
   2. `CREATE DATABASE database_name;` : DB 생성
   3. `DROP DATABASE database_name;` : DB 제거
   4. `USE database_name;` : Table을 생성하는 것과 같은 일을 수행할 데이터베이스를 선택한다.
2. **Table**
   1. ```
      CREATE TABLE table_name (
        name VARCHAR(20),
        age INT
      );
      ```
      Table의 이름과 칼럼명 생성
   2. `SHOW TABLES;` : 테이블의 목록을 보여줌
   3. `DESC table_name;` : 특정한 테이블을 분석해줌.
   4. `DROP TABLE table_name` : 테이블 제거
   5. `INSERT INTO table_name (name, age) VALUES (val1, val2);` : 테이블의 row 값들 삽입
   6. `SELECT * FRROM table_name;` : 특정한 테이블의 모든 row 출력
3. **NULL**
    -  ```
        CREATE TABLE table_name(
          name VARCHAR(20) NOT NULL,
          age INT NOT NULL
        );
       ```
      `NOT NULL`을 특정 칼럼에 설정해 줄 수 있음. 그러면 NULL 값을 허용해주지 않아 특정 칼럼은 **필수**적으로 insert되어야 할 칼럼임을 명시해줌.
4. **DEFAULT**
    - table을 생성할 때 `name VARCHAR(20) DEFAULT 'No name'`으로 기본값을 설정해줄 수 있음. 
5. **Primary Key**
   1. table을 생성할 때 `id INT NOT NULL PRIMARY KEY`로 작성하면 id가 primary key로 지정이 되고 중복을 허용하지 않는 id값이 된다.
   2. `id INT NOT NULL AUTO_INCREMENT PRIMARY KEY`로 지정하면 id 값이 1부터 순차적으로 저절로 늘어나는 primary key가 된다.

## Table 조회와 수정, 삭제
1. Read 조회
   - `SELECT * FROM <table>`로 table을 조회할 수 있다. 
   - `*` 대신에 `name, age`와 같은 요소들을 삽입하여 특정 칼럼들만 조회할 수 있다.
   - `SELECT * FROM <table> WHERE <condition>` 에서 조건을 설정하여 조건을 만족하는 row들만 조회할 수 있다.
   - `SELECT name AS '이름'`을 통해 조회되는 Table의 칼럼명을 지정할 수 있다.
2. Update 수정
   - `UPDATE <table> SET <col>=<val> WHERE <condition>` : 조건을 만족하는 칼럼들의 값을 `<val>`로 수정한다. 
3. Delete 삭제
   - `DELETE FROM <table> WHERE <condition>` : 조건을 만족하는 row를 삭제할 수 있다.
   - `DELETE FROM <table>`을 통해 전체 테이블의 데이터를 삭제할 수 있다. Table의 구조를 지우는 것은 아니며 Table 전체를 없애고 싶을 때는 `DROP TABLE <table>`을 사용한다.