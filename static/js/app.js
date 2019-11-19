// Mi código JavaScript:


//Cargo la fecha del sistema

document.getElementById("fecha").innerHTML = fecha();

function fecha() {
    var d = new Date(),
        minutes = d.getMinutes().toString().length == 1 ? '0' + d.getMinutes() : d.getMinutes(),
        hours = d.getHours().toString().length == 1 ? '0' + d.getHours() : d.getHours(),
        ampm = d.getHours() >= 12 ? 'pm' : 'am',
        months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Setiembre', 'Octubre', 'Noviembre', 'Diciembre'],
        days = ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'];
    return days[d.getDay()] + ', ' + d.getDate() + ' de ' + months[d.getMonth()] + ' de ' + d.getFullYear(); //+' '+hours+':'+minutes+ampm;
}

//Cargo la hora del sistema

function clock() {

    //Save the times in variables
    var today = new Date();

    var hours = today.getHours();
    var minutes = today.getMinutes();
    var seconds = today.getSeconds();

    /*
        //Set the AM or PM time
        if (hours >= 12) {
            meridiem = " PM";
        } else {
            meridiem = " AM";
        }

        //convert hours to 12 hour format and put 0 in front
        if (hours > 12) {
            hours = hours - 12;
        } else if (hours === 0) {
            hours = 12;
        }
    */
    //Put 0 in front of single digit minutes and seconds

    if (minutes < 10) {
        minutes = "0" + minutes;
    } else {
        minutes = minutes;
    }

    if (seconds < 10) {
        seconds = "0" + seconds;
    } else {
        seconds = seconds;
    }
    document.getElementById("clock").innerHTML = (hours + ":" + minutes + ":" + seconds);
}
setInterval('clock()', 1000);