<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Validação</h1>
    <form action="" method="get">
        <input type="text" name="regex" id="">
        <input type="submit" value="Validar">
    </form>
    
</body>
</html>

<?php 
if(isset($_GET['regex'])){
    $valor = $_GET['regex'];
    echo"<h2> $valor </h2>";

    if(preg_match('/[0-9]/', $valor)){
        echo "Somente números";
        
    } else {
        echo "Contém outros caracteres";
    }
}
?>