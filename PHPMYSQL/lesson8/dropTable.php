<?php
    try{

        $pdo = new PDO("mysql:host=localhost;dbname=db4","root","");

        $sql = "DROP TABLE products";

        $pdo->exec($sql);

        echo "Table dropped successfully!";

    }catch(PDOException $e){
        echo "Error dropping table: ". $e.getMessage();
    }
?>