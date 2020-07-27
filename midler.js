
var iframe = document.getElementById('SOLOWORK');

var markedsverdi = iframe.contentWindow.document.getElementsByClassName('toppanel table')[0].children[0].children[0].children[0].children[1].innerHTML.split(" NOK")[0];
var tilgjenlig = iframe.contentWindow.document.getElementsByClassName('toppanel table')[0].children[0].children[3].children[0].children[1].innerHTML.split(" NOK")[0];

return [markedsverdi, tilgjenlig]