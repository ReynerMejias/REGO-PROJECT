document.getElementById('fechaFinal').addEventListener('change', function() {

    // Obtener las fechas de los inputs
    var fechaInicio = document.getElementById('fechaInicio').textContent;
    var dineroMes = document.getElementById('dineroMes').textContent;
    var fechaFin = document.getElementById('fechaFinal').value;
    
    fechaInicio = fechaInicio.split('/');
    fechaInicio = fechaInicio[2] + '-' + fechaInicio[1] + '-' + fechaInicio[0];
    
    // Verificar si ambas fechas están presentes
    if (fechaInicio && fechaFin) {
        // Crear objetos de fecha
        var inicio = new Date(fechaInicio);
        var fin = new Date(fechaFin);
        var dinero = parseInt(dineroMes);

        // Calcular la diferencia en meses
        var meses = (fin.getFullYear() - inicio.getFullYear()) * 12;
        meses -= inicio.getMonth();
        meses += fin.getMonth();

        // Ajustar basado en los días si es necesario
        if (fin.getDate() < inicio.getDate()) {
            meses--;
        }

        // Mostrar el resultado
        document.getElementById('resultado').value = meses * dinero;
    }
});