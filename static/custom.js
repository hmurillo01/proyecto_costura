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
    const form = document.getElementById("costurera-form");
    const modal = document.getElementById("modal-message");

    form.addEventListener("submit", function(event) {
        event.preventDefault();

        // Enviar el formulario de manera asíncrona con AJAX
        fetch(form.action, {
            method: form.method,
            body: new FormData(form)
        })
        .then(response => {
            if (response.ok) {
                // Muestra la modal con el mensaje de "Registro exitoso"
                modal.style.display = "block";

                // Cierra el modal después de 5 segundos
                setTimeout(function() {
                    modal.style.display = "none";
                    form.reset();
                }, 5000);
            } else {
                // Manejar errores de respuesta del servidor
                console.error('Error al enviar el formulario');
            }
        })
        .catch(error => {
            console.error('Error al enviar el formulario:', error);
        });
    });
});



/* document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("fabrica-form");
    const modal = document.getElementById("modal-message");

    form.addEventListener("submit", function(event) {
        event.preventDefault();

        // Enviar el formulario de manera asíncrona con AJAX
        fetch(form.action, {
            method: form.method,
            body: new FormData(form)
        })
        .then(response => {
            if (response.ok) {
                // Muestra la modal con el mensaje de "Registro exitoso"
                modal.style.display = "block";

                // Cierra el modal después de 5 segundos
                setTimeout(function() {
                    modal.style.display = "none";
                    form.reset();
                }, 5000);
            } else {
                // Manejar errores de respuesta del servidor
                console.error('Error al enviar el formulario');
            }
        })
        .catch(error => {
            console.error('Error al enviar el formulario:', error);
        });
    });
}); */


