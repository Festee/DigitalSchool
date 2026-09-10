<?php
    $my_file = fopen("ds.txt",'w');

    $my_text = "Digital school\n";

    fwrite($my_file,$my_text);
?>