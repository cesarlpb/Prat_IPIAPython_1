// Variable global para almacenar la instancia del gráfico
let myChart = null;

// Función para generar un array del 1 al 10000
function generateLargeArray() {
    return Array.from({length: 10000}, (_, i) => i + 1);
}

// Agregar un listener al formulario para manejar el evento de envío
document.getElementById('searchForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevenir el envío del formulario por defecto

    const array = generateLargeArray(); // Generar el array automáticamente
    const target = Number(document.getElementById('target').value);

    // Realizar una solicitud POST al servidor para realizar las búsquedas
    fetch('/search', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ array, target }) // Convertir los datos a JSON
    })
    .then(response => response.json()) // Parsear la respuesta JSON
    .then(data => {
        // Actualizar los resultados en la interfaz de usuario
        document.getElementById('binaryResult').textContent = `Búsqueda Binaria - Tiempo: ${data.binary.time.toFixed(6)} segundos`;
        document.getElementById('linearResult').textContent = `Búsqueda Lineal - Tiempo: ${data.linear.time.toFixed(6)} segundos`;
        
        // Llamar a la función para actualizar el gráfico con los nuevos datos
        updateChart(data.binary.time, data.linear.time);
    })
    .catch(error => console.error('Error:', error)); // Manejo de errores
});

// Función para actualizar el gráfico con los nuevos tiempos de ejecución
function updateChart(binaryTime, linearTime) {
    const ctx = document.getElementById('comparisonChart').getContext('2d');
    
    // Destruir el gráfico anterior si ya existe para evitar superposición
    if (myChart) {
        myChart.destroy();
    }
    
    // Crear una nueva instancia del gráfico con los datos actualizados
    myChart = new Chart(ctx, {
        type: 'bar', // Tipo de gráfico: barras
        data: {
            labels: ['Búsqueda Binaria', 'Búsqueda Lineal'], // Etiquetas de las barras
            datasets: [{
                label: 'Tiempo de Ejecución (segundos)', // Etiqueta del dataset
                data: [binaryTime, linearTime], // Datos para las barras
                backgroundColor: ['#007bff', '#ff0000'], // Colores de fondo de las barras
                borderColor: ['#0056b3', '#b30000'], // Colores de borde de las barras
                borderWidth: 1 // Ancho del borde de las barras
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true, // Iniciar el eje Y desde cero
                    ticks: {
                        // Función de callback para formatear los valores del eje Y
                        callback: function(value) {
                            return value.toFixed(6) + ' s'; // Mostrar los valores en segundos
                        }
                    }
                }
            },
            plugins: {
                legend: {
                    display: true, // Mostrar la leyenda
                    labels: {
                        // Función para generar etiquetas de leyenda con colores correspondientes
                        generateLabels: function(chart) {
                            return chart.data.labels.map(function(label, i) {
                                return {
                                    text: label, // Texto de la etiqueta
                                    fillStyle: chart.data.datasets[0].backgroundColor[i] // Color de la etiqueta
                                };
                            });
                        }
                    }
                }
            }
        }
    });
}
