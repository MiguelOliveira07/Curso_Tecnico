<?php

    echo 'hello world!<br>';
    print 'Olá Mundo<br>';

    $nome = 'Miguel<br>';
    $idade = '18';
    $funciona = true;
    $altura = 2.57;

    if ($idade < 18){
        echo 'Miguel é novo<br>';
    } else {
        echo 'Miguel é velho<br>';
    }

    echo 'Tenho: ';
    echo $idade + $altura;
    echo ' anos';
    
    $dia = 'sexta';

    switch ($dia) {
        case 'segunda':
            echo 'Inicio da semana<br>';
            break;
        case 'sexta':
            echo '<br>Amém<br>';
        }

    for( $i = 0; $i <= 100; $i+=20 ){
        echo "Valor: $i <br>";
    }

    $i = 0;
    while ( $i < 100) {
        $i+=10;
        echo "Valor (while): $i <br>";
    }

?>

<h1>Tag de Título</h1>