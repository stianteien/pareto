
	
	
	var body = document.getElementsByClassName('cell-table cell-table--quote-list')[0].children[1].children;
	
	var navn = new Array();
	var tatt_inn = new Array();
	var mnd_sluttkurs = new Array();
	var kurs = new Array();
	var endring_i_dag = new Array();
	var endring_mnd = new Array();
	
	for(var i=0;i<body.length;i++) {
		navn.push(body[i].children[0].innerHTML);
		tatt_inn.push(body[i].children[1].innerHTML);
		mnd_sluttkurs.push(body[i].children[3].innerHTML);
		kurs.push(body[i].children[4].innerHTML);
		endring_i_dag.push(body[i].children[5].innerHTML);
		endring_mnd.push(body[i].children[6].children[0].innerHTML);
		
		
	}
	
	
	
	return [navn, tatt_inn, mnd_sluttkurs, kurs, endring_i_dag, endring_mnd]
	
	
