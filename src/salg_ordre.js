javascript:
(function() {


var iframe = document.getElementById('SOLOWORK');
search();

function search() {
	setTimeout(function() {
		if(iframe.contentWindow.document.getElementsByName('amount')[0]) {
			handle();
		}else{
			search();
		}
	},50);
}

function handle() {
	iframe.contentWindow.document.getElementsByName('amount')[0].value = antall;
		 
	var pris = iframe.contentWindow.document.getElementsByClassName('progress progress-orderdepth progress-bid')[0].parentNode.parentNode.children[2].innerHTML;
	iframe.contentWindow.document.getElementsByName('limit')[0].value = pris;

	iframe.contentWindow.document.getElementsByName('next')[0].click();
}


})()