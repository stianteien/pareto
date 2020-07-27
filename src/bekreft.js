

var iframe = document.getElementById('SOLOWORK');
search();

function search() {
	setTimeout(function() {
		if(iframe.contentWindow.document.getElementsByName('confirm')[1]) {
			bekreft();
		}else{
			search();
		}
	},50);
}



function bekreft() {	
	iframe.contentWindow.document.getElementsByName('confirm')[1].click()
}	
