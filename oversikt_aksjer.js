


var iframe = document.getElementById('SOLOWORK');
var body = iframe.contentWindow.document.getElementsByClassName('gridview')[0].children[2].children;


var navn = new Array();
var kurs = new Array();
var gjkurs = new Array();
var prosent = new Array();
var gevinst = new Array();
var antall = new Array();
var totalverdi = new Array();

for(var i=0;i<body.length;i++) {
	navn.push(body[i].children[0].children[0].children[0].innerHTML);
	kurs.push(body[i].children[3].children[0].innerHTML.split("&nbsp;")[0]);
	gjkurs.push(body[i].children[6].children[0].innerHTML);
	prosent.push(body[i].children[7].children[0].innerHTML);
	gevinst.push(body[i].children[8].children[0].children[0].innerHTML);
	antall.push(body[i].children[9].children[0].innerHTML);
	totalverdi.push(body[i].children[11].children[0].innerHTML);
}

return [navn, kurs, gjkurs, prosent, gevinst, antall, totalverdi]