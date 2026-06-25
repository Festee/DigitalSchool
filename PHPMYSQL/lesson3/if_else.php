<?php

    $mosha = 25;

    // if($mosha < 18){
    //     echo "Shko n'shkoll !!!";
    // }else{
    //     echo "Shko nfakultet !!!";
    // }

    if($mosha < 18){
        echo "Shko ne shkolle";
    }
    else if($mosha == 21){
        echo "Nisja fakultetit";
    }
    else if($mosha > 21){
        echo "Vazhdo me pune";
    }
    else{
        echo "Nuk ka moshe";
    }

?>