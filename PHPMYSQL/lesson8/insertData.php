<?php
    try{
        $pdo = new PDO ("mysql:host=localhost;dbname=db4","root","");

    $username = "Jack";
    $pass = "test";

    $sql = "INSERT INTO users (username,pass) VALUES ('$username','$pass')";

    $pdo -> exec($sql);

    echo "New record created successfully";

    }catch(Excpetion $e){
        echo $e -> getMessage();
    }

    //SELECT * FROM PRODUCTS AS P JOIN CATEGORIES AS C ON P.CATEGORY_ID = C.ID

    // SELECT products.name as 'Product name', categories.name as 'Category' FROM products INNER JOIN 
    // categories on products.category_id=categories.id
?>