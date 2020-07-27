

var iframe = document.getElementById('SOLOWORK');
iframe.contentWindow.document.getElementsByName('custodydd')[0].selectedIndex=3;
iframe.contentWindow.document.getElementsByName('custodydd')[0].dispatchEvent(new Event('change'));
