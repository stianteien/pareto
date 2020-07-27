(function() {

var a = 9;
if(selg) {
	a = 10;
}

var iframe = document.getElementById('SOLOWORK');
 

iframe.contentWindow.document.getElementsByClassName('fund_search_name_textfield')[0].value = ticket ;
iframe.contentWindow.document.getElementsByClassName('button-orange fundsearch')[0].click();


click_orange(); 
function click_orange() {
	setTimeout(function() {
		if(iframe.contentWindow.document.getElementsByClassName('even')[0].children[a].children[0].children[0]) {
			iframe.contentWindow.document.getElementsByClassName('even')[0].children[a].children[0].children[0].click();
		}else{
			click_orange();
		}
	},50);
}


})()