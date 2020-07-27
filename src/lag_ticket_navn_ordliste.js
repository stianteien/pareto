

/* se slik ut: {'tic':'navn', 'tik':'navnet'} */

document.getElementsByClassName('large-12 columns medium-12')[0].outerHTML = '<textarea id="tekst" rows="4" cols="50"> hei </textarea>';
var body = document.getElementsByClassName('table table-striped stock-list-development')[0].children[1].children;
var data = '{';

for(var i=0;i<body.length;i++) {
	data += '"'+body[i].children[4].children[0].innerHTML + '":"' + body[i].children[5].children[0].innerHTML + '",';
}

data = data.slice(0,-1);
data += '}';
document.getElementById('tekst').value = data;
return data
