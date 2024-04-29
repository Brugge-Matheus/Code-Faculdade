<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CRUD</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" integrity="sha512-SnH5WK+bZxgPHs44uWIX+LLJAJ9/2PkPKZ5QiAj6Ta86w+fsb2TkcmfRyVX3pBnMFcV7oQPJkl9QevSCWr3W6A==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <style>
        h1 {
            font-family: Arial, Helvetica, sans-serif;
            text-align: center;
            color: black;
        }

        a {
            font-family: Arial, Helvetica, sans-serif;
            color: black;
        }


        /* Tabela */
        table {
            margin: 20px 0;
        }

        i {
            padding: 5px;
            font-size: 1.2em;
            transition: 0.2s;
            text-decoration: none;
            color: black;

        }

        i:hover {
            transform: scale(1.2);
            transition: 0.2s;
        }

        .fa-trash:hover {
            color: red;
        }

        .fa-circle-plus:hover {
            color: green;
        }

        a {
            text-decoration: none;
        }

        table {
            border: 1px solid black;
            border-collapse: collapse;
            background-color: #f5f5f5;
            width: 100%;
            margin-bottom: 20px;
        }

        th, td {
            padding: 8px;
            text-align: left;
        }

        th {
            background-color: #333;
            color: #fff;
        }

        tr:nth-child(even) {
            background-color: #ddd;
        }

        tr:hover {
            background-color: #ccc;
        }

        /* Formularios */
        .form-container {
            width: 100%;
            max-width: 400px; /* Ajuste conforme necessário */
            margin: 0 auto;
        }

        .form-group {
            margin-bottom: 20px;
        }

        .form-group label {
            display: block;
            font-weight: bold;
        }

        .form-group input {
            width: 100%;
            padding: 8px;
            box-sizing: border-box;
            border: 1px solid #ccc;
            border-radius: 4px;
            margin: 10px 0;
        }

        .form-group textarea {
            height: 100px; /* Ajuste conforme necessário */
        }

        .form-group input[type="submit"],
        .form-group input[type="button"] {
            padding: 10px 20px;
            background-color: #333;
            color: #fff;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }

        .form-group input[type="submit"]:hover,
        .form-group input[type="button"]:hover {
            background-color: #555;
        }

        
    </style>
</head>
