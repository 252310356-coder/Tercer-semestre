<?php
//Parte 1
//1. Crear un script PHP que declare varias variables de diferentes tipos (enteros,
//cadenas, arreglos, objetos).
//2. Asignar valores a las variables y mostrar el uso de memoria utilizando la
//función memory_get_usage().
//3. Liberar las variables (estableciéndolas en null o utilizando unset()) y
//mostrar nuevamente el uso de memoria.
//4. Comparar y comentar las diferencias observadas en el uso de memoria
//antes y después de liberar las variables.
class Carro {
    public $marca;
    public $modelo;

    public function __construct($marca, $modelo) {
        $this->marca = $marca;
        $this->modelo = $modelo;
    }
}

$carro1 = new Carro("Toyota", "Corolla");
$nombre = "Juan";
$edad = 30;
$personas = ["Ana", "Luis", "Carlos"];
echo "Uso de memoria despues de la declaracion: ", memory_get_usage(), "<br>";

$carro1 = null;
$nombre=null;
$edad=null;
$personas=null;
echo "Uso de memoria luego de la eliminacion: ", memory_get_usage(), "<br>";
//Parte 2
//Crear un script PHP que declare variables y referencias.
//2. Crear un arreglo grande y asignarlo a una variable.
//3. Asignar la variable del arreglo a una nueva variable por valor y por
//referencia.
//4. Modificar el arreglo a través de la referencia y observar los cambios.
//5. Mostrar el uso de memoria antes y después de realizar las modificaciones
echo "Segunda parte del codigo <br>";
$nombre = "Maria";
$edad = 25;
$personas = ["Ana", "Luis", "Carlos", "Pedro", "Sofia", "Marta", "Diego", "Lucia", "Javier", "Elena"];
$personas_ref = &$personas;
$personas_val = $personas;
echo "Uso de memoria despues de la declaracion: ", memory_get_usage(), "<br>";
$personas_ref = [0];
echo "Personas: <br>";
print_r($personas);
echo "<br>Personas por referencia: <br>";
print_r($personas_ref);
echo "<br>Personas por valor: <br>";
print_r($personas_val);
echo "<br>1Uso de memoria despues de la declaracion y modificacion: ", memory_get_usage(), "<br>";

//Parte 3
//1. Crear un script PHP que genere un gran número de objetos en un bucle.
//2. Liberar los objetos y forzar la ejecución del recolector de basura usando
//gc_collect_cycles().
//3. Mostrar el uso de memoria antes y después de la recolección de basura.
//4. Comentar sobre el impacto del recolector de basura en el manejo de
//memoria.
echo "Tercera parte del codigo <br>";
for ($i = 0; $i < 10000; $i++) {
    $carro = new Carro("Marca" . $i, "Modelo" . $i);
    $carros[] = $carro;
}
echo "Uso de memoria despues de la creacion de objetos: ", memory_get_usage(), "<br>";

unset($carros);
gc_collect_cycles();

echo "Uso de memoria luego de la recoleccion de basura: ", memory_get_usage(), "<br>";


?>