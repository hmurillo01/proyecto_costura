/* codigo_js = 
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('crear_costurera_form').addEventListener('submit', function() {
        // Reinicia los valores de los campos del formulario
        document.getElementById('id_identificacion').value = '';
        document.getElementById('id_nombre').value = '';
        document.getElementById('id_apellido').value = '';
        document.getElementById('id_fecha_nacimiento').value = '';
        document.getElementById('id_direccion').value = '';
    });
}); */


document.addEventListener("DOMContentLoaded", function() {
    var form = document.getElementById("costurera-form");
    var modal = document.getElementById("modal-message");

    form.addEventListener("submit", function(event) {
        event.preventDefault();

        // Limpia los campos del formulario
        form.reset();

        // Muestra la modal con el mensaje de "Registro exitoso"
        modal.style.display = "block";

        // Cierra la modal después de 3 segundos
        setTimeout(function() {
            modal.style.display = "none";
        }, 2000);
    });
});


document.addEventListener("DOMContentLoaded", function() {
    var form = document.getElementById("fabrica-form");
    var modal = document.getElementById("modal-message");

    form.addEventListener("submit", function(event) {
        event.preventDefault();

        // Limpia los campos del formulario
        form.reset();

        // Muestra la modal con el mensaje de "Registro exitoso"
        modal.style.display = "block";

        // Cierra la modal después de 3 segundos
        setTimeout(function() {
            modal.style.display = "none";
        }, 3000);
    });
});



