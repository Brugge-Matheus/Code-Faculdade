<?php 
require 'Mysql_config.php';

    $id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);

    if($id) {
        $sql = $pdo->prepare("DELETE FROM clientes WHERE idCliente = :id");
        $sql->bindValue(':id', $id);
        $sql->execute();

    }
    
header('Location: index.php');
exit;
    